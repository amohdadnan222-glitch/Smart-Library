# 📚 Smart Library Management System

A web-based **Library Management System** built with **Python, Flask, SQLite, HTML, CSS, and Bootstrap**.

The system provides role-based access for **Students, Teachers, and Administrators** and helps manage books, borrowing, returns, searching, user profiles, and library records through a centralized web application.

---

## 🚀 Project Overview

Smart Library is designed to simplify common library operations through a web-based platform.

Instead of managing library records manually, the system provides dedicated functionality for different users and keeps important library information organized in a SQLite database.

### 👥 User Roles

- **Student**
  - View available books
  - Search for books
  - View issued books
  - Track borrowing information
  - Manage profile information

- **Teacher**
  - Search and view books
  - Issue books
  - View issued books
  - Process book returns
  - Manage profile information

- **Administrator**
  - Manage the library system
  - Access administrative functions
  - Manage records and system information

---

## ✨ Key Features

### 🔐 Authentication & Role-Based Access
Separate authentication and access flows are provided for students, teachers, and administrators.

### 📖 Book Management
The system maintains book records and tracks important information such as availability.

### 🔎 Book Search
Books can be searched using information such as:

- Title
- Author
- ISBN
- Category

### 📤 Issue & Return Management
The system records book issuing and returning operations and updates book availability accordingly.

### 📊 Library Records
Borrowing information is stored in the SQLite database, including issue dates, return dates, status, and fines.

### 👤 Profile Management
Users can access and update their profile information.

### 🎨 Responsive Web Interface
The frontend uses HTML, CSS, and Bootstrap to provide a clean web interface.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Application logic |
| Flask | Web framework |
| SQLite | Database |
| HTML | Page structure |
| CSS | Styling |
| Bootstrap | Responsive UI |
| Jinja2 | Dynamic HTML templates |

---

## 🏗️ Project Structure

```text
Smart-Library/
│
├── static/
│   └── css/
│
├── templates/
│
├── app.py
├── database.py
├── update_database.py
├── hash_admin_password.py
├── requirements.txt
├── .gitignore
└── README.md
