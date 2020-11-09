from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate , MigrateCommand
from flask_script import Manager

from flask_admin import Admin
from flask_admin import AdminIndexView 
from flask_admin.contrib.sqla import ModelView

from flask_security import SQLAlchemyUserDatastore
from flask_security import Security

from flask_security import current_user
from flask import redirect, url_for, request




app = Flask(__name__)
app.config.from_object(Configuration)


db = SQLAlchemy(app)

migrate = Migrate(app , db)
manager = Manager(app)
manager.add_command('db' , MigrateCommand)


# Admin #
from models import * # esli budet vishe to error import togo chego eshe net a tut norm




admin = Admin(app)
admin.add_view(ModelView(Post , db.session))
admin.add_view(ModelView(Tag , db.session))


# flask security##

user_datastore = SQLAlchemyUserDatastore(db, User , Role)
security = Security(app , user_datastore)
