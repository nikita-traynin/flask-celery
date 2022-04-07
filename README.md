# flask-celery
This is a barebones POC for using celery in a flask app. This mainly follows along the celery docs as well as [this older guide](https://blog.miguelgrinberg.com/post/using-celery-with-flask) specific to flask and celery. 

The goal of this project is to prepare for incorporating celery into my Style-Transfer project in order to assign the ML tasks to EC2 worker instances. Eventually that project will be split into the worker and front end repos, since they will be deployed in different environments.
## Step to Run
 - clone this project and run `git pull` to get latest changes
 - cd into the project directory and run the command `celery -A flaskapp.celery --pool=solo -l info` in a bash terminal
 - Run `export FLASK_APP=flaskapp` and `export FLASK_ENV=development`
 - Run the command "flask run" in a new terminal
 - Go to localhost:5000 and ensure that the three background tasks adn received and execute according the delay and sleep times. 
