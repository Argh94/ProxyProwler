# 🦁 ProxyProwler

<div align="center">
  <img src="https://img.shields.io/badge/ProxyProwler-v1.0-blueviolet?style=for-the-badge&logo=python" alt="ProxyProwler Version">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python" alt="Python Version">
  <img src="https://img.shields.io/github/workflow/status/Argh94/ProxyProwler/ProxyProwler?label=Workflow&style=flat-square" alt="Workflow Status">
  <img src="https://img.shields.io/github/license/Argh94/ProxyProwler?label=License&style=flat-square" alt="License">
</div>

<div align="center">
  <p><strong>آخرین به‌روزرسانی:</strong> 12:48 03-08-1404 (به وقت ایران)</p>
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

### 🔗 SOCKS5 Proxies (67 Active)

| # | سرور (Server) | پورت (Port) | پینگ (Ping) | وضعیت (Status) |
|---|---------------|-------------|-------------|----------------|
| 1 | `45.43.83.18` | `6301` | 127.07ms | ✅ فعال |
| 2 | `45.131.209.91` | `80` | 8.97ms | ✅ فعال |
| 3 | `185.148.104.52` | `80` | 8.97ms | ✅ فعال |
| 4 | `104.18.191.172` | `80` | 16.78ms | ✅ فعال |
| 5 | `104.18.40.47` | `80` | 8.71ms | ✅ فعال |

</div>

<div align="center">

### 🔗 SOCKS4 Proxies (25 Active)

| # | سرور (Server) | پورت (Port) | پینگ (Ping) | وضعیت (Status) |
|---|---------------|-------------|-------------|----------------|
| 1 | `144.139.210.56` | `80` | 216.16ms | ✅ فعال |
| 2 | `101.200.158.109` | `8880` | 204.76ms | ✅ فعال |
| 3 | `64.64.152.248` | `39593` | 40.26ms | ✅ فعال |
| 4 | `192.252.215.2` | `4145` | 81.16ms | ✅ فعال |
| 5 | `166.88.169.119` | `6726` | 18.23ms | ✅ فعال |

</div>

<div align="center">

### 🔗 HTTPS Proxies (56 Active)

| # | سرور (Server) | پورت (Port) | پینگ (Ping) | وضعیت (Status) |
|---|---------------|-------------|-------------|----------------|
| 1 | `104.19.66.163` | `80` | 8.77ms | ✅ فعال |
| 2 | `104.17.106.99` | `80` | 17.08ms | ✅ فعال |
| 3 | `141.101.122.238` | `80` | 8.78ms | ✅ فعال |
| 4 | `104.17.247.188` | `80` | 16.28ms | ✅ فعال |
| 5 | `104.16.0.165` | `80` | 16.20ms | ✅ فعال |

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
