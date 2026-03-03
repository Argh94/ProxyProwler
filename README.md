# 🦁 ProxyProwler

<div align="center">
  <img src="https://img.shields.io/badge/ProxyProwler-v1.0-blueviolet?style=for-the-badge&logo=python" alt="ProxyProwler Version">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python" alt="Python Version">
  <img src="https://img.shields.io/github/workflow/status/Argh94/ProxyProwler/ProxyProwler?label=Workflow&style=flat-square" alt="Workflow Status">
  <img src="https://img.shields.io/github/license/Argh94/ProxyProwler?label=License&style=flat-square" alt="License">
</div>

<div align="center">
  <p><strong>آخرین به‌روزرسانی:</strong> 22:18 12-12-1404 (به وقت ایران)</p>
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


<div align="center">

### 🔗 SOCKS5 Proxies (55 Active)

| # | سرور (Server) | پورت (Port) | پینگ (Ping) | وضعیت (Status) |
|---|---------------|-------------|-------------|----------------|
| 1 | `186.148.180.46` | `999` | 106.95ms | ✅ فعال |
| 2 | `23.95.242.79` | `3128` | 39.35ms | ✅ فعال |
| 3 | `61.158.175.38` | `9002` | 195.57ms | ✅ فعال |
| 4 | `141.98.153.86` | `80` | 156.69ms | ✅ فعال |
| 5 | `84.39.112.144` | `3128` | 159.96ms | ✅ فعال |

</div>

<div align="center">

### 🔗 SOCKS4 Proxies (55 Active)

| # | سرور (Server) | پورت (Port) | پینگ (Ping) | وضعیت (Status) |
|---|---------------|-------------|-------------|----------------|
| 1 | `184.178.172.25` | `15291` | 126.67ms | ✅ فعال |
| 2 | `8.221.138.111` | `9080` | 116.96ms | ✅ فعال |
| 3 | `192.111.135.17` | `18302` | 89.28ms | ✅ فعال |
| 4 | `70.166.167.38` | `57728` | 130.02ms | ✅ فعال |
| 5 | `45.116.114.37` | `5678` | 1267.65ms | ✅ فعال |

</div>

<div align="center">

### 🔗 HTTPS Proxies (23 Active)

| # | سرور (Server) | پورت (Port) | پینگ (Ping) | وضعیت (Status) |
|---|---------------|-------------|-------------|----------------|
| 1 | `69.70.244.34` | `80` | 131.92ms | ✅ فعال |
| 2 | `46.249.100.124` | `80` | 156.05ms | ✅ فعال |
| 3 | `8.219.97.248` | `80` | 166.87ms | ✅ فعال |
| 4 | `31.40.204.250` | `80` | 706.06ms | ✅ فعال |
| 5 | `5.161.155.252` | `80` | 71.64ms | ✅ فعال |

</div>


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
