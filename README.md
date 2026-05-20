# 🔐 Secure Authentication System with Two-Factor Verification

A production-ready authentication system built with **Django**, featuring Two-Factor Authentication (2FA) via email OTP, a robust password policy, security question verification, and full password history protection.

---

## ✨ Features

### 🔑 Registration
- Username, email, and password signup
- **Security question** set at registration for extra identity verification
- Real-time password validation on the frontend

### 🛡️ Password Policy
- Minimum **8 characters**
- Must contain at least one **uppercase** letter
- Must contain at least one **lowercase** letter
- Must contain at least one **digit**
- **Password history check** — prevents reuse of recent passwords (hashed & stored securely)

### 🔒 Login & 2FA Flow
```
Enter Username & Password
        ↓
Credentials Verified
        ↓
OTP Code sent to registered Email
        ↓
Enter OTP + Security Question Answer
        ↓
Access Granted ✅
```

### 🔄 Password Reset
- Full forgot-password flow via email
- Reset link sent to registered email
- Confirmation page after successful reset

---

## 🛠️ Tech Stack

| Category        | Technology                  |
|-----------------|-----------------------------|
| Backend         | Python, Django 4.2          |
| Database        | SQLite                      |
| Frontend        | HTML5, CSS3                 |
| Authentication  | Django Auth + Custom User   |
| 2FA             | Email OTP (Django send_mail)|
| Password Security | Django Hashers (PBKDF2)  |
| Session Storage | Django Sessions             |

---

## 📁 Project Structure

```
FinalProject1/
│
├── app1/
│   ├── models.py        # CustomUser with security question & password history
│   ├── views.py         # Signup, Login, 2FA verify, Logout logic
│   ├── validators.py    # UniquePasswordValidator — blocks password reuse
│   ├── urls.py          # App URL routing
│   └── admin.py         # Admin panel config
│
├── templates/
│   ├── signup.html           # Registration form
│   ├── login.html            # Login form
│   ├── verifycode.html       # OTP + Security question form
│   ├── home.html             # Dashboard (login required)
│   ├── incorrectCode.html    # Wrong OTP page
│   ├── password_reset_form.html    # Forgot password
│   ├── password_reset_confirm.html # New password form
│   └── password_reset_done.html    # Reset success page
│
├── FinalProject1/
│   ├── settings.py      # Django settings + email config
│   └── urls.py          # Root URL config
│
└── manage.py
```

---

## 🗄️ Database Models

### `CustomUser` (extends AbstractUser)
| Field            | Type         | Description                  |
|------------------|--------------|------------------------------|
| username         | CharField    | Unique username               |
| email            | EmailField   | Used for OTP delivery         |
| password         | CharField    | Hashed with PBKDF2            |
| security         | CharField    | Security question answer      |
| password_history | M2M          | Stores past hashed passwords  |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation
```bash
# 1. Clone the repository
git clone https://github.com/Hirad1380/Login.git
cd Login

# 2. Install dependencies
pip install django

# 3. Apply migrations
python manage.py migrate

# 4. Run the server
python manage.py runserver
```

### Email Configuration
In `settings.py`, configure your email credentials:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'
```

> ⚠️ Use an **App Password** from your Google account — not your regular Gmail password.

---

## 🔁 Authentication Flow Detail

1. **Signup** → User registers with username, email, password & security answer
2. **Login** → Credentials checked → OTP generated & emailed
3. **Verify** → User submits OTP + security answer → Session validated
4. **Home** → Accessible only with `@login_required`
5. **Logout** → Session cleared → Redirected to login

---

## 👨‍💻 Author

**Hirad Bayat**  
M.Sc. Applied Computer Science — University of Duisburg-Essen  
📧 Bayathirad7@gmail.com  
🔗 LinkedIn: [Hirad Bayat](https://www.linkedin.com/in/hirad-bayat)  
🐙 GitHub: [Hirad1380](https://github.com/Hirad1380)
