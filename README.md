
A comprehensive LEARNING MANAGEMENT SYSTEM with role-based access control, course management, student tracking, and sponsorship features.

ROLES:
	•	Admin: Oversee platform operations.
	•	Instructor: Manage courses and assessments.
	•	Student: Enroll in courses and complete assessments.
	•	Sponsor: Fund students and track their progress.
________________________________________________________________________________________________________________________________________________

✅ Features Included
	1.	CRUD (Create, Read, Update, Delete):
	•	Make CRUD operations based on database design.

	2.	Data Filtering and Searching:
	•	Students can search for courses by name, instructor, or difficulty level.
	•	Sponsors can filter students by status or progress.
	3.	Data Pagination:
	•	Paginate course lists, student records, and sponsorship details.
	4.	Authentication:
	•	Role-based authentication using Django Groups.
	5.	Analytics:
	•	Admin Dashboard: Display metrics like total users, active courses, and student enrollments.
	•	Sponsor Dashboard: Show sponsorship impact, student progress, and fund utilization.
	6.	Emailing (using Mailtrap):
	•	Notify students about course deadlines and assessment results.
	•	Notify sponsors about progress reports.
	7.	Notification:
	•	Alerts for instructors on course completion rates and student engagement.
	•	Notifications for students about new assignments and due dates.
	8.	Deployed (Optional):
	•	Host the application on a free source (e.g., Heroku, Render).
	9.	Testing and Documentation:
	•	Provide detailed API tests.
	•	Include user and developer documentation.

___________________________________________________________________________________________________________________________________________________________
## TECHNOLOGY STACK

### BACKEND
- Python 3.10
- Django 4.2
- Django REST Framework
- Mailtrap (For Emailing and Notification)
  

### Frontend
- *Bootstrap 5*
- *HTML5/CSS3
- *JavaScript
  ________________________________________________________________________________________________________________________________________________________

## INSTALLATION

### Prerequisites
- Python 3.10+
- PostgreSQL
_________________________________________________________________________________________________________________________________________________________

### SETUP INSTRUCTIONS

1. *Create virtual environment*:
   bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   

3. *Install dependencies*:
   bash
   pip install -r requirements.txt
   

4. *Configure environment variables*:
   Create .env file with:
   env
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   DATABASE_URL=postgres://user:password@localhost:5432/lmsdb
   EMAIL_HOST=your_smtp_host
   EMAIL_PORT=587
   EMAIL_HOST_USER=your_email
   EMAIL_HOST_PASSWORD=your_password
   

5. *Run migrations*:
   bash
   python manage.py migrate
   

6. *Create superuser*:
   bash
   python manage.py createsuperuser
   

7. *Run development server*:
   bash
   python manage.py runserver
