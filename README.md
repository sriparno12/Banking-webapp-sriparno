# 🏦 StreamBank App

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Issues](https://img.shields.io/github/issues/PruthvirajChavan45/streambank-app)
![Stars](https://img.shields.io/github/stars/PruthvirajChavan45/streambank-app?style=social)

A **simple banking management system** built with **Python & Streamlit**.  
This project allows users to create and manage accounts with features like deposit, withdrawal, updating info, and deleting accounts - all through a clean web interface.  

> 💡 Ideal for learning **OOP concepts**, **Python development**, and **Streamlit web apps**.  

---

## ✨ Features

- 👤 Create a new account with a unique account number  
- 💰 Deposit money (up to ₹10,000 per transaction)  
- 🏧 Withdraw money (with balance check)  
- 📑 View account details (secured with PIN)  
- ✏️ Update account information (name, email, PIN)  
- 🗑️ Delete account permanently  
- 🔒 PIN-protected authentication for all operations  
- 📂 Data stored locally in a JSON file (`data.json`)  

---

## 📂 Project Structure

```
streambank-app/
│── app.py              # Streamlit frontend (UI + interactions)
│── bank.py             # Backend logic for bank operations
│── requirements.txt    # Required Python libraries
│── data.json           # Auto-generated file to store account data
│── screenshots/        # App UI screenshots for README.md
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/PruthvirajChavan45/streamlit-bank.git
cd streamlit-bank
```

Create a virtual environment (recommended):

```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the Streamlit app:

```
streamlit run app.py
```

By default, the app runs locally at:

👉 [http://localhost:8501/](http://localhost:8501/)  

---

## 📸 Screenshots

### 🏠 Home Page
![Home Screenshot](screenshots/home.png)

### 👤 Create Account
![Create Account Screenshot](screenshots/create-account.png)

### 💰 Deposit Money
![Deposit Screenshot](screenshots/deposit.png)

### 🏧 Withdraw Money
![Withdraw Screenshot](screenshots/withdraw.png)

### 📑 Account Details
![Show Details Screenshot](screenshots/show_details.png)

### ✏️ Update Your Info
![Update Info Screenshot](screenshots/update_info.png)

### 🗑️ Delete Account
![Delete Account Screenshot](screenshots/delete_account.png)

---

## 🔮 Future Improvements

- Add **transaction history** and filter options  
- Implement **user authentication via email**  
- Integrate a **database** (SQLite / PostgreSQL) for robust storage  
- Deploy online using **Streamlit Cloud / Heroku**  
- Add **unit tests** and improved error handling  

> ⚡ These features are planned for future updates to make the app more complete and production-ready.

---

## 🛠️ Tech Stack

- **Python 3.x**  
- **Streamlit** (UI framework)  
- **JSON** (local storage)  

---

## 👨‍💻 Author

Developed and modified by Sriparno Chowdhury
linkedin: https://www.linkedin.com/in/sriparno-chowdhury-92a58416a/

