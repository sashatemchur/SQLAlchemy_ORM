from imp import load_compiled
from tokenize import group
from faker import Faker

from models.database import create_db, Session
from models.lesson import Lesson
from models.student import Student
from models.group import Group


def create_database(load_fake_data: bool = True):
    # This is the function that creates our database and writes data to it from the _load_fake_data function
    create_db()
    if load_fake_data:
        _load_fake_data(Session())
      
        
def _load_fake_data(session: Session):
    # Creates fake data using the faker library
    lessons_names = ['MAthematics', 'Programming', 'History', 'Algebra', 'Physical education']
    group1 = Group(group_name='Group A')
    group2 =  Group(group_name='Group B')
    session.add(group1)
    session.add(group2)
    
    for key, it in enumerate(lessons_names):
        lesson = Lesson(lesson_title=it)
        lesson.groups.append(group1)
        if key % 2 == 0:
            lesson.groups.append(group2)
        session.add(lesson)
        
    faker = Faker('en_US')
    group_list = [group1, group2]
    session.commit()
    
    for _ in range(50):
        full_name = faker.name().split(' ')
        age = faker.random.randint(13, 18)
        address = faker.address()
        group = faker.random.choice(group_list)
        student = Student(full_name, age, address, group.id)
        session.add(student)
    
    session.commit()
    session.close()
        