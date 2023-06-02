سلام.
پروژه سایت محاسبات سریع که بکند سایت با پایتون و جنگو نوشته شده.
نحوه اجرا:
* ابتدا پایتون 3 را در سیستم عامل خود نصب کنید.
* محیط venv درست کنید:
``` Command Prompt
python -m venv venv
```
* برای فعال سازی محیط مجازی از کد زیر استفاده کنید:
* ویندوز:
``` Command Prompt
.\venv\Scripts\activate
```
در صورتی که هنگام فعالسازی به مشکل خوردید، [این سایت را ببینید](https://www.sharepointdiary.com/2014/03/fix-for-powershell-script-cannot-be-loaded-because-running-scripts-is-disabled-on-this-system.html)
* لینوکس و یا مک:
``` bash
source venv/bin/activate
```
* سپس پکیج های مورد نیاز را از فایل requirements.txt نصب کنید. (میتوانید از دستور زیر استفاده کنید)
``` Command Prompt
pip install -r requirements.txt
```
* سپس با دستور زیر پروژه را اجرا کنید:
``` Command Prompt
python manage.py runserver
```
پروژه روی پورت 8000 ران میشود و از طریق http://localhost:8000/ یا http://127.0.0.1:8000/ در دسترس است.
