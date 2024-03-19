# Password Manager

### Requirements to run this app:

- Python 3.+
- Venv

### How to run this app?

Clone this repository and enter the folder. Create a virtual environment.

```bash
python3 -m venv venv
```

You need to activate virtual env:

```bash
source venv/bin/activate
```

Now run this command in the terminal to install the required libraries:

```bash
pip install -r requirements.txt
```

Migrate the db:

```
python manage.py makemigrations
python manage.py migrate
```

For admin panel, first create a superuser:

```bash
python3 manage.py createsuperuser
```

Start server:

```bash
python3 manage.py runserver
```

**Go to** http://127.0.0.1:8000/

### Screenshots:

![home](/assets/1.png)

![add](/assets/2.png)

![login](/assets/3.png)

![register](/assets/4.png)

![passwords](/assets/5.png)
