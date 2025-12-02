from sqlalchemy import Column, Integer, String, DateTime,ForeignKey,Float
from sqlalchemy.orm import relationship
from dbconnection import Base

class Inventory(Base):
    __tablename__ = "inventory"

    inventory_id = Column(Integer, primary_key=True, index=True)
    film_id= Column(Integer,ForeignKey("film.film_id"), primary_key=True)
    store_id=Column(Integer,ForeignKey("store.store_id"),primary_key=True)
    last_update = Column(DateTime)

    film=relationship("Film",back_populates="inventory")
    store =relationship("Store",back_populates="inventory")

class FilmCategory(Base):
    __tablename__ = "film_category"

    film_id = Column(Integer, ForeignKey("film.film_id"), primary_key=True)
    category_id = Column(Integer, ForeignKey("category.category_id"), primary_key=True)
    last_update = Column(DateTime)

    film = relationship("Film", back_populates="film_category")
    category = relationship("Category", back_populates="film_category")



class Country(Base):
    __tablename__ = "country"

    country_id = Column(Integer, primary_key=True, index=True)
    country= Column(String)
    last_update = Column(DateTime)  

    city=relationship("City",back_populates="country")  

class City(Base):
    __tablename__ = "city"

    city_id = Column(Integer, primary_key=True, index=True)
    city= Column(String)
    country_id=Column(Integer,ForeignKey("country.country_id"),primary_key=True)
    last_update = Column(DateTime)

    
    address=relationship("Address",back_populates="city")
    country=relationship("Country",back_populates="city")    

class Address(Base):
    __tablename__ = "address"

    address_id = Column(Integer, primary_key=True, index=True)
    address= Column(String)
    district=Column(String)
    city_id=Column(Integer,ForeignKey("city.city_id"),primary_key=True)
    postal_code=Column(Integer)
    phone=Column(Integer)
    last_update = Column(DateTime) 

    city=relationship("City",back_populates="address")
    
    store=relationship("Store",back_populates="address")

class Store(Base):
    __tablename__ = "store"

    store_id = Column(Integer, primary_key=True, index=True)
    manager_staff_id=Column(Integer)
    address_id = Column(Integer,ForeignKey("address.address_id"),primary_key=True)
    last_update = Column(DateTime)   

    address=relationship("Address",back_populates="store")
    inventory =relationship("Inventory",back_populates="store")

       