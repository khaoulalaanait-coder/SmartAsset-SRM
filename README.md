# SmartAsset SRM

## Technologies

- Django
- Django REST Framework (DRF)
- PostgreSQL
- React
- JWT Authentication
- Docker (later)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/khaoulalaanait-coder/SmartAsset-SRM.git

cd SmartAsset-SRM
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

The backend will be available at:

```
http://127.0.0.1:8000/
```

The Django admin interface is available at:

```
http://127.0.0.1:8000/admin/
```