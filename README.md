# Flask Fitness Tracker

## About


## Set up
__initial set up__
* Create directory: `mkdir flask_fitness_tracker`
* Go into the directory: `cd flask_fitness_tracker`
* Set up virtual environment: `python -m venv .env`
* Activate the virtual environment: `.env/bin/activate`
* `pip3 install flask`
* `touch .gitignore`

__initialise the app__
`mkdir app`
`touch app/__init__.py`
`touch app/routes.py`
`touch runner.py`

__Set up environment variable so that it is remembered across sessions__
* `pip3 install python-dotenv`
* `touch .flaskenv`   

__Create your models__
* `touch app/models.py`

__Implement SQLalchemy__
* `pip3 install flask-sqlalchemy`
* `pip3 install flask-migrate`
* `touch config.py`
* `flask db init`
* `flask db migrate -m "<your comments here>"`
* `flask db upgrade`

__Create instances of your models__
* `touch seeds.py`

__Create HTML templates__
* `mkdir app/templates`
* `touch app/templates/base.html`
* `touch app/templates/index.html`