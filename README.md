# 📚 Library Management System

## Project Overview

The **Library Management System** is a console-based application developed using **Python** and **MySQL**. The project demonstrates how a team collaborates using **Git** and **GitHub** by dividing work into modules, working on feature branches, creating Pull Requests, reviewing code, and merging changes.

This project is developed for learning:

* Python Programming
* MySQL Database
* Git & GitHub Collaboration
* Modular Programming
* Team-Based Software Development

---

# Team Members

| Role          | Responsibility                                                                                          |
| ------------- | ------------------------------------------------------------------------------------------------------- |
| Team Lead     | Repository Management, Database, Authentication, Issue/Return Module, Reports, Integration, Code Review |
| Contributor 1 | Book Management Module                                                                                  |
| Contributor 2 | Member Management Module                                                                                |

---

# Technologies Used

* Python 3.x
* MySQL
* Git
* GitHub

---

# Project Features

## Authentication

* Admin Login

## Book Management

* Add Book
* Update Book
* Delete Book
* Search Book
* Display All Books

## Member Management

* Register Member
* Update Member
* Delete Member
* Search Member
* Display All Members

## Issue & Return Management

* Issue Book
* Return Book
* View Issued Books

## Reports

* Total Books
* Available Books
* Issued Books
* Total Members

---

# Project Structure

```text
Library-Management-System/
│
├── auth/
│   ├── login.py
│   └── auth_service.py
│
├── config/
│   └── db_config.py.example
│
├── database/
│   ├── connection.py
│   ├── create_database.sql
│   ├── create_tables.sql
│   └── sample_data.sql
│
├── menus/
│   ├── main_menu.py
│   ├── book_menu.py
│   ├── member_menu.py
│   ├── issue_menu.py
│   └── report_menu.py
│
├── models/
│   ├── book.py
│   ├── member.py
│   ├── issue.py
│   └── user.py
│
├── services/
│   ├── book_service.py
│   ├── member_service.py
│   ├── issue_service.py
│   ├── report_service.py
│   └── auth_service.py
│
├── docs/
├── tests/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Database Tables

The project uses the following tables:

* users
* books
* members
* issued_books

---

# Module Responsibilities

### Team Lead

* Project Setup
* GitHub Repository Management
* Database Design
* Authentication
* Main Menu
* Issue & Return Module
* Reports
* Integration
* Testing
* Documentation

### Contributor 1

Book Management

* Book Model
* Book CRUD
* Book Menu

### Contributor 2

Member Management

* Member Model
* Member CRUD
* Member Menu

---

# Git Branch Strategy

```text
main

↓

develop

├── feature-book-module

├── feature-member-module

├── feature-authentication

├── feature-issue-return

└── feature-reports
```

---

# GitHub Workflow

```text
Create Repository

↓

Initial Project Setup

↓

Create develop Branch

↓

Assign GitHub Issues

↓

Create Feature Branch

↓

Develop Module

↓

Commit Changes

↓

Push Branch

↓

Create Pull Request

↓

Code Review

↓

Merge into develop

↓

Integration Testing

↓

Merge develop → main
```

---

# Database Setup

### Step 1

Create the database by executing:

```
database/create_database.sql
```

### Step 2

Create all tables by executing:

```
database/create_tables.sql
```

### Step 3

Insert sample records by executing:

```
database/sample_data.sql
```

### Step 4

Copy

```
config/db_config.py.example
```

to

```
config/db_config.py
```

Update your MySQL username and password.

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project directory

```bash
cd Library-Management-System
```

Install required package

```bash
pip install -r requirements.txt
```

Run the application

```bash
python main.py
```

---

# Learning Objectives

This project demonstrates:

* Python Project Structure
* Object-Oriented Programming
* MySQL Database Connectivity
* CRUD Operations
* Modular Programming
* Git Branching Strategy
* GitHub Collaboration
* Pull Requests
* Code Reviews
* Merge Process
* Team-Based Software Development

---

# Future Improvements

* Barcode Scanner Support
* Student Login
* Book Reservation
* Fine Calculation
* Dashboard
* Export Reports (PDF/Excel)
* Email Notifications

---

# License

This project is developed for educational purposes.
