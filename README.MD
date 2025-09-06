# 📘 Django Project Setup Guide
Here we're using 
1.Django as Python Framework for web developement
2.Maria db as Database
........

## 🔹 Prerequisites
Make sure you have the following installed on your system:
- [Python 3.9+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [MariaDB](https://mariadb.org/download/)
- [Git](https://git-scm.com/downloads) (optional, if using version control)

---


## 🔹 1. Clone the Project
```bash
git clone https://github.com/PrajwalBS-coder/UV-env-With-Django.git
cd your-django-project
```

---
## Here we're using uv As Virtul env

https://github.com/astral-sh/uv/releases

download from above url


## 🔹 2. Create & Activate Virtual Environment
```bash
uv venv
```

- On Linux/Mac:
  ```bash
  source venv/bin/activate
  ```
- On Windows:
  ```bash
  venv\Scripts\activate
  ```

---

---
After activating virtul env
## 🔹 3. Install Dependencies
```bash
uv pip install -r requirements.txt
```

---

## 🔹 4. Setup MariaDB Database
downlod from here https://mariadb.org/download/
### Log into MariaDB
```bash
mysql -u root -p
```

### Create Database & User
```sql
CREATE DATABASE my_django_db;
CREATE USER 'django_user'@'localhost' IDENTIFIED BY 'StrongPassword123!';
GRANT ALL PRIVILEGES ON my_django_db.* TO 'django_user'@'localhost';
FLUSH PRIVILEGES;
```

---

## 🔹 5. Configure Django Settings

In `project/settings.py`, update `DATABASES`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   
        'NAME': 'my_django_db',
        'USER': 'django_user',
        'PASSWORD': 'StrongPassword123!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

---

## 🔹 6. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🔹 7. Create Superuser
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin login.

---

## 🔹 8. Run the Development Server
```bash
python manage.py runserver
```

Now open your browser and go to:  
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🔹 9. Access Django Admin
Visit:  
👉 [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)  
Login using the superuser credentials you created.

---

## 🔹 10. (Optional) Run in Production
For production, you may need:
- Gunicorn / uWSGI
- Nginx / Apache
- Docker (optional)
- Environment variables for secrets

---

✅ You’re now ready to run your Django project with **MariaDB** as the database.
