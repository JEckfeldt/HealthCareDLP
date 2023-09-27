# HealthCareDLP
WSU Capstone Senior Project

# Setup
Download source code and open up a terminal
Setup an environment for the project
    1. "py -m venv project-name" will create a folder project name with environment info
    (myvenv or venv suggested they are already in the git ignore)
    2. Activate the environment go to project-name/Scripts and run activate or activate.bat
    3. You should see (project-name) on the far left of your terminal
    4. Make sure you run activate every time you open a new terminal to work inside your env 
    (You can run into version control issues if not)
Install the python reqs
    1. Make sure you are in the same dir as requirements.txt
    2. Run "pip install -r requirements.txt"
    3. This gives you all the packages used for the project (Just Django for now)

# Django Server
To run the Django Server on localhost:8000 by default
    1. Make sure you're in the same directory as manage.py (HealthCareForm)
    2. Run "python manage.py runserver"
    3. Ctrl-C in terminal will quit the server

# Description
A Django health care patient app that focuses on encryption and access control management as Data Loss Prevention methods.

# Scenario
A doctor would input patient information, other users (other doctor, developer, analyst) would only be able to see necessary information.
