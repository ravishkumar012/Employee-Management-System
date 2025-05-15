
# Employee Management System – Edunet Foundation

## 👨‍💼 Project Title
**Employee Management System**  
Built with 🐍 Python + 📊 Streamlit + 🗄️ MySQL  
A user-friendly web-based dashboard for managing employee data, developed by students of MIT, Meerut.

---

## 🧠 Objective

To build an interactive and secure system for:
- Adding, editing, deleting employee records
- Analyzing salary and department distributions
- Managing user accounts with login authentication
- Contacting admins via a message form

You can use this project at :
- [Home Page](https://emp-system.streamlit.app/)



- [Admin Dashboard](https://emp-system1.streamlit.app/)
---

## 🛠️ Technologies Used

| Tech | Purpose |
|------|---------|
| **Streamlit** | Web interface |
| **Python** | Core logic |
| **MySQL** | Backend database |
| **Pandas** | Data handling |
| **Matplotlib** | Data visualization |
| **HTML/CSS** | Custom styling |

---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/mehta-g1/employee-management-system.git
cd employee-management-system
```

### 2️⃣ Install Required Libraries

```bash
pip install streamlit pandas mysql-connector-python matplotlib pillow streamlit-option-menu
```

### 3️⃣ Set Up the MySQL Database

#### Open MySQL and run:

```sql
CREATE DATABASE project;
USE project;

CREATE TABLE user_password (
    empid INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(20),
    department VARCHAR(50),
    username VARCHAR(50),
    password VARCHAR(100),
    email VARCHAR(100),
    mobile VARCHAR(15),
    salary FLOAT
);

CREATE TABLE emp_data (
    empid INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    department VARCHAR(50),
    position VARCHAR(100),
    salary FLOAT,
    address TEXT,
    mobile VARCHAR(15),
    email VARCHAR(100),
    merital_status BOOLEAN,
    start_date VARCHAR(100)
);
```

✅ Or use an existing database like [freesqldatabase.com](https://www.freesqldatabase.com/) and update credentials in `empdata.py` and `app.py`.

---

## 🚀 Running the App

### 🔹 Main Site (Landing + Register/Login)

```bash
streamlit run app.py
```

### 🔹 Admin Dashboard (After Login)

```bash
streamlit run empdata.py
```

---

## 🎯 Key Features

### 👤 Login System
- Username + Password authentication
- Forgot Password via username & mobile number
- New account creation with auto-generated usernames

### 🧾 Employee Management
- Add/Edit/Delete employees
- Search by Employee ID
- Validate age, mobile number, email, salary

### 📊 Data Visualization
- Salary range pie chart (Low/Medium/High)
- Department-wise distribution chart

### 📩 Contact Us
- Send feedback, questions, or issues
- Data saved into `messages.csv` with timestamps

### 📁 Admin Panel
- View all employee data
- Visual dashboard & quick navigation via sidebar
- Responsive layout with custom CSS

---

## 🧑‍💻 Developer

| Name | GitHub / LinkedIn |
|------|--------------------|
| Vikash Kumar Mehta | [GitHub](https://github.com/Mehta-g1) / [Linkedin](https://www.linkedin.com/in/mehta-g1?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)|


---

## 📷 Screenshots

Included screenshots of:
- Login page
- Add employee form
- Dashboard overview
- Salary & department charts

---

## 📌 Future Enhancements

- Add profile photo upload
- Role-based access (Admin vs User)
- Export data to Excel or PDF
- Cloud deployment (e.g. Render, Streamlit Cloud)

---
