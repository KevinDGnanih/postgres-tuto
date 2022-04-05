from sqlalchemy import (
    create_engine, Table, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instruction from the "chinook" datbase
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a clase-based model for the "Programmer" table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# open an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

#  creating records on our Programmer table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="Frist Programmer" 
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Programmer" 
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language" 
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="Americian",
    famous_for="Apollo 11" 
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="Amercian",
    famous_for="Microsoft" 
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web" 
)

kevin_davy_white = Programmer(
    first_name="Kevin",
    last_name="Davy White",
    gender="M",
    nationality="French",
    famous_for="Awarded Best Singer Songwriter" 
)

# add each instance of our programmers to our session
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(kevin_davy_white)

# updating a single recod
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "Internation Star"

# commit our session to the database
# session.commit()

# updating miltiple records
# people = session.query(Programmer)
# for person in people:
#    if person.gender == "F":
#        person.gender = "Female"
#    elif person.gender == "M":
#        person.gender = "Male"
#    else:
#        print("Gender not defined")
#    session.commit()


# deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# defensive programming
if programmer is not None:
    print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
    confirmation = input("Are you sure you want to delete this records? (y/n)")
    if confirmation.lower() == "y":
        session.delete(programmer)
        session.commit()
        print("Prgrammer has been deleted")
    else:
        print("Programmer not deleted")
else:
    print("No records found")


# delete multiple records
# programmers = session.query(Programmer)
# for programmer in programmers:
#    session.delete(programmer)
#   session.commit()

# query the database to find all Programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )