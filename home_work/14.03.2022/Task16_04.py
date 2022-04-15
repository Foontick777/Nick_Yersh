from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()
engine = create_engine("sqlite:///sqlite04.db", echo=True)

association_table = Table('association', Base.metadata,
                          Column('student_id', Integer, ForeignKey('student.id')),
                          Column('book_id', Integer, ForeignKey('book.id'))
                          )



class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)


class Book(Base):
    __tablename__= 'Book'
    id = Column(Integer, primary_key=True)
    title= Column(String)
    pages_count = Column(Integer)
    student = relationship("Student",
                           secondary=association_table, backref='student')


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

s1 = Student(firstname='Ivan', lastname="Ivanov")
s2 = Student(firstname='Iv', lastname="Ivan")
s3 = Student(firstname='Nick', lastname="Er")
book1 = Book(title='Book1', pages_count=120)
book2 = Book(title='Book2', pages_count=420)
book3 = Book(title='Book3', pages_count=220)



session.add_all([s1,s2,s3, book1,book2,book3])
session.commit()

conn = engine.connect()
# p = association_table.insert().values(book_id=1, student_id=3)
# conn.execute(p)