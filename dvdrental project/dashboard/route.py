
 
from fastapi import APIRouter
from sqlalchemy.orm  import Session
from dbconnection import get_db
from fastapi import Depends
from datetime import datetime
from dashboard import crud,schema
from typing import Optional

dashboard_router=APIRouter(prefix="/dashboard",tags=["dashboard"])




@dashboard_router.get("/v1/",response_model=schema.DashboardResponse) 
async def dashboard(start_date: Optional[datetime]=None,
    end_date: Optional[datetime]=None, 
    store_id: Optional[int]=None, 
    city_id: Optional[int]=None ,
    country_id: Optional[int]=None, 
    category_id: Optional[int]=None, 
    film_id: Optional[int] =None,
db:Session=Depends(get_db)):
    total_rentals=crud.total_rental(start_date,end_date,store_id,city_id,country_id,category_id,film_id,db)
    total_revenue=crud.total_revenue(start_date,end_date,store_id,city_id,country_id,category_id,film_id,db)
    top5_rented_movie=crud.top5_rented_movie(start_date,end_date,store_id,city_id,country_id,category_id,db)
    rental_by_category=crud.rentals_per_category(start_date,end_date,store_id,city_id,country_id,category_id,film_id,db)
    rental_per_day=crud.rentals_per_day(start_date,end_date,store_id,city_id,country_id,category_id,film_id,db)
    return {
    "total_rentals": total_rentals,
    "Total_Revenue": total_revenue,
    "Top5_rented_movies": top5_rented_movie,
    "Rentals_by_category": rental_by_category,
    "Rentals_per_day": rental_per_day
}

    