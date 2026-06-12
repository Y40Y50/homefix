# HomeFix

HomeFix is a property maintenance management platform built with Django. 
The system allows property owners to manage their properties, contractors, and maintenance jobs in one place.

Users can create accounts, register properties, add contractors, and track maintenance jobs from creation through completion. The platform provides an organised way to manage maintenance tasks while keeping all records securely stored in a relational database.

The project was developed using HTML, CSS, Bootstrap, Python, Django, and SQLite, following full CRUD functionality and responsive web design principles.

# Live Website

Deployed Application:
https://homefix-yahya-6300fce8c888.herokuapp.com/

GitHub Repository:
https://github.com/Y40Y50/homefix


# User Stories

## As a Property Owner

* I want to create an account so that I can access the HomeFix platform.
* I want to register my properties so that I can keep maintenance records organised.
* I want to add contractors so that I can assign work to them.
* I want to create maintenance jobs so that repairs and improvements can be tracked.
* I want to update job statuses so that I know which jobs are pending, in progress, or completed.
* I want to edit and delete records so that information remains accurate and up to date.

## As a Contractor

* I want to view maintenance jobs assigned to me so that I can manage my workload.
* I want maintenance information to be clearly organised so that I can understand job requirements.
* I want to see property details related to a job so that I can complete work efficiently.

## As the Site Owner

* I want users to manage their maintenance records through a secure online platform.
* I want the system to store data in a relational database so that information is organised and reliable.
* I want the website to be responsive so that users can access it on desktop, tablet, and mobile devices.

# Features

## User Authentication

* User registration system.
* User login and logout functionality.
* Secure user authentication using Django's built-in authentication system.

## Property Management

Users can:

* Create properties.
* View a list of properties.
* Edit property information.
* Delete properties.

Each property stores:

* Property name.
* Address.
* Property type.
* Creation date.

## Contractor Management

Users can:

* Add contractors.
* View contractor details.
* Edit contractor information.
* Delete contractors.

Each contractor stores:

* Name.
* Trade type.
* Phone number.
* Email address.

## Maintenance Job Management

Users can:

* Create maintenance jobs.
* View maintenance jobs.
* Edit maintenance jobs.
* Delete maintenance jobs.

Each job stores:

* Job title.
* Description.
* Property.
* Contractor.
* Priority level.
* Status.
* Creation date.

## Home Page

The home page includes:

* Welcome section.
* Exclusive offers section.
* Service categories.
* Most requested services.
* Promotional services video.
* Contact information.
* Social media links.

## Responsive Design

The website is fully responsive and supports:

* Desktop devices.
* Tablet devices.
* Mobile devices.

## Navigation

A responsive navigation menu allows users to quickly access:

* Home
* Properties
* Contractors
* Jobs
* Create Job
* Login/Register
* Logout

# Database Schema

The HomeFix application uses a relational database consisting of four main entities:

- User
- Property
- Contractor
- MaintenanceJob

## Entity Relationship Diagram (ERD)

![ERD](README-assets/erd.png)

### Entity Relationships

- One User can have many Properties.
- One User can have many Contractors.
- One User can have many Maintenance Jobs.
- One Property can be linked to many Maintenance Jobs.
- One Contractor can be linked to many Maintenance Jobs.



## User

The User model is provided by Django's authentication system and stores user account information.

### Property

| Field         | Type               |
| ------------- | ------------------ |
| id            | Primary Key        |
| user          | Foreign Key (User) |
| name          | CharField          |
| address       | TextField          |
| property_type | CharField          |
| created_at    | DateTimeField      |

### Contractor

| Field      | Type               |
| ---------- | ------------------ |
| id         | Primary Key        |
| user       | Foreign Key (User) |
| name       | CharField          |
| trade_type | CharField          |
| phone      | CharField          |
| email      | EmailField         |

### MaintenanceJob

| Field       | Type                     |
| ----------- | ------------------------ |
| id          | Primary Key              |
| user        | Foreign Key (User)       |
| property    | Foreign Key (Property)   |
| contractor  | Foreign Key (Contractor) |
| title       | CharField                |
| description | TextField                |
| priority    | CharField                |
| status      | CharField                |
| created_at  | DateTimeField            |

## Entity Relationship Diagram (ERD)

User (1)
│
├── Property (Many)
├── Contractor (Many)
└── MaintenanceJob (Many)

Property (1) ──────< MaintenanceJob (Many)
Contractor (1) ───< MaintenanceJob (Many)
A user can own multiple properties, contractors and maintenance jobs.

Each maintenance job belongs to one property and one contractor.

This design ensures that users can only access and manage their own data while maintaining relationships between properties, contractors and maintenance jobs.


# Technologies Used

## Programming Languages

* Python
* HTML5
* CSS3

## Frameworks

* Django
* Bootstrap 5

## Database

* SQLite (Development Database)

## Tools and Software

* Visual Studio Code
* Git
* GitHub
* Heroku
* Google Chrome Developer Tools

## Libraries

* Django Authentication System
* Font Awesome Icons


# Installation

1. Clone the repository

git clone https://github.com/Y40Y50/homefix.git

2. Navigate to the project folder

cd homefix

3. Create a virtual environment

python -m venv .venv

4. Activate the virtual environment

Windows:
.venv\Scripts\activate

5. Install dependencies

pip install -r requirements.txt

6. Run migrations

python manage.py migrate

7. Start the development server

python manage.py runserver


# Deployment

## Heroku Deployment

The application was deployed using Heroku.

### Deployment Steps

1. Create a Heroku application.
2. Connect the GitHub repository.
3. Configure environment variables.
4. Deploy the main branch.
5. Run database migrations.
6. Open the deployed application.


# Deployment Testing

The deployed Heroku application was tested against the local development version to ensure that all functionality worked correctly after deployment.

| Feature | Local Version | Live Version | Result |
|----------|--------------|--------------|---------|
| Homepage loads | Pass | Pass | Pass |
| User Registration | Pass | Pass | Pass |
| User Login | Pass | Pass | Pass |
| Create Property | Pass | Pass | Pass |
| Edit Property | Pass | Pass | Pass |
| Delete Property | Pass | Pass | Pass |
| Create Contractor | Pass | Pass | Pass |
| Create Maintenance Job | Pass | Pass | Pass |
| Search Jobs | Pass | Pass | Pass |
| Filter Jobs | Pass | Pass | Pass |
| Responsive Design | Pass | Pass | Pass |

The deployed application behaved consistently with the local development version.

## Deployment Verification Screenshots

### Live HomeFix Application

![Live Site](README-assets/live-site.png)

### Django Admin Panel

![Admin Panel](README-assets/admin-panel.png)

### Heroku Dashboard

![Heroku Dashboard](README-assets/heroku-dashboard.png)

## Form Validation Testing

| Test | Input | Expected Result | Result |
|--------|--------|--------|--------|
| Property name left blank | Empty field | Form validation message displayed | Pass |
| Contractor email invalid | test@test | Validation error displayed | Pass |
| Required fields empty | Empty submission | User prevented from submitting form | Pass |
| Login invalid credentials | Wrong username/password | Error message displayed | Pass |


# Security Features

The HomeFix application implements several security features to protect user data.

## Authentication

* Users must register an account before accessing protected features.
* Django's built-in authentication system is used for login and logout functionality.

## User Data Protection

* Properties, contractors and maintenance jobs are linked to the logged-in user.
* Users can only view, edit and delete their own records.
* Access to other users' records is restricted.

## Environment Variables

* Secret keys are stored securely and are not committed to the GitHub repository.
* Sensitive configuration data is protected using environment variables.

## Production Security

* DEBUG mode is disabled in the deployed production version.
* User data is stored securely within the database.


# Screenshots

## Home Page (Guest User)

![Home Page Guest](README-assets/home_without_login.png)

## Home Page (Logged In User)

![Home Page Logged In](README-assets/home_with_login.png)

## User Registration

![Register](README-assets/register.png)

## Dashboard

![Dashboard](README-assets/dashboard.png)

## Properties Management

![Properties](README-assets/properties.png)

## Add Property

![Add Property](README-assets/add_property.png)

## Contractors Management

![Contractors](README-assets/contractors.png)

## Add Contractor

![Add Contractor](README-assets/create_contractor.png)

## Maintenance Jobs

![Maintenance Jobs](README-assets/maintenance_jobs.png)

## Create Maintenance Job

![Create Maintenance Job](README-assets/create_maintenance_job.png)

## Search Maintenance Jobs

![Search Jobs](README-assets/search_maintenance_jobs.png)

## Filter Maintenance Jobs

![Filter Jobs](README-assets/fillter_maintenance_jobs.png)

## Pagination

![Pagination](README-assets/next_page_maintenance_jobs.png)

## Mobile Responsive Design

![Mobile View](README-assets/mobile_view.png)

## Tablet Responsive Design

![Tablet View](README-assets/tablet_view.png)


# Credits

## Media

Images used within the project were sourced from royalty-free image websites for educational purposes.

## Icons

Font Awesome icons were used throughout the website.

## Frameworks

Bootstrap 5 was used for responsive design and layout components.


# Wireframes

The following wireframes were created during the planning stage of the project to define the structure, layout and user journey before development began.

## Home Page Wireframe

The homepage wireframe was designed to showcase the main services offered by HomeFix, highlight featured maintenance categories and provide clear navigation for users.

![Home Page Wireframe](README-assets/homepage-wireframe-desktop.png)

---

## Login Page Wireframe

The login page wireframe was designed to provide users with a simple and secure way to access their accounts.

![Login Page Wireframe](README-assets/login-wireframe.png)

---

## Dashboard Wireframe

The dashboard wireframe was created to provide users with an overview of their properties, contractors and maintenance jobs from a central location.

![Dashboard Wireframe](README-assets/dashboard-wireframe.png)

---

## Create Maintenance Job Wireframe

The maintenance job creation wireframe was designed to allow users to quickly create and manage maintenance requests.

![Create Maintenance Job Wireframe](README-assets/create-maintenance-job-wireframe.png)

---

## Final Implemented Screens

The following screenshots show how the completed application compares with the original wireframes.

### Login Page

![Login Page](README-assets/login-page.png)

### User Registration

![Register Page](README-assets/register-page.png)

### Add Property

![Add Property](README-assets/add-property-page.png)

### Add Contractor

![Add Contractor](README-assets/add-contractor-page.png)

### Create Maintenance Job

![Create Maintenance Job](README-assets/create-maintenance-job-page.png)

### Django Admin Panel

![Admin Panel](README-assets/admin-panel.png)

# Bugs

## Fixed Bugs

* Book Now buttons originally redirected unauthenticated users to the registration page. This was updated to improve the user journey.
* HTML validation errors caused by missing alt attributes were resolved.
* Heading hierarchy issues identified during validation were corrected.
* Python PEP8 formatting issues were fixed following validation testing.

### Login Error

Issue:
Entering invalid login credentials caused a Server Error (500).

Fix:
The login view was updated to handle invalid authentication attempts and display an appropriate error message to the user.

Result:
Users now receive a validation message instead of a server error.

## Bug Fixes and Validation Testing

### Contractor Phone Number Validation

During testing, it was discovered that the Contractor form accepted text values in the phone number field. This allowed invalid data such as "test" or "adafd" to be entered and saved.

To resolve this issue, phone number validation was added to the Contractor form. The system now checks the input and prevents non-numeric phone numbers from being submitted.

**Test Performed**

| Test Case | Input | Expected Result | Actual Result | Status |
|------------|--------|----------------|--------------|--------|
| Valid phone number | 07812345678 | Form submits successfully | Form submitted successfully | Pass |
| Invalid phone number | adafd | Validation error displayed | "Enter a valid phone number" displayed | Pass |

**Result**

The validation now prevents invalid phone numbers from being stored in the database, improving data quality and user input validation.

### Evidence

The screenshot below shows the validation message displayed when invalid text is entered into the phone number field.

![Contractor Phone Validation](README-assets/valid-phon-mumber.png)

## Known Bugs

* No known bugs at the time of submission.

# Future Improvements

The following features could be added in future versions of HomeFix:

* Email notifications for maintenance job updates.
* Contractor user accounts with dedicated dashboards.
* File and image uploads for maintenance jobs.
* Advanced reporting and analytics.
* Calendar scheduling for maintenance work.
* Search and filtering for properties and contractors.
* Job assignment notifications.
* Integration with external mapping services.
* Live chat support between property owners and contractors.



### Entity Relationships

- One User can have many Properties.
- One User can have many Contractors.
- One User can have many Maintenance Jobs.
- One Property can be linked to many Maintenance Jobs.
- One Contractor can be linked to many Maintenance Jobs.

# Testing

| Test ID | Feature | Test Description | Expected Result | Result |
|----------|----------|------------------|----------------|---------|
| T01 | User Registration | Create a new user account | User account created successfully | Pass |
| T02 | User Login | Login with valid credentials | User redirected to dashboard | Pass |
| T03 | Add Property | Create a new property record | Property saved in database | Pass |
| T04 | View Properties | Display all user properties | Properties displayed correctly | Pass |
| T05 | Add Contractor | Create a new contractor record | Contractor saved in database | Pass |
| T06 | View Contractors | Display all contractors | Contractors displayed correctly | Pass |
| T07 | Create Maintenance Job | Create a maintenance job | Job saved successfully | Pass |
| T08 | Edit Maintenance Job | Update job information | Changes saved successfully | Pass |
| T09 | Delete Maintenance Job | Delete an existing job | Job removed successfully | Pass |
| T10 | Search Jobs | Search by job title | Matching jobs displayed | Pass |
| T11 | Filter Jobs | Filter by status | Correct jobs displayed | Pass |
| T12 | Pagination | Navigate between pages | Correct page displayed | Pass |
| T13 | Mobile Responsive Design | Open website on mobile screen | Layout adapts correctly | Pass |
| T14 | Tablet Responsive Design | Open website on tablet screen | Layout adapts correctly | Pass |
| T15 | Navigation Menu | Navigate between pages | Correct page loads | Pass |


# Validation

## HTML Validation

The HTML for the HomeFix project was validated using the W3C Nu HTML Checker.

During development, validation errors were identified, including missing image alt attributes and heading hierarchy issues. These problems were corrected before final submission.

The final validation check returned no errors or warnings.

**Evidence:**

![HTML Validation Results](README-assets/html_validator.png)

---

## CSS Validation

The project's custom CSS stylesheet was validated using the W3C CSS Validation Service.

The validator reported no errors, confirming that the stylesheet complies with current CSS standards.

**Evidence:**

![CSS Validation Results](README-assets/css_validator.png)

---

## Python (PEP8) Validation

Python files were validated using the Code Institute CI Python Linter.

Several issues were initially identified, including:

* Line length violations
* Trailing whitespace
* Missing blank lines
* Indentation inconsistencies

After correcting these issues, all tested Python files passed validation with no errors.

### Models.py

**Evidence:**

![Models.py Validation](README-assets/models_py_validator.png)

### Views.py

**Evidence:**

![Views.py Validation](README-assets/views_py_validator.png)

---

## Django System Check

Django's built-in system check framework was used throughout development to verify the project's configuration.

Running the application returned:

```bash
python manage.py runserver
```

Result:

```text
System check identified no issues (0 silenced).
```

This confirms that the project's models, URLs, settings and installed applications were configured correctly.

---

## Validation Summary

All HTML, CSS and Python code was successfully validated. Any issues identified during testing were resolved before project completion. The validation evidence provided above demonstrates compliance with web standards and PEP8 coding guidelines.

# Lighthouse Testing

Google Lighthouse was used to evaluate the performance, accessibility, SEO and best practices of the HomeFix application.

Testing was performed using Chrome Developer Tools on the Home Page in tablet view.

## Results

| Category       | Score |
| -------------- | ----- |
| Performance    | 87    |
| Accessibility  | 92    |
| Best Practices | 100   |
| SEO            | 90    |

The results indicate that the application performs well across key web quality metrics, with particularly strong scores in Best Practices, Accessibility and SEO.

### Lighthouse Report

![Lighthouse Report](README-assets/lighthouse_report.png)


