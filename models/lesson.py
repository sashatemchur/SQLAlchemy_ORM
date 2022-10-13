from tokenize import group
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship

from models.database import Base

# This file combines two models, student and group

association_table = Table('association', Base.metadata,
                            Column('lesson_id', Integer, ForeignKey('lessons.id')),
                                   Column('group_id', Integer, ForeignKey('groups.id'))
                                   )

class Lesson(Base):
    __tablename__ = 'lessons'
    
    id = Column(Integer, primary_key=True)
    lesson_title = Column(String)
    groups = relationship('Group', secondary=association_table, backref='group_lesson')
        
    def __repr__(self):
        return f'Subject [ID: {self.id}, Title: {self.lesson_title}]'