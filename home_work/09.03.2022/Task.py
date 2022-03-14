from sqlalchemy import create_engine

e = create_engine('sqlite:///sqlite1.db')
e.execute("""
    CREATE TABLE user (
        id INTEGER primary key autoincrement,
        firstname VARCHAR(255),
        lastname VARCHAR(255),
        age integer
    )
""")
conn = e.connect()
transaction = conn.begin()

conn.execute(
    "INSERT INTO USER (firstname, lastname, age) VALUES (:firstname, :lastname, :age)",
    firstname="Pasha", lastname="Ivanov", age=30,
)
conn.execute(
    "INSERT INTO USER (firstname, lastname, age) VALUES (:firstname, :lastname, :age)",
    firstname="Nick", lastname="Tim", age=25,

)
conn.execute(
    "INSERT INTO USER (firstname, lastname, age) VALUES (:firstname, :lastname, :age)",
    firstname="Nick", lastname="Yersh", age=31,

)
conn.execute(
    "INSERT INTO USER (firstname, lastname, age) VALUES (:firstname, :lastname, :age)",
    firstname="Jack", lastname="Jer", age=28,

)
transaction.commit()
conn.close()

conn = e.connect()
transaction = conn.begin()


result = e.execute("""
    SELECT * FROM user WHERE firstname = 'Nick' or age < 30;
""")
for user in result:
    print(user)

result1 = e.execute("""
    SELECT * FROM user WHERE age > 15 and age < 26;
""")
for user in result1:
    print(user)