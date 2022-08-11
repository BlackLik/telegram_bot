from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()
name_database = 'report.db'
engine = create_engine(f'sqlite:///{name_database}')
