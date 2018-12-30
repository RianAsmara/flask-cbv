# Example Flask Class Basic View
This is sample project using to implement Class Basic View in Flask. This just for learning. In this project will tech you, how to write flask app using Class Basic View.

## Installation Package
This app using this package:

1. Flask
2. Flask Migrate
3. Flask Marshmallow
4. Marshmallow SQLAlchemy
5. PyMysql for database dialect
6. Flask-Restplus for Building Rest Api and Swagger Documentation
7. Flask-Script for executing our app using Command Line Interface (CLI)
8. Flask-SQLAlchemy for Database ORM(Object Relation Mapping)

To install all packages you just running this command in your terminal.

```$ pip install -r requirements.txt```



## Running Apps

Before you run this apps. You should have to create database. And change DATABASE_URI, API_VERSION, APP_MODE and SECRET_KEY in ```tools\migrate.sh``` and ```tools\run.sh``` with your database name, api version, app mode with this options [production, testing, develompent] and your secret key. And running ```tools\migrate.sh``` to create database and all object to table in database.

And next run your application with execute ```$./todos/run.sh```

Open your browser and go to this url ```http://localhost:8009/api/$YOUR_API_VERSION/todos```

### ***Happy Coding and Keep Learning***