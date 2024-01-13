# Project Title: Django CRUD Application with PostgreSQL and Poetry

Author : Christian Q. Cleofas - Junior Backend Developer (Python)

# Overview:

This project is a simple CRUD (Create, Read, Update, Delete) application built using the Django web framework. It utilizes PostgreSQL as the database for data storage and Poetry for package management.

Features:

- Create: Users can add new records to the database.
- Read: Retrieve and display records from the database.
- Update: Modify existing records in the database.
- Delete: Remove records from the database.

Technologies Used:

- Django: A high-level Python web framework for rapid development.
- PostgreSQL: A powerful open-source relational database management system.
- Poetry: A dependency manager for Python projects that simplifies package management.

Setup Instructions:

1. Clone the repository:

   git clone https://github.com/your-username/your-repo.git](https://github.com/chrstncleofas/django-postgresql-2024.git)

2. Install project dependencies using Poetry:

   poetry install

3. Apply database migrations:

   poetry run python manage.py migrate

4. Run the development server:

   poetry run python manage.py runserver

5. Access the application at http://localhost:8000

Project Structure:

- /your-app: Django app containing your CRUD functionality.
- /your-project: Django project settings and configuration.
- /poetry.lock and pyproject.toml: Poetry configuration files for dependency management.
- /requirements.txt: Auto-generated requirements file by Poetry.

Contribution Guidelines:

If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure tests pass.
4. Create a pull request, detailing the changes made and the reason for the changes.

Acknowledgements:

Give credit to any third-party libraries, frameworks, or tools used in your project.

License:

This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to customize this README according to your specific project details and preferences. Good luck with your Django CRUD application!
