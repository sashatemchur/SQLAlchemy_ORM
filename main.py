import os

from sqlalchemy import and_
from models.database import DATABASE_NAME, Session
import create_database as db_creator
from models.lesson import Lesson, association_table
from models.student import Student
from models.group import Group


# This is the main file from which we run the entire program and there are 3 ways to output data

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()
        
        session = Session()
        
        for it in session.query(Lesson): # The first way
            print(it)
            print('*' * 5)
    
        for it in session.query(Student).join(Group).filter(Group.group_name == 'Group A'): # The second way
            print(it)
            print('*' * 5)

        for it, gr in session.query(Student, Group): # The third way
            print(it, gr)
