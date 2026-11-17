Job Alert System

A Django-based job aggregation and alert platform that collects job
postings from supported company career sites, stores them in a database,
and helps users find jobs that match their preferences.

Features
- Job collection: Scrapes job postings from configured company
  career sites using platform-specific scrapers.
- Duplicate handling: Generates a SHA-256 hash from the company
  name, job title, and application URL to identify existing postings.
- Job search: Filters active jobs by search term, location, work
  mode, and employment type.
- User accounts: Supports registration and login through the
  project's user API.
- Job alerts: Authenticated users can create and view alerts based
  on keywords, location, work mode, and employment type.
- Matching jobs: Users can request jobs matching a particular
  alert.
- Notifications: Creates in-app notifications for newly discovered
  jobs that match active alerts.
- Email alerts: Attempts to email the user when a newly discovered
  job matches an active alert.
- Read/unread status: Users can view unread notifications and mark
  notifications as read.
- Safe handling of empty scrape results: The scraper skips
  deactivation when a company returns no jobs, helping prevent
  accidental deactivation caused by an empty result.

Current behavior: Notifications and emails are triggered for newly
created database records that match active alerts. Creating an alert
does not automatically send notifications for matching jobs that are
already in the database. Email delivery depends on valid SMTP
configuration. Scraping must be run manually or configured with a
scheduler.

Technology Stack
- Python
- Django
- Django REST Framework
- MySQL
- requests and platform-specific scraping logic
- SMTP email configuration
- Postman for API testing

Project Structure
The repository is organized into Django apps and supporting packages.
Names may vary slightly as the project evolves.
job_alert_system/
├── companies/       # Company records and career-site configuration
├── dashboard/       # Dashboard-related code
├── jobs/            # Job model, APIs, and job services
├── alerts/          # Job alert model, endpoints, and matching logic
├── notifications/   # In-app notification model and endpoints
├── users/           # User registration and login
├── scraper/         # Scraper base class, factory, orchestrator, platform scrapers
├── scheduler/       # Scheduling-related code, if configured
├── config/          # Django settings and URL configuration
├── manage.py
└── requirements.txt

Getting Started
1. Clone the repository
git clone https://github.com/SarojPanwar/job_alert_system.git
cd job_alert_system
2. Create and activate a virtual environment
Linux/macOS:
python3 -m venv venv
source venv/bin/activate
Windows PowerShell:
python -m venv venv
venv\Scripts\Activate.ps1
3. Install dependencies
pip install -r requirements.txt
4. Configure environment variables
Create a .env file in the project root. Use the variable names
expected by your config/settings.py.

Example:
SECRET_KEY=replace_with_a_secure_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=127.0.0.1
DB_PORT=3306

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_app_password
DEFAULT_FROM_EMAIL=your_email@example.com

Important: The exact database and email variable names must match
the names read by your settings file. Update this example if your
project uses different names. Never commit .env, database credentials,
email app passwords, or production secrets to GitHub.
5. Prepare the database
Create the MySQL database and user, then run:
python manage.py migrate
Create an administrator account if needed:
python manage.py createsuperuser
6. Start the development server
python manage.py runserver
The default development address is http://127.0.0.1:8000/. If your
project uses another port, use that port instead.
7. Run job scraping
Run the management command manually:
python manage.py scrape_jobs
This command processes active company records using the configured
scrapers. For automatic production scraping, configure a scheduler (for
example, a Render Cron Job) to run this command on a schedule. Deploying
the Django web service alone does not automatically schedule scraping.
API Overview
The following routes reflect the endpoints tested during development.
Confirm config/urls.py and each app's urls.py for the exact route
configuration.

Base URL for local testing: http://127.0.0.1:9000

  Method                  Endpoint                                       Purpose
  POST                  /api/users/register/                         Register a user

  POST                  /api/users/login/                            Log in and obtain an
                                                                         authentication token

  GET                   /api/jobs/                                   List/search jobs

  GET                   /api/alerts/                                 List alerts belonging
                                                                         to the authenticated
                                                                         user

  POST                  /api/alerts/                                 Create a job alert

  GET                   /api/alerts/<alert_id>/jobs/                 Get jobs matching an
                                                                         alert

  DELETE                /api/alerts/<alert_id>/delete/                      Delete an alert

  GET                   /api/notifications/                          List notifications for
                                                                         the authenticated user

  GET                   /api/notifications/unread/                   List unread
                                                                         notifications

  PATCH                 /api/notifications/<notification_id>/read/   Mark a notification as
                                                                     read
Authentication in Postman
For protected endpoints, log in and copy the returned DRF token. Set
this header:
Authorization: Token YOUR_TOKEN
Use the token for the account whose alerts or notifications you want to
access. Each account sees its own user-specific alerts and
notifications.
How the Job Alert Flow Works
1. Company records identify active career sites and the scraper
   platform to use.
2. The scraper command fetches job postings from each configured
   company.
3. The job service computes a hash and creates or updates each job
   record.
4. If a job is newly created in the database, the alert service checks
   active alerts against its keywords, location, work mode, and
   employment type.
5. If an alert matches, the application creates an in-app notification
   and attempts to send an email.
6. Existing jobs can be queried through an alert's matching-jobs
   endpoint, but creating an alert does not automatically notify the
   user about jobs already stored in the database.
7. Jobs missing from a successful, non-empty scrape can be deactivated.
   If a scraper returns no jobs, deactivation is skipped for that
   company to avoid treating a failed/empty scrape as proof that all
   jobs disappeared.

New record vs. newly posted job: The current implementation treats a
job as new when its hash is not already in the database. A previously
posted job that the system has never stored can therefore trigger a
notification when first discovered.


