import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    userId = Column(Integer, primary_key=True)
    userName = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)


class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    characterId = Column(Integer, primary_key=True)
    name = Column(String(250))
    gender = Column(String(250))
    skin_color = Column(String(250))
    height = Column(Integer)
    birth_year = Column(Integer)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    planetsId = Column(Integer, primary_key=True)
    planet_name = Column(String(250))
    population = Column(Integer)
    diameter = Column(Integer)
    climaty = Column(String(250))
    gravity = Column(String(250))
    terrain = Column(String(250))

class Ships(Base):
    __tablename__ = 'ships'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    shipsId = Column(Integer, primary_key=True)
    ship_name = Column(String(250))
    max_speed = Column(Integer)
    passengers = Column(Integer)
    model = Column(String(250))

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    favId = Column(Integer, primary_key=True)
    shipsId = Column(Integer, ForeignKey("ships.id"))
    planetsId = Column(Integer, ForeignKey("planets.id"))
    charId = Column(Integer, ForeignKey("character.id"))
    userId = Column(Integer, ForeignKey("user.id"))
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
