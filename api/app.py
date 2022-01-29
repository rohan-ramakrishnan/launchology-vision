from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# initializing the app and database
app = Flask("__name__")
db = SQLAlchemy()
db.init_app(app)


# main function
if __name__ == "main":
    app.run(debug=True)
