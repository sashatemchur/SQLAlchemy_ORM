from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.database import Base


class Group(Base):
    # This class creates a model in the database
    __tablename__ = 'groups'
    
    id = Column(Integer, primary_key=True)
    group_name = Column(String)
    student = relationship('Student')


    def __repr__(self):
        return f'Group [ID: {self.id}, Title: {self.group_name}]'