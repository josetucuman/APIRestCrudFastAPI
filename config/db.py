from math import e
from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:@localhost:3306/db_logincat")



meta_data = MetaData()

