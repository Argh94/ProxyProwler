# 🦁 ProxyProwler

<div align="center">
  <img src="https://img.shields.io/badge/ProxyProwler-v1.0-blueviolet?style=for-the-badge&logo=python" alt="ProxyProwler Version">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python" alt="Python Version">
  <img src="https://img.shields.io/github/workflow/status/Argh94/ProxyProwler/ProxyProwler?label=Workflow&style=flat-square" alt="Workflow Status">
  <img src="https://img.shields.io/github/license/Argh94/ProxyProwler?label=License&style=flat-square" alt="License">
</div>

<div align="center">
  <p><strong>آخرین به‌روزرسانی:</strong> 21:59 28-07-1404 (به وقت ایران)</p>
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

### 🔗 SOCKS5 Proxies (82 Active)

| # | سرور (Server) | پورت (Port) | پینگ (Ping) | وضعیت (Status) |
|---|---------------|-------------|-------------|----------------|
| 1 | `45.67.215.11` | `80` | 2.21ms | ✅ فعال |
| 2 | `5.45.126.128` | `8080` | 101.88ms | ✅ فعال |
| 3 | `195.85.23.157` | `80` | 2.25ms | ✅ فعال |
| 4 | `212.183.88.241` | `80` | 2.37ms | ✅ فعال |
| 5 | `209.50.172.71` | `3129` | 1.45ms | ✅ فعال |

</div>

<div align="center">

### 🔗 SOCKS4 Proxies (43 Active)

| # | سرور (Server) | پورت (Port) | پینگ (Ping) | وضعیت (Status) |
|---|---------------|-------------|-------------|----------------|
| 1 | `101.255.24.98` | `3128` | 233.20ms | ✅ فعال |
| 2 | `202.40.181.220` | `31247` | 278.39ms | ✅ فعال |
| 3 | `209.50.172.71` | `3129` | 4.82ms | ✅ فعال |
| 4 | `1.0.0.4` | `80` | 2.43ms | ✅ فعال |
| 5 | `8.213.129.15` | `8080` | 765.67ms | ✅ فعال |

</div>

<div align="center">

### 🔗 HTTPS Proxies (51 Active)

| # | سرور (Server) | پورت (Port) | پینگ (Ping) | وضعیت (Status) |
|---|---------------|-------------|-------------|----------------|
| 1 | `89.116.250.4` | `80` | 2.28ms | ✅ فعال |
| 2 | `185.162.229.172` | `80` | 2.53ms | ✅ فعال |
| 3 | `104.17.190.13` | `80` | 2.73ms | ✅ فعال |
| 4 | `45.131.211.217` | `80` | 2.27ms | ✅ فعال |
| 5 | `104.129.194.43` | `10336` | 2.96ms | ✅ فعال |

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
