from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class ormUser(Base):
    __tablename__ = 'orm_user'

    email = Column(String(255), primary_key=True)
    id = Column(Integer(10), nullable=False)
    full_name = Column(String(255), nullable=False)
    
    orm_Document = relationship('ormDocument', secondary='orm_edit_Document_By_Template')


class ormDocument(Base):
    __tablename__ = 'orm_Document'
    data_field = Column(String(255), primary_key=True)
    name_field = Column(Integer(10), nullable=False)
    description = Column(String(255))


    orm_users = relationship('ormUser', secondary='orm_edit_Document_By_Template')


class ormEditDocByTemplate(Base):
    __tablename__ = 'orm_edit_Document_By_Template'

    email = Column(String(255),ForeignKey('orm_user.email'),primary_key = True)
    data_field = Column(String(255), ForeignKey('orm_Document.data_field'), primary_key=True)
