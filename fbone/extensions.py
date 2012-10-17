# -*- coding: utf-8 -*-

from flaskext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flaskext.mail import Mail
mail = Mail()

from flaskext.cache import Cache
cache = Cache()

from flaskext.login import LoginManager
login_manager = LoginManager()