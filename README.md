# HealthCareDLP
WSU Capstone Senior Project

## Setup
Download source code and open up a terminal
Setup an environment for the project <br>
    1. "py -m venv project-name" will create a folder project name with environment info
    (myvenv or venv suggested they are already in the git ignore)  <br>
    2. Activate the environment go to project-name/Scripts and run activate or activate.bat  <br>
    3. You should see (project-name) on the far left of your terminal  <br>
    4. Make sure you run activate every time you open a new terminal to work inside your env 
    (You can run into version control issues if not)   <br> <br>
Install the python reqs<br>
    1. Make sure you are in the same dir as requirements.txt<br>
    2. Run "pip install -r requirements.txt"<br>
    3. This gives you all the packages used for the project (Just Django for now)<br>
## Django Server
To run the Django Server on localhost:8000 by default <br>
    1. Make sure you're in the same directory as manage.py (HealthCareForm) <br>
    2. Run "python manage.py runserver" <br>
    3. Ctrl-C in terminal will quit the server  <br>

## Description
A Django health care patient app that focuses on encryption and access control management as Data Loss Prevention methods. <br>

## Scenario
A doctor would input patient information, other users (other doctor, developer, analyst) would only be able to see necessary information. <br>
