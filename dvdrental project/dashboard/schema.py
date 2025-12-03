from pydantic import BaseModel
from datetime import datetime
from typing import List

class TotalRental(BaseModel):
    store_id: int
    city_id: int
    country_id: int
    film_id: int
    total_rentals: int

class TotalRevenue(BaseModel):
    store_id: int
    city_id: int
    country_id: int
    film_id: int
    total_revenue: float

class Top5RentedMovie(BaseModel):
    film_id: int
    title: str
    store_id: int
    city_id: int
    country_id: int
    total_rentals: int

class RentalsCategory(BaseModel):
    category_id: int
    name: str
    film_id: int
    store_id: int
    city_id: int
    country_id: int
    total_rentals: int

class RentalsperDay(BaseModel):
    category_id: int
    film_id: int
    store_id: int
    city_id: int
    country_id: int
    rental_date:datetime
    total_rentals: int

class DashboardResponse(BaseModel):
    total_rentals: List[TotalRental]
    total_revenue: List[TotalRevenue]
    top5_rented_movies: List[Top5RentedMovie]
    rentals_by_category: List[RentalsCategory]
    rentals_per_day:  List[RentalsperDay]
