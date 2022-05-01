import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    password = Column(String(100), nullable=False)
    cellphone = Column(Integer, nullable=False)
    post = relationship("post")
    seguidores = relationship("seguidores")
    seguidos = relationship("seguidos")

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    imagen = Column(String(250))
    copy = Column(String(250))
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("user")
    like = relationship("like")
    comments = relationship("comments")

class Seguidores(Base):
    __tablename__ = "seguidores"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id")) 
    seguidores_id = Column(Integer)
    user = relationship("user")

class Seguidos(Base):
    __tablename__ = "seguidos"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id")) 
    seguidos = Column(Integer)
    user = relationship("user")

class Like(Base):
    __tablename__ = "like"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("post.id")) 
    post = relationship("post")

class Comments(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("post.id")) 
    comments = Column(String(100))
    post = relationship("post")

    def to_dict(self):
        return {}


try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e