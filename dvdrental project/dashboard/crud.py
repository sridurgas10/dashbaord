
from sqlalchemy import select, func, and_,or_
from sqlalchemy.orm  import Session
from rental.models import Rental
from payment.models import Payment 
from dashboard.model import City,Country,Address,Store,Inventory,FilmCategory
from film.models import Film
from category.model import Category


def total_rental(start_date,end_date,store_id,city_id,country_id,category_id,film_id, db: Session):
    query = (
        select (Store.store_id,City.city_id,Country.country_id,Category.category_id,Film.film_id,
                (func.count(Rental.rental_id).label("total_rentals")))
        .select_from(Rental)
        .join(Inventory, Rental.inventory_id == Inventory.inventory_id)
        .outerjoin(Store, Inventory.store_id == Store.store_id)
        .join(Address, Store.address_id == Address.address_id)
        .outerjoin(City, Address.city_id == City.city_id)
        .outerjoin(Country, City.country_id == Country.country_id)
        .outerjoin(Film, Inventory.film_id == Film.film_id)
        .outerjoin(FilmCategory, Film.film_id == FilmCategory.film_id)
        .outerjoin(Category, FilmCategory.category_id == Category.category_id)
       .where(
          and_(
               or_(Rental.rental_date.between(start_date, end_date), start_date == None, end_date == None),
               or_(Store.store_id == store_id, store_id == None),
               or_(City.city_id == city_id, city_id == None),
               or_(Country.country_id == country_id, country_id == None),
               or_(Category.category_id == category_id, category_id == None),
               or_(Film.film_id == film_id, film_id == None)
    )
)

        .group_by (Store.store_id,Category.category_id,Film.film_id,Country.country_id,City.city_id)
        .order_by (func.count(Rental.rental_id) )       
        
    )
    result = db.execute(query).all()
    return result
   

def total_revenue(start_date,end_date,store_id,city_id,country_id,category_id,film_id, db: Session):
    query = (
        select(Store.store_id,City.city_id,Country.country_id,Category.category_id,Film.film_id,
               (func.sum(Payment.amount).label("total_revenue")))
        .select_from(Payment)
        .join(Rental, Payment.rental_id == Rental.rental_id)
        .join(Inventory, Rental.inventory_id == Inventory.inventory_id)
        .outerjoin(Store, Inventory.store_id == Store.store_id)
        .join(Address, Store.address_id == Address.address_id)
        .outerjoin(City, Address.city_id == City.city_id)
        .outerjoin(Country, City.country_id == Country.country_id)
        .outerjoin(Film, Inventory.film_id == Film.film_id)
        .join(FilmCategory, Film.film_id == FilmCategory.film_id)
        .outerjoin(Category, FilmCategory.category_id == Category.category_id)
        .where(
          and_(
              or_(Rental.rental_date.between(start_date, end_date), start_date == None, end_date == None),
              or_(Store.store_id == store_id, store_id == None),
              or_(City.city_id == city_id, city_id == None),
              or_(Country.country_id == country_id, country_id == None),
              or_(Category.category_id == category_id, category_id == None),
              or_(Film.film_id == film_id, film_id == None)
        )
        )
        .group_by(Store.store_id,City.city_id,Country.country_id,Category.category_id,Film.film_id)
        .order_by(func.sum(Payment.amount))
    )
    result = db.execute(query).all()
    return result

def top5_rented_movie(start_date,end_date,store_id,city_id,country_id,category_id, db: Session):
    query =(
         select (Film.film_id,Film.title,Store.store_id,City.city_id,Country.country_id,Category.category_id,
                (func.count(Rental.rental_id).label("total_rentals")))
        .select_from(Rental)
        .join(Inventory, Rental.inventory_id == Inventory.inventory_id)
        .outerjoin(Store, Inventory.store_id == Store.store_id)
        .join(Address, Store.address_id == Address.address_id)
        .outerjoin(City, Address.city_id == City.city_id)
        .outerjoin(Country, City.country_id == Country.country_id)
        .outerjoin(Film, Inventory.film_id == Film.film_id)
        .outerjoin(FilmCategory, Film.film_id == FilmCategory.film_id)
        .outerjoin(Category, FilmCategory.category_id == Category.category_id)
        .where(
          and_(
              or_(Rental.rental_date.between(start_date, end_date), start_date == None, end_date == None),
              or_(Store.store_id == store_id, store_id == None),
              or_(City.city_id == city_id, city_id == None),
              or_(Country.country_id == country_id, country_id == None),
              or_(Category.category_id == category_id, category_id == None)
             
        )      
        )
        .group_by(Film.film_id, Film.title,Store.store_id,City.city_id,Country.country_id,Category.category_id)
        .order_by(func.count(Rental.rental_id).desc())
        .limit(5)
        )

    

    result = db.execute(query).all()
    return result


def rentals_per_category(start_date,end_date,store_id,city_id,country_id,category_id,film_id, db: Session):
    query = (
        select(
            Category.category_id,Category.name,Store.store_id,City.city_id,Country.country_id,Film.film_id,
            (func.count(Rental.rental_id).label("total_rentals")))
        .select_from(Rental)
        .join(Inventory, Rental.inventory_id == Inventory.inventory_id)
        .outerjoin(Store, Inventory.store_id == Store.store_id)
        .join(Address, Store.address_id == Address.address_id)
        .outerjoin(City, Address.city_id == City.city_id)
        .outerjoin(Country, City.country_id == Country.country_id)
        .outerjoin(Film, Inventory.film_id == Film.film_id)
        .outerjoin(FilmCategory, Film.film_id == FilmCategory.film_id)
        .outerjoin(Category, FilmCategory.category_id == Category.category_id)
        .where(
          and_(
              or_(Rental.rental_date.between(start_date, end_date), start_date == None, end_date == None),
              or_(Store.store_id == store_id, store_id == None),
              or_(City.city_id == city_id, city_id == None),
              or_(Country.country_id == country_id, country_id == None),
              or_(Category.category_id == category_id, category_id == None),
              or_(Film.film_id == film_id, film_id == None)
        )
        )
        .group_by(Category.category_id, Category.name,Store.store_id,City.city_id,Country.country_id,Film.film_id)
        .order_by(func.count(Rental.rental_id))
    )
    result = db.execute(query).all()
    return  result

def rentals_per_day(start_date,end_date,store_id,city_id,country_id,category_id,film_id, db: Session):
   
    query =(
        select (Store.store_id,City.city_id,Country.country_id,Category.category_id,Film.film_id,Rental.rental_date,
                (func.count(Rental.rental_id).label("total_rentals")))
        .select_from(Rental)
        .join(Inventory, Rental.inventory_id == Inventory.inventory_id)
        .outerjoin(Store, Inventory.store_id == Store.store_id)
        .join(Address, Store.address_id == Address.address_id)
        .outerjoin(City, Address.city_id == City.city_id)
        .outerjoin(Country, City.country_id == Country.country_id)
        .outerjoin(Film, Inventory.film_id == Film.film_id)
        .outerjoin(FilmCategory, Film.film_id == FilmCategory.film_id)
        .outerjoin(Category, FilmCategory.category_id == Category.category_id)
        .where(
          and_(
              or_(Rental.rental_date.between(start_date, end_date), start_date == None, end_date == None),
              or_(Store.store_id == store_id, store_id == None),
              or_(City.city_id == city_id, city_id == None),
              or_(Country.country_id == country_id, country_id == None),
              or_(Category.category_id == category_id, category_id == None),
              or_(Film.film_id == film_id, film_id == None)
        )
        )  
        .group_by (Store.store_id,Category.category_id,Film.film_id,Country.country_id,City.city_id,Rental.rental_date)
        .order_by (func.count(Rental.rental_id) )       
        
    )
    result = db.execute(query).all()
    return result
    

    
