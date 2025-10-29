Step 1: Open Terminal in vs code and type
cd path/to/your/lab

Step 2: Create a Virtual Environment and type
python -m venv env
env\Scripts\activate

Step 3: Install Django and type
pip install django

Step 4: Create Django Project
Now create a project named myfirstproject and type
django-admin startproject myfirstproject

Step 5: Run Development Server
Go into the project folder so type
cd myfirstproject
run the server so type
python manage.py runserver

Step 6: Open Browser and visit:
http://127.0.0.1:8000/
we will see the Django default homepage that says:
“The install worked successfully! Congratulations!”
