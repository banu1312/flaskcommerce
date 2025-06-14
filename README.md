# 🛍️ FlaskCommerce API

FlaskCommerce adalah RESTful API untuk e-commerce sederhana sebagai project akhir semester. API ini mendemonstrasikan integrasi antara **relational database (MySQL)** dan **NoSQL (MongoDB)**, dengan fitur autentikasi JWT dan manajemen user serta produk.

---

## 🚀 Fitur

- ✅ Register & Login dengan JWT Authentication
- 🔐 Token Refresh & Logout (JWT Blacklisting)
- 🛍️ CRUD Produk (MySQL via SQLAlchemy)
- 📝 CRUD Review (MongoDB via PyMongo)
- 🔗 Sinkronisasi data produk (MySQL) dan review (MongoDB)
- 👤 User Profile (Protected Endpoint)

---

## ⚙️ Tech Stack

- **Flask** — Web framework
- **Flask-SQLAlchemy** — ORM untuk MySQL
- **PyMySQL** — Driver untuk MySQL
- **Flask-JWT-Extended** — JWT Authentication
- **Flask-Migrate** — Database migration
- **Flask-Cors** — CORS middleware
- **PyMongo** — Akses MongoDB
- **Marshmallow (opsional)** — Validasi & serialisasi (jika digunakan)

---

## 📦 Library yang harus di-install

```txt
Flask
Flask-SQLAlchemy
PyMySQL
Flask-Migrate
Flask-JWT-Extended
Flask-Cors
pymongo
dnspython


INSTALL DENGAN : pip3 install -r requirements.txt

# Clone repository
git clone https://github.com/USERNAME/flaskcommerce.git
cd flaskcommerce

# Buat dan aktifkan virtual environment
python3 -m venv venv
source venv/bin/activate

# Install semua dependensi
pip install -r requirements.txt

# Set environment variable (opsional untuk JWT_SECRET, dll.)
export FLASK_APP=run.py

# Inisialisasi dan migrate database MySQL
flask db init
flask db migrate
flask db upgrade

# Jalankan server Flask
flask run


POST /register
Content-Type: application/json

{
  "name": "Raditya",
  "email": "raditya@mail.com",
  "password": "123456"
}


POST /login
Content-Type: application/json

{
  "email": "raditya@mail.com",
  "password": "123456"
}

{
  "access_token": "eyJ0eXAiOiJKV1QiLCJh...",
  "refresh_token": "eyJhbGciOiJIUzI1NiJ9..."
}

GET /me
Authorization: Bearer <access_token>

📌 Catatan
Gunakan MySQL untuk produk dan user, MongoDB untuk review

Pastikan database flaskcommerce (MySQL) dan koleksi review (MongoDB) tersedia

Review MongoDB mengandung field product_id yang mengacu ke produk di MySQL

📤 Deployment
Kamu bisa deploy project ini ke:

🟦 Render.com (Flask support)

☁️ Railway, Heroku (dengan Procfile)

🌐 Vercel (jika frontend menyatu)

👨‍💻 Author
Raditya Banuputra Syamil
S1 Informatika, Developer & E-commerce Tech Enthusiast
