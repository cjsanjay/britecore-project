# britecore-project
A web app for registering and checking already resgistered feature requests in the system.

Setup: Tech stack Python/Django

Step1: Clone the github repository on your machine
    >git clone https://github.com/cjsanjay/britecore-project.git
 
Step 2: Create a virtual environment so that it wont affect the other applications
    >cd britecore-project
    >virtualenv --python=python3.4 myvenv
    >source myvenv/bin/activate
    >pip install django==1.9 
      (If pip is not install in your machine then installit using sudo apt-get install pip)

Step3: Create database in your machine
    >python manage.py migrate

Step4: Run the server
    >python manage.py runserver

step 5:  go to address http://127.0.0.1:8000/

               
 
