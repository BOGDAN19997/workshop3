from dao.orm.model import *
from dao.db import TaxesDb

db = TaxesDb()

Base.metadata.create_all(db.sqlalchemy_engine)


session = db.sqlalchemy_session

# clear all tables in right order
session.query(ormUserDocument).delete()
session.query(ormDocument).delete()
session.query(ormUser).delete()


# populate database with new rows

Bogdan = ormUser( user_name="Bogdan",
               user_birthday='10-OCT-2000',
               user_email='bogdan.galuga@gmail.com',
               user_studybook='KM1111',
               user_year='04-DEC-1997',
               )



Andriy = ormUser( user_name="Andriy",
               user_birthday='10-OCT-2001',
               user_email='andrew34@gmail.com',
               user_studybook='KM2222',
               user_year='10-OCT-2010',
               )


Petro = ormUser( user_name="Peter",
               user_birthday='10-OCT-2011',
               user_email='peta.cool@gmail.com',
               user_studybook='KM2222',
               user_year='10-OCT-2010',
               )



Casco = ormSkill(data_field='Casco')
Taxes = ormSkill(skill_name='Taxes')

# create relations
Bob.orm_skills.append(Casco)
Bob.orm_skills.append(Taxes)

Boba.orm_skills.append(Casco)

Boban.orm_skills.append(Taxes)

# insert into database
session.add_all([Casco,Taxes,Bogdan,Andriy,Petro])

session.commit()