🧑‍💼 Customer Relationship Management (CRM)
A sleek and responsive Customer Relationship Management (CRM) web application built with Django and Bootstrap. Manage your customer records effortlessly with an intuitive interface and robust functionality.

### ✨ Features
Authentication: Users can securely register, log in, and log out.

CRUD Operations: Add, view, update, and delete customer records seamlessly.

Responsive Design: Fully optimized for all devices using Bootstrap 5.

Customer Records: Manage detailed records including:

Name.

Email.

Phone Number.

Address.

City, State, and ZipCode.

Creation Date.

Interactive Tooltips: Hover-friendly tooltips for improved navigation.

### 🛠️ Technologies Used
Technology	          Purpose

Django	              Backend Framework

SQLite (default)	    Database (can be switched to MySQL/PostgreSQL)

HTML, CSS, Bootstrap	Frontend Design and Styling

Django Auth System	  User Authentication


### 🚀 Setup Instructions
## Prerequisites
Python 3.x installed on your system.

Django 3.x or later.

Bootstrap 5 included via CDN or locally.

### Installation Steps
## Clone the Repository

git clone https://github.com/your-username/crm-project.git
cd crm-project

## Create and Activate Virtual Environment (optional)

python -m venv venv
source venv/bin/activate   # For Windows: venv\Scripts\activate

## Install Dependencies

pip install -r requirements.txt

## Apply Database Migrations

python manage.py migrate

## Create a Superuser

python manage.py createsuperuser

## Run the Development Server

python manage.py runserver

## Visit Your App
Open http://127.0.0.1:8000/ in your browser.


### 📋 Authentication
Login: Users must log in to view or manage records.

Registration: A user can create a new account by providing basic details.

### 🖼️ Views & Templates

##Dynamic Pages
# Home:

A list of customer records is displayed in a responsive table.

"View", "Edit", and "Delete" actions are provided for each record.

# Add Record:

User-friendly form to add new records.

# Update Record:

Edit customer details with pre-filled form values.

# View Record:

Displays customer details with actionable links.

# Login/Register:

Secure and responsive authentication pages.

### 🖌️ Static Files

## CSS: Uses Bootstrap 5 for design consistency.

## JavaScript: Added interactivity via Bootstrap JS components.

## Custom Assets: Place your CSS/JS/images in the static/ directory.


## Database Errors:

Ensure migrations are applied:

python manage.py migrate

### 📚 Next Steps

## Add Search & Filter functionality for customer records.

##Implement User Roles (e.g., Admin, Manager).

## Deploy the application to a cloud platform like Heroku or AWS.

## Expand database support to MySQL or PostgreSQL.

### 🎉 Conclusion
This CRM app is perfect for learning Django's core functionalities while building a practical tool. Feel free to fork and customize the project to suit your needs!
