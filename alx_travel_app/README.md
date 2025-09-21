
markdown
# ALX Travel App

A comprehensive Django-based travel booking platform that allows users to discover, book, and review properties worldwide.

## Features

- **Property Listings**: Detailed listings with amenities, pricing, and availability
- **Booking System**: Complete reservation management with status tracking
- **Review System**: User ratings and comments for properties
- **RESTful API**: Full API endpoints for all models using Django REST Framework
- **Admin Panel**: Django admin interface for managing data
- **Database Seeding**: Automated population of sample data for development
- **API Documentation**: Integrated Swagger/OpenAPI documentation

## Project Structure
alx_travel_app/
├── alx_travel_app/ # Django project settings
├── listings/ # Main application
│ ├── models.py # Database models
│ ├── serializers.py # API serializers
│ ├── admin.py # Admin panel configuration
│ ├── management/
│ │ └── commands/
│ │ └── seed.py # Database seeding command
│ └── ...
├── requirements.txt # Python dependencies
└── .env # Environment variables

text

## Data Models

### Listing
- Property details (title, description, address, type)
- Pricing and capacity information
- Amenities and availability status
- Owner relationship

### Booking
- Reservation details (dates, guests, price)
- Status management (pending, confirmed, cancelled, completed)
- Guest and listing relationships

### Review
- Rating system (1-5 stars)
- User comments
- Unique constraint per user per listing

## Installation

### Prerequisites
- Python 3.8+
- MySQL 5.7+
- pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd alx_travel_app
Create and activate virtual environment

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
pip install -r requirements.txt
Configure environment variables
Create a .env file in the project root:

bash
# Database configuration
DB_NAME=alx_travel_db
DB_USER=alx_travel_user
DB_PASSWORD=your_secure_password
DB_HOST=localhost
DB_PORT=3306

# Django configuration
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
Setup MySQL database

sql
CREATE DATABASE alx_travel_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'alx_travel_user'@'localhost' IDENTIFIED BY 'your_secure_password';
GRANT ALL PRIVILEGES ON alx_travel_db.* TO 'alx_travel_user'@'localhost';
FLUSH PRIVILEGES;
Run migrations

bash
python manage.py makemigrations
python manage.py migrate
Create superuser

bash
python manage.py createsuperuser
Seed the database (optional)

bash
python manage.py seed
Run development server

bash
python manage.py runserver
Usage
Access Points
Admin Panel: http://localhost:8000/admin/

API Documentation: http://localhost:8000/swagger/

ReDoc Documentation: http://localhost:8000/redoc/

API Overview: http://localhost:8000/api/

Database Seeding
Populate the database with sample data for development and testing:

bash
# Basic seeding (default quantities)
python manage.py seed

# Customized seeding
python manage.py seed --users 5 --listings 10 --bookings 20 --reviews 15
Options:

--users: Number of users to create (default: 10)

--listings: Number of listings to create (default: 20)

--bookings: Number of bookings to create (default: 50)

--reviews: Number of reviews to create (default: 30)

API Endpoints
GET/POST /api/listings/ - List and create properties

GET/PUT/DELETE /api/listings/{id}/ - Retrieve, update, or delete specific listing

GET/POST /api/bookings/ - List and create bookings

GET/POST /api/reviews/ - List and create reviews

Development
Technology Stack
Backend: Django 4.2.7, Django REST Framework

Database: MySQL with mysqlclient connector

API Documentation: drf-yasg (Swagger/OpenAPI)

Data Generation: Faker library for seeding

Environment Management: python-dotenv

Key Dependencies
django==4.2.7

djangorestframework==3.14.0

django-cors-headers==4.3.1

drf-yasg==1.21.7

mysqlclient==2.2.0

django-environ==0.11.2

Faker==19.6.2

Common Commands
bash
# Run tests
python manage.py test

# Check code quality
python manage.py check

# Create new migration files
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Start development server
python manage.py runserver
API Examples
Create a Listing
bash
curl -X POST http://localhost:8000/api/listings/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Beachfront Villa",
    "description": "Beautiful villa with ocean view",
    "address": "123 Beach Road",
    "city": "Miami",
    "country": "USA",
    "property_type": "villa",
    "price_per_night": "250.00",
    "max_guests": 6,
    "num_bedrooms": 3,
    "num_beds": 4,
    "num_bathrooms": 2,
    "amenities": "Pool, WiFi, Kitchen, Parking"
  }'
Get All Listings
bash
curl http://localhost:8000/api/listings/
Troubleshooting
Common Issues
MySQL Connection Errors

Verify MySQL service is running

Check database credentials in .env file

Ensure user has proper privileges

Migration Errors

Delete migration files and database, then recreate

Run python manage.py makemigrations and migrate

Environment Variables Not Loading

Ensure .env file is in project root

Check file permissions

Verify variable names match settings.py

Getting Help
If you encounter issues:

Check the Django error logs in the terminal

Verify all installation steps were completed

Ensure all dependencies are installed correctly

License
This project is part of the ALX Software Engineering program.

Contributing
This is a learning project for the ALX program. Contributions are welcome through issues and pull requests.

Support
For support related to this project, please check the ALX program resources or contact your program mentors.

Happy coding!