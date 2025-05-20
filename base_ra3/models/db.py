from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

user = 'sammy'
password = 'password'

instance = f'mysql+pymysql://{user}:{password}@localhost:3306/exp3pra3'