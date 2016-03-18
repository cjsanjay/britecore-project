# britecore-project
Setup: Tech stack Python/Django

Step1: Clone the github repository on your machine
    1. git clone https://github.com/cjsanjay/britecore-project.git
 
Step 2: Create a virtual environment so that it wont affect the other applications
    1. cd britecore-project
    2. virtualenv --python=python3.4 myvenv
    3. source myvenv/bin/activate
    4. pip install django==1.9 
      (If pip is not install in your machine then installit using sudo apt-get install pip)

Step3: Create database in your machine
    1. python manage.py migrate

Step4: Run the server
    1. python manage.py runserver

step 5:  go to address http://127.0.0.1:8000/

               
 
