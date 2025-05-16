# 🧾 Recipe Book

A simple Django web app where you can add your favorite recipes with a **title**, **description**, and an **image**. All added recipes are displayed below the form.

---

## 🛠 Features

- 📄 Add a recipe title and description
- 🖼️ Upload an image of the recipe
- 📋 View all submitted recipes in a list
- 🌐 Built using Django

---

## 📷 Demo

![Demo Screenshot](media/demo.png)  
*(Optional — add a screenshot of your project here if you like)*

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/nikghost17/Recipe-Project.git
cd recipe-book
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate    # On Windows
# OR
source venv/bin/activate # On macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Run the Development Server

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your browser to use the app.
