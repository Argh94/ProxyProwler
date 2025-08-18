import requests
import re
import random
import time
import logging
import socket
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import pytz
import jdatetime
import timeit
import json

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
]

def get_random_user_agent():
    return random.choice(USER_AGENTS)

def check_proxy_status(server, port, timeout=3):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((server, int(port)))
        sock.close()
        if result == 0:
            logging.info(f"Proxy {server}:{port} is online")
            return True
        else:
            logging.warning(f"Proxy {server}:{port} is offline or unreachable")
            return False
    except (socket.timeout, socket.gaierror, ConnectionRefusedError) as e:
        logging.error(f"Error checking proxy {server}:{port}: {e}")
        return False

def measure_proxy_ping(server, port, timeout=3, tries=1):
    total_time = 0
    successful_tries = 0
    for _ in range(tries):
        start_time = timeit.default_timer()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((server, int(port)))
            sock.close()
            if result == 0:
                elapsed = (timeit.default_timer() - start_time) * 1000 
                total_time += elapsed
                successful_tries += 1
                logging.debug(f"Ping for {server}:{port}: {elapsed:.2f}ms")
            else:
                logging.warning(f"Ping failed for {server}:{port}")
        except (socket.timeout, socket.gaierror, ConnectionRefusedError) as e:
            logging.error(f"Ping error for {server}:{port}: {e}")
        time.sleep(0.2)
    if successful_tries > 0:
        average_ping = total_time / successful_tries
        logging.info(f"Average ping for {server}:{port}: {average_ping:.2f}ms")
        return average_ping
    return None

def fetch_proxies_from_url(url, proxy_type, max_proxies=50):
    proxies = []
    headers = {'User-Agent': get_random_user_agent()}
    pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}$'
    
    try:
        logging.info(f"Fetching {proxy_type} proxies from {url}")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        proxy_checks = []
        
        content_type = response.headers.get('content-type', '')
        if 'application/json' in content_type:
            try:
                data = response.json()
                logging.info(f"Processing JSON content from {url}")
                for item in data[:max_proxies]:
                    ip = item.get('ip')
                    port = item.get('port')
                    if ip and port:
                        proxy = f"{ip}:{port}"
                        if re.match(pattern, proxy):
                            server, port = proxy.split(':')
                            proxy_checks.append((proxy, server, port))
                        else:
                            logging.debug(f"Invalid {proxy_type} proxy format in JSON: {proxy}")
                    else:
                        logging.debug(f"Missing ip or port in JSON item: {item}")
            except json.JSONDecodeError as e:
                logging.error(f"Invalid JSON format from {url}: {e}")
                return []
        else:
            lines = response.text.splitlines()
            for line in lines[:max_proxies]:
                line = line.strip()
                if not line:
                    continue
                if re.match(pattern, line):
                    server, port = line.split(':')
                    proxy_checks.append((line, server, port))
                else:
                    logging.debug(f"Invalid {proxy_type} proxy format: {line}")
        
        with ThreadPoolExecutor(max_workers=10) as executor:
            future_to_proxy = {executor.submit(check_proxy_status, server, port): (proxy, server, port) for proxy, server, port in proxy_checks}
            for future in as_completed(future_to_proxy):
                proxy, server, port = future_to_proxy[future]
                try:
                    if future.result():
                        ping = measure_proxy_ping(server, port)
                        if ping is not None:
                            proxies.append((proxy, ping))
                            logging.info(f"Valid and online {proxy_type} proxy: {proxy} (Ping: {ping:.2f}ms)")
                        else:
                            logging.warning(f"Skipping {proxy_type} proxy {proxy} due to ping failure")
                    else:
                        logging.warning(f"Skipping offline {proxy_type} proxy: {proxy}")
                except Exception as e:
                    logging.error(f"Error checking {proxy_type} proxy {proxy}: {e}")
                time.sleep(0.1)
        
        logging.debug(f"Proxies fetched for {proxy_type}: {proxies}")
        return proxies
    except requests.RequestException as e:
        logging.error(f"HTTP error fetching {url}: {e}")
        return []

def save_proxies_to_file(proxies, proxy_type):
    output_dir = os.getenv('OUTPUT_DIR', '/tmp/proxies')
    filename = f"{output_dir}/{proxy_type}.txt"
    try:
        unique_proxies = list(set(proxy[0] for proxy in proxies))
        logging.debug(f"Unique proxies for {proxy_type}: {unique_proxies}")
        os.makedirs(output_dir, exist_ok=True)
        with open(filename, 'w', encoding='utf-8') as file:
            if unique_proxies:
                for proxy in unique_proxies:
                    file.write(proxy + '\n')
            else:
                file.write('')
        logging.info(f"Saved {len(unique_proxies)} unique {proxy_type} proxies to {filename}")
        if os.path.exists(filename):
            logging.info(f"Confirmed: {filename} exists in {output_dir}")
        else:
            logging.error(f"Failed: {filename} was not created")
        return proxies
    except IOError as e:
        logging.error(f"Error writing to {filename}: {e}")
        return []

def update_readme(proxy_dict):
    try:
        utc_now = datetime.now(pytz.UTC)
        iran_tz = pytz.timezone('Asia/Tehran')
        iran_now = utc_now.astimezone(iran_tz)
        jalali_date = jdatetime.datetime.fromgregorian(datetime=iran_now)
        update_time_iran = jalali_date.strftime('%H:%M %d-%m-%Y')
        logging.info(f"Updating README with Iranian timestamp: {update_time_iran}")

        proxy_counts = {ptype: len(proxies) for ptype, proxies in proxy_dict.items()}
        
        table_rows = ""
        for proxy_type, proxies in proxy_dict.items():
            table_rows += f"\n<div align=\"center\">\n\n### 🔗 {proxy_type} Proxies ({proxy_counts[proxy_type]} Active)\n\n"
            table_rows += "| # | سرور (Server) | پورت (Port) | پینگ (Ping) | وضعیت (Status) |\n"
            table_rows += "|---|---------------|-------------|-------------|----------------|\n"
            sample_proxies = random.sample(proxies, min(5, len(proxies))) if proxies else []
            if not sample_proxies:
                table_rows += f"| - | - | - | - | هیچ پروکسی فعالی یافت نشد |\n"
            for i, (proxy, ping) in enumerate(sample_proxies, 1):
                server, port = proxy.split(':')
                status = "✅ فعال" if ping is not None else "❌ غیرفعال"
                table_rows += f"| {i} | `{server}` | `{port}` | {ping:.2f}ms | {status} |\n"
            table_rows += "\n</div>\n"

        readme_content = f"""# 🦁 ProxyProwler

<div align="center">
  <img src="https://img.shields.io/badge/ProxyProwler-v1.0-blueviolet?style=for-the-badge&logo=python" alt="ProxyProwler Version">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python" alt="Python Version">
  <img src="https://img.shields.io/github/workflow/status/Argh94/ProxyProwler/ProxyProwler?label=Workflow&style=flat-square" alt="Workflow Status">
  <img src="https://img.shields.io/github/license/Argh94/ProxyProwler?label=License&style=flat-square" alt="License">
</div>

<div align="center">
  <p><strong>آخرین به‌روزرسانی:</strong> {update_time_iran} (به وقت ایران)</p>
  <p><strong>فایل‌های پروکسی:</strong> فایل‌های <code>SOCKS5.txt</code>, <code>SOCKS4.txt</code>, <code>HTTPS.txt</code>, و <code>requirements.txt</code> در <a href="https://github.com/Argh94/ProxyProwler/releases">بخش Releases</a> در دسترس هستند.</p>
</div>

**ProxyProwler** یک ابزار قدرتمند و خودکار پایتون برای جمع‌آوری، بررسی و مدیریت پروکسی‌های **SOCKS5**، **SOCKS4** و **HTTPS** از منابع عمومی است. این پروژه با هدف ارائه پروکسی‌های فعال و باکیفیت برای توسعه‌دهندگان و کاربران طراحی شده و خروجی‌ها را در فایل‌های مرتب ذخیره می‌کند.

---

## 🎯 چرا ProxyProwler؟
- 🌐 **جمع‌آوری خودکار**: پروکسی‌ها از منابع معتبر و به‌روز جمع‌آوری می‌شوند.
- ⚡ **بررسی کیفیت**: وضعیت آنلاین بودن و پینگ هر پروکسی بررسی می‌شود.
- 🗑 **حذف تکراری‌ها**: پروکسی‌های تکراری به‌صورت خودکار حذف می‌شوند.
- 📊 **خروجی مرتب**: پروکسی‌ها در فایل‌های جداگانه ذخیره می‌شوند.
- 🖥 **رابط کاربری حرفه‌ای**: اطلاعات پروکسی‌ها در README با جدول‌های زیبا نمایش داده می‌شود.

---

## 🚀 ویژگی‌ها
- **پشتیبانی از منابع متنوع**: جمع‌آوری پروکسی از لینک‌های متنی و JSON.
- **اجرای موازی**: استفاده از ThreadPoolExecutor برای بررسی سریع پروکسی‌ها.
- **اندازه‌گیری پینگ**: نمایش پینگ هر پروکسی برای انتخاب بهترین‌ها.
- **حذف پروکسی‌های غیرفعال**: فقط پروکسی‌های آنلاین ذخیره می‌شوند.
- **به‌روزرسانی دستی**: از طریق GitHub Actions قابل اجرا است.

---

## 📋 پیش‌نیازها
برای اجرای این پروژه به موارد زیر نیاز دارید:
- 🐍 **پایتون 3.9 یا بالاتر**
- 📦 **کتابخانه‌های مورد نیاز**:
  - `requests`
  - `pytz`
  - `jdatetime`
- نصب وابستگی‌ها:
  ```bash
  pip install -r requirements.txt

## 🛠 نحوه استفاده
1. **دانلود پروکسی‌ها**:
   - فایل‌های <code>SOCKS5.txt</code>, <code>SOCKS4.txt</code>, <code>HTTPS.txt</code>, و <code>requirements.txt</code> را از <a href="https://github.com/model7855/ProxyProwler/releases">بخش Releases</a> دانلود کنید.
2. **استفاده در ابزارها**:
   - پروکسی‌ها را در کلاینت‌های خود (مثل مرورگرها یا ابزارهای شبکه) وارد کنید.
3. **اجرای دستی**:
   - Workflow را از تب <strong>Actions</strong> در GitHub اجرا کنید تا پروکسی‌ها به‌روزرسانی شوند.

---

## 🌍 منابع پروکسی
ProxyProwler از منابع معتبر زیر برای جمع‌آوری پروکسی‌ها استفاده می‌کند:

<div align="center">

| منبع | نوع پروکسی | لینک |
|------|-------------|------|
| OpenProxyList | SOCKS5, SOCKS4, HTTPS | [GitHub](https://github.com/roosterkid/openproxylist) |
| KangProxy | SOCKS5, SOCKS4, HTTPS | [GitHub](https://github.com/officialputuid/KangProxy) |
| Proxifly | SOCKS5, SOCKS4, HTTPS | [GitHub](https://github.com/proxifly/free-proxy-list) |
| Hookzof | SOCKS5 | [GitHub](https://github.com/hookzof/socks5_list) |
| TheSpeedX | SOCKS5, SOCKS4 | [GitHub](https://github.com/TheSpeedX/SOCKS-List) |
| Jetkai | SOCKS5 | [GitHub](https://github.com/jetkai/proxy-list) |
| ProxyScrape | SOCKS5 | [API](https://api.proxyscrape.com) |

</div>

---

## 📈 نمونه پروکسی‌ها
جدول‌های زیر نمونه‌ای از پروکسی‌های فعال (حداکثر ۵ نمونه برای هر نوع) را همراه با پینگ و وضعیت آن‌ها نمایش می‌دهند:

{table_rows}

> **💡 نکته**: برای دسترسی به لیست کامل و به‌روز پروکسی‌ها، فایل‌های مربوطه را از <a href="https://github.com/Argh94/ProxyProwler/releases">بخش Releases</a> دانلود کنید.

---

## 🛠 عیب‌یابی
اگر با مشکلی مواجه شدید، این مراحل را امتحان کنید:
- **خطای نصب کتابخانه‌ها**: مطمئن شوید فایل `requirements.txt` را از Releases دانلود کرده‌اید.
- **عدم تولید فایل‌های پروکسی**: لاگ‌های GitHub Actions را بررسی کنید تا ببینید آیا منابع پروکسی در دسترس هستند.
- **پروکسی‌های غیرفعال**: منابع پروکسی ممکن است موقتاً از دسترس خارج شوند. منابع جدید را به لیست `proxy_urls` اضافه کنید.

---

## 🤝 مشارکت در پروژه
ما از مشارکت شما استقبال می‌کنیم! برای کمک به بهبود ProxyProwler:
1. مخزن را فورک کنید.
2. تغییرات خود (مثل اضافه کردن منابع جدید یا بهبود کد) را اعمال کنید.
3. Pull Request بفرستید.
ایده‌های جدید یا گزارش باگ‌ها را از طریق **Issues** در GitHub مطرح کنید.

---

## 📜 لایسنس
این پروژه تحت **[لایسنس MIT](https://github.com/Argh94/ProxyProwler/blob/main/Files/LISENSE)** منتشر شده است. شما آزادید که از کد استفاده کنید، تغییر دهید و به اشتراک بگذارید.

---

<div align="center">
  <p><strong>🚀 ProxyProwler</strong> - با قدرت به دنبال پروکسی‌های فعال!</p>
  <p>برای سوالات یا پیشنهادات، در <a href="https://github.com/Argh94/ProxyProwler/issues">GitHub</a> با ما در تماس باشید.</p>
</div>
"""
        filename = "README.md"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(readme_content)
        logging.info(f"Successfully updated {filename}")
        if os.path.exists(filename):
            logging.info(f"Confirmed: {filename} exists in the repository root")
        else:
            logging.error(f"Failed: {filename} was not created")
    except Exception as e:
        logging.error(f"Error updating {filename}: {e}")

if __name__ == "__main__":
    proxy_urls = {
        'SOCKS5': [
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks5/socks5.txt",
            "https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/protocols/socks5/data.txt",
            "https://raw.githubusercontent.com/hookzof/socks5_list/master/tg/socks.json",
            "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
            "https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&proxytype=socks5"
        ],
        'SOCKS4': [
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks4/socks4.txt",
            "https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/protocols/socks4/data.txt",
            "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt"
        ],
        'HTTPS': [
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
            "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
            "https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/protocols/http/data.txt"
        ]
    }
    proxy_type = sys.argv[1] if len(sys.argv) > 1 else None
    proxy_dict = {}
    if proxy_type and proxy_type in proxy_urls:
        all_proxies = []
        for url in proxy_urls[proxy_type]:
            proxies = fetch_proxies_from_url(url, proxy_type)
            all_proxies.extend(proxies)
        proxy_dict[proxy_type] = all_proxies
        save_proxies_to_file(all_proxies, proxy_type)
    else:
        for proxy_type, urls in proxy_urls.items():
            all_proxies = []
            for url in urls:
                proxies = fetch_proxies_from_url(url, proxy_type)
                all_proxies.extend(proxies)
            proxy_dict[proxy_type] = all_proxies
            save_proxies_to_file(all_proxies, proxy_type)

    logging.debug(f"Final proxy_dict: {proxy_dict}")
    update_readme(proxy_dict)
