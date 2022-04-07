# flask-celery

cd into the project directory and run the command "celery -A flaskapp.celery --pool=solo -l info in a bash terminal

Then, after setting the env variables FLASK_APP to "flaskapp" and FLASK_ENV to "development", run the command "flask run" in a new terminal

Go to localhost:5000 and ensure that the three background tasks adn received and execute according the delay and sleep times. 
