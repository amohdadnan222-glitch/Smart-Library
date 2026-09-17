# 📚 Smart Library Management System

A Flask-based web application for managing library operations with **role-based access, book management, user authentication, issue/return tracking, search functionality, dashboards, and SQLite database integration**.

---

## 📌 Project Overview

The **Smart Library Management System** is a web-based application developed using Python and Flask to simplify common library management activities.

The system provides separate functionality for users and administrators, allowing books and users to be managed efficiently through a centralized web interface.

The project demonstrates practical implementation of:

- User authentication
- Role-based access control
- Book catalogue management
- Book issue and return tracking
- Search functionality
- Dashboard-based management
- SQLite database integration
- Responsive web interface

---

## ✨ Features

### 🔐 User Authentication

The system provides secure user authentication functionality.

Users can:

- Register a new account
- Log in using their credentials
- Access features according to their assigned role
- Log out securely

Passwords are stored using password hashing rather than plain-text storage.

---

### 👥 Role-Based Access

The application supports different levels of access for users.

The role-based system allows administrators to perform management operations while regular users can access the functionality available to them.

This helps prevent unauthorized access to administrative features.

---

### 📚 Book Catalogue

The book catalogue allows users to view available books in the library.

The system maintains information such as:

- Book title
- Author
- Category
- Availability
- Other relevant book information

Users can search the catalogue to find books more easily.

---

### 📖 Book Issue & Return

The system supports tracking of library books.

Library operations include:

- Issuing books
- Recording issued books
- Returning books
- Tracking book availability
- Maintaining issue/return records

This reduces the need for manual record keeping.

---

### 🔎 Book Search

A search functionality is provided to help users quickly find books from the catalogue.

Books can be searched based on available book information such as title, author, or other relevant fields.

---

### 📊 Dashboard

The application provides dashboard functionality for managing and viewing library information.

The dashboard can provide an overview of important library records and activities.

---

### 🗄️ SQLite Database

The application uses **SQLite** for local database management.

The database stores information related to:

- Users
- Books
- Library transactions
- Issue and return records
- Other application data

Database operations are separated into dedicated Python modules to keep the application organized.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python** | Backend application development |
| **Flask** | Web application framework |
| **SQLite** | Database management |
| **HTML** | Web page structure |
| **CSS** | User interface styling |
| **Bootstrap** | Responsive UI components |
| **Jinja2** | Dynamic HTML templates |
| **Werkzeug** | Password hashing and security |
| **Gunicorn** | Production WSGI server |

---

---

## 🖥️ Application Screenshots

### 🏠 Home Page

The home page provides the main entry point to the Smart Library Management System.

![Home Page](Home-page.png)

---

### 🔐 User Login

The login page allows registered users to securely access the application.

![User Login](User-login.png)

---

### 📝 User Registration

New users can create an account through the registration page.

![User Registration](User-registration.png)

---

### 📚 Book Catalogue

The book catalogue displays available books and provides access to library book information.

![Book Catalogue](Book-Catalogue.png)

---

## 🔄 Application Workflow

```text
                ┌──────────────────┐
                │    Home Page     │
                └────────┬─────────┘
                         │
                ┌────────▼─────────┐
                │ Login / Register │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │ Authentication   │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │    Dashboard     │
                └────────┬─────────┘
                         │
              ┌──────────┼──────────┐
              │          │          │
              ▼          ▼          ▼
          ┌───────┐  ┌───────┐  ┌──────────┐
          │ Books │  │ Search│  │ Issue /  │
          │       │  │       │  │ Return   │
          └───────┘  └───────┘  └──────────┘
                         │
                         ▼
                ┌──────────────────┐
                │ SQLite Database  │
                └──────────────────┘

---



## 🏗️ Application Architecture

The application follows a simple Flask-based web architecture.

```text
                    ┌─────────────────────┐
                    │      Web Browser    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Flask App       │
                    │       app.py        │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
       ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
       │ Authentication│ │ Book Module │ │ Dashboard   │
       └─────────────┘  └─────────────┘  └─────────────┘
              │                │                │
              └────────────────┼────────────────┘
                               ▼
                    ┌─────────────────────┐
                    │   SQLite Database   │
                    └─────────────────────┘
