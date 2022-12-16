import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er
import enum
from sqlalchemy import Integer, Enum

Base = declarative_base()


class Characters(Base):
    __tablename__ = 'characters'
    name = Column(String(250), ForeignKey("vehicle.pilot"), ForeignKey("favorites.favorite_characters"))
    planet_from = Column(String(250), ForeignKey("planets.name"))
    id = Column(Integer, primary_key=True)
    age = Column(Integer)
    
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    size = Column(Integer)
    population = Column(Integer)
    climate = Column(String(250))
    name = Column(String(250), ForeignKey("favorites.favorite_planets"))

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), ForeignKey("favorites.favorite_vehicles"))
    pilot = Column(String(250))
    type = Column(String(250))

class Users(Base):
    __tablename__ = 'users'
    username = Column(String(250), nullable=False)
    pasword = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey("favorites.user_id"), primary_key=True)

class Favorites(Base):
    __tablename__ = 'favorites'
    date_added = Column(DateTime(False))
    user_id = Column(Integer, primary_key=True)
    favorite_characters = Column(Integer)
    favorite_planets = Column(Integer)
    favorite_vehicles = Column(Integer)


# class Post(Base):
#     __tablename__ = 'post'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('user.id'))

# class Comment(Base):
#     __tablename__ = 'comment'
#     id = Column(Integer, primary_key=True)
#     comment_text = Column(String(250), nullable=False)
#     author_id = Column(Integer, ForeignKey('user.id'))
#     post_id = Column(Integer, ForeignKey('post.id'))

# class MediaType(enum.Enum):
#     png = "png"
#     jpg = "jpg"
#     gif = "gif"

# class Media(Base):
#     __tablename__ = 'media'
#     id = Column(Integer, primary_key=True)
#     type = Column(Enum(MediaType))
#     url = Column(String(250), nullable=False)
#     post_id = Column(Integer, ForeignKey('post.id'))
    
   

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
