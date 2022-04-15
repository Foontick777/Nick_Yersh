from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
Base = declarative_base()
engine = create_engine("sqlite:///sqlite1.db", echo=True)



class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)


class Diary(Base):
    __tablename__= 'diary'
    id = Column(Integer, primary_key=True)
    gpa = Column(Integer)
    student_id = Column(Integer, ForeignKey("student.id"), nullable=False)
    student = relationship(
        "Student",
        foreign_keys="Diary.student_id",
        backref=backref("diary", uselist=False))


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

s1 = Student(firstname='Ivan', lastname="Ivanov")
diary = Diary(gpa=6, student=s1)


session.add_all([s1, diary])
session.commit()