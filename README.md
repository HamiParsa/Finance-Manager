<div align="center">
  <img src="https://img.shields.io/badge/Finance_Tracker-6C63FF?style=for-the-badge&logoColor=white"/>
  <h1>📊 Finance Tracker</h1>
  <p><b>Smart way to manage your money</b></p>
  <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js&logoColor=white"/>
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white"/>
  <img src="https://img.shields.io/badge/Tailwind-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white"/>
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white"/>
</div>

## 📖 About

Finance Tracker is a full-stack web application that helps you manage your personal finances. Track your income, expenses, and budgets with an intuitive dashboard and real-time charts.

**Live Demo:** Coming Soon

## ✨ Features

### User Features
- 🔐 Secure JWT authentication
- 📊 Interactive dashboard with charts
- 💰 Add and manage transactions
- 📁 Organize with custom categories
- 📈 Set monthly budgets
- 📱 Fully responsive design

### Admin Features
- 🛠️ Django admin panel
- 👥 User management
- 📋 Full CRUD operations

## 🛠️ Tech Stack

### Frontend
- Next.js 14 (App Router)
- TypeScript
- Tailwind CSS
- Chart.js + Recharts
- Heroicons

### Backend
- Django 5.0
- Django REST Framework
- SQLite
- JWT Authentication
- CORS

## 📁 Project Structure
<code>
finance-tracker/
├── backend/
│ ├── accounts/ # User management
│ ├── transactions/ # Transaction handling
│ ├── categories/ # Category management
│ └── budgets/ # Budget management
└── frontend/
├── app/
│ ├── (auth)/ # Login/Register
│ └── (dashboard)/ # Dashboard pages
└── lib/ # API client & hooks


</code>





## 🚀 Installation

### Prerequisites
- Python 3.8+
- Node.js 18+
- pip
- npm

### Backend Setup


git clone https://github.com/yourusername/finance-tracker.git
cd finance-tracker/backend

## Create virtual environment
```
python -m venv venv
```
## Activate (Windows)
```
venv\Scripts\activate
```

## Activate (Mac/Linux)
```
source venv/bin/activate
```

## Install dependencies
```
pip install -r requirements.txt
```

## Run migrations
```
python manage.py makemigrations
python manage.py migrate
```
## Create admin user
```
python manage.py createsuperuser
```

## Start server
```
python manage.py runserver
Frontend Setup
```
cd ../frontend

## Install dependencies
```
npm install
```
## Create .env.local
```
echo "NEXT_PUBLIC_API_URL=http://127.0.0.1:8000/api" > .env.local
```
## Start development server
```
npm run dev
```
Environment Variables
Create .env.local in frontend directory:

env
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000/api
## 📡 API Endpoints
Method	Endpoint	Description
<code>
POST	/api/auth/register/	Register user
POST	/api/auth/login/	Login user
GET	/api/auth/profile/	Get profile
GET	/api/transactions/	List transactions
POST	/api/transactions/	Create transaction
GET	/api/transactions/summary/	Get summary
GET	/api/categories/	List categories
GET	/api/budgets/	List budgets
</code>


## 📊 Database Schema
python
User:
- username, email, first_name, last_name
- phone, avatar, currency
- created_at, updated_at

Category:
- name, type (INCOME/EXPENSE)
- icon, color, user (FK)
- is_default, created_at

Transaction:
- user (FK), category (FK)
- amount, type (INCOME/EXPENSE)
- description, date
- payment_method
- created_at, updated_at

Budget:
- user (FK), category (FK)
- amount, period (MONTHLY/QUARTERLY/YEARLY)
- month, year, created_at
## 🔐 Authentication Flow
User registers with username, email, and password

User logs in and receives JWT tokens

Tokens stored in localStorage

All API requests include token in headers

Token auto-refresh on expiration

Logout clears tokens and redirects to login

## 🗓️ Roadmap
PostgreSQL integration

Dark/Light theme toggle

Email notifications

Export to PDF/CSV

Multi-currency support

Recurring transactions

Financial goals tracking

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

## 📄 License
This project is open source and available under the MIT License.

## 👨‍💻 Author

**Developed by:** [HamiParsa](https://github.com/HamiParsa)
💬 Full-Stack Developer | Building real-world projects with modern web technologies

---

<div align="center">
  <img src="https://skillicons.dev/icons?i=nextjs,typescript,tailwind,django,python,sqlite" />
  <br/>
  <p>Made with ❤️ and ☕</p>
  <p>⭐ Star this repo if you like it!</p>
</div>
