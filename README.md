# 🦁 ProxyProwler

<div align="center">
  <img src="https://img.shields.io/badge/ProxyProwler-v1.0-blueviolet?style=for-the-badge&logo=python" alt="ProxyProwler Version">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python" alt="Python Version">
  <img src="https://img.shields.io/github/workflow/status/Argh94/ProxyProwler/ProxyProwler?label=Workflow&style=flat-square" alt="Workflow Status">
  <img src="https://img.shields.io/github/license/Argh94/ProxyProwler?label=License&style=flat-square" alt="License">
</div>

<div align="center">
  <p><strong>آخرین به‌روزرسانی:</strong> 22:17 11-12-1404 (به وقت ایران)</p>
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

### 🔗 SOCKS5 Proxies (48 Active)

| # | سرور (Server) | پورت (Port) | پینگ (Ping) | وضعیت (Status) |
|---|---------------|-------------|-------------|----------------|
| 1 | `8.210.17.35` | `8081` | 178.98ms | ✅ فعال |
| 2 | `8.219.191.219` | `8118` | 200.11ms | ✅ فعال |
| 3 | `79.110.200.148` | `8081` | 137.13ms | ✅ فعال |
| 4 | `113.212.111.4` | `8090` | 241.89ms | ✅ فعال |
| 5 | `211.38.188.120` | `9080` | 160.82ms | ✅ فعال |

</div>

<div align="center">

### 🔗 SOCKS4 Proxies (61 Active)

| # | سرور (Server) | پورت (Port) | پینگ (Ping) | وضعیت (Status) |
|---|---------------|-------------|-------------|----------------|
| 1 | `121.43.109.88` | `3129` | 572.25ms | ✅ فعال |
| 2 | `68.71.254.6` | `4145` | 77.52ms | ✅ فعال |
| 3 | `154.94.238.147` | `50161` | 180.98ms | ✅ فعال |
| 4 | `47.250.51.110` | `31281` | 240.88ms | ✅ فعال |
| 5 | `123.57.1.16` | `5555` | 232.91ms | ✅ فعال |

</div>

<div align="center">

### 🔗 HTTPS Proxies (31 Active)

| # | سرور (Server) | پورت (Port) | پینگ (Ping) | وضعیت (Status) |
|---|---------------|-------------|-------------|----------------|
| 1 | `31.40.204.250` | `80` | 192.92ms | ✅ فعال |
| 2 | `8.219.97.248` | `80` | 195.39ms | ✅ فعال |
| 3 | `41.191.203.164` | `80` | 256.41ms | ✅ فعال |
| 4 | `45.225.207.182` | `999` | 1150.86ms | ✅ فعال |
| 5 | `47.250.159.65` | `8008` | 203.77ms | ✅ فعال |

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
