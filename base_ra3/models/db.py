from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

user = 'test1'
password = 'test1'

instance = f'mysql+pymysql://{user}:{password}@localhost:3306/exp3pra3'