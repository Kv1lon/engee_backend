# Engee

A site for monitoring parameters of electrical systems of high-tech equipmen

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software:

- Python 3.x
- Django (specify version if necessary)
- Any other dependencies required

### Installing

A step-by-step series of examples that tell you how to get a development environment running:

1. Clone the repository:
```bash
git clone https://github.com/elaiviaien/engee.git
```

2. Navigate to the project directory:
```bash
cd engee_backend
```

3. Install the requirements:
```bash
pip install -r requirements.txt
```

4. Create and apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Run the development server:
```bash
python manage.py runserver
```
or just run the following command to start the server with docker:
```
docker compose up -d
```

Navigate to http://localhost:8000 in your web browser to view the application.

## Running the Tests

Explain how to run the automated tests for this system, if any.

## Deployment

Add additional notes about how to deploy this on a live system. You may specify instructions for platforms like Heroku, AWS, etc.

## Built With

- Django Rest Framework
- Django
- Docker
- PostgreSQL
- Nginx
- Gunicorn

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc.