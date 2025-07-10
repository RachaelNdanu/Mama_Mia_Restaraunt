# Django Restaurant Website Demo 🍽️

![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.12%2B-blue.svg)


This demo app provides a basic website for a fictitious restaurant, allowing customers to view the menu, learn more about the restaurant, and make a reservation.

Built using the [Django](https://www.djangoproject.com/) web framework (Python), SQLite, HTML, CSS, and Tailwind.

## 🌄 Screenshots

![dan-poynor-django-restaurant-app](https://github.com/danpoynor/django-restaurant-website-demo/assets/764270/e0494afd-fc3e-42bc-81f3-63f664d62532)

---

## ✨ Features

- **Home Page** – Landing page with hero banner and feature sections.
- **About Page** – Learn more about the restaurant’s story.
- **Booking Page** – Reserve a table using a Django form.
- **Menu Page** – Browse available meals.
- **Menu Item Page** – View individual meal details.
- **Admin Interface** – Manage bookings and menu items.
- **Responsive Design** – Works well on desktop and mobile.

---

## 📦 Installation and Setup

Follow these steps to run the project locally:

### 1. Clone the repository:

```bash
git clone <repository-url>
cd <project-directory>
```

### 2. Create and activate a virtual environment:

```bash
python3 -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables:

Create your `.env` file based on the provided example:

```bash
nano .env
```

To get the secret key, run the following command in your activated environment:
(You only need to do this once, and you can reuse the key later.)

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

and paste it into your `.env` file:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
```

### 5. Run migrations:

```bash
python manage.py migrate
```

### 6. Create an admin user:

```bash
python manage.py createsuperuser
```

Follow the prompts to complete the setup.

### 7. Run the development server:

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser to view the app.

---

## ⚙️ Environment Configuration

This project uses a `.env` file for local configuration. Example:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
```

A sample `.env.example` file is included. **Do not commit `.env`** to version control.

---

## 🖼️ Static Files and Images

Static assets (CSS, images) are located under:

```
restaurant/static/
```

Images are stored in:

```
restaurant/static/img/
```

During development (`DEBUG=True`), Django will serve these automatically.

---

## 🔐 Admin Area

To access the Django admin:

1. Start the server:

```bash
python manage.py runserver
```

2. Visit [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

3. Log in using your superuser credentials.

You can manage menu items and bookings under the **RESTAURANT** section.

---

## 🧪 Running Tests

The app includes tests for models, views, and forms. To run them:

```bash
python manage.py test
```
