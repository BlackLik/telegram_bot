from ast import Index
from sqlalchemy import Column, Integer, String, Index
from server import Base, engine, name_database
from sqlalchemy.orm import Session
import os.path

def create_database():
    if os.path.exists(name_database) == False: 
        Base.metadata.create_all(engine)
        print('Database created successfully')
    else:
        print('Database already exists')

session = Session(engine)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_telegram = Column(Integer, nullable=False)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    phone_number = Column(String(12), nullable=False)
    vcard = Column(String, nullable=True)
    __table_args__ = (
        Index('index_id_tg', id_telegram, unique=True),
    )
    
    def __repr__(self) -> str:
        return f'User(id={self.id}, id_telegram={self.id_telegram}, first_name={self.first_name}, last_name={self.last_name}, phone_number={self.phone_number}, vcard={self.vcard})'
    