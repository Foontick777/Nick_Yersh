from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()
engine = create_engine("sqlite:///sqlite.db")


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    group_id = Column(
        Integer, ForeignKey("group.id"), nullable=False)
    group = relationship(
        "Group", foreign_keys="Student.group_id", backref="student")

class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    title = Column(String)



Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
group = Group(title='G1')
s1 = Student(firstname='Ivan', lastname="Ivan", group=group)
s2 = Student(firstname='Neivan', lastname="NeIvan", group=group)
s3 = Student(firstname='Name', lastname="Surname", group=group)
group2 = Group(title='G2')
s4 = Student(firstname='Pavel', lastname="Iv", group=group2)
s5 = Student(firstname='Nick', lastname="Nam", group=group2)
s6 = Student(firstname='Tom', lastname="Sami", group=group2)
session.add_all([group, s1, s2, s3, group2, s4, s5, s6])
session.commit()