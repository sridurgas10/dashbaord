📊 dashboard metrics to return
intern must calculate and return the following metrics from db:
1. total rentals
2. total revenue
3. top 5 rented movies
4. rentals by category
5.rentals per day


select*from inventory

--total rentals
select s.store_id,c.category_id,f.film_id,country.country_id,city.city_id,
count(r.rental_id) as total_rentals from rental r
left join inventory i on r.inventory_id = i.inventory_id
left join film f on i.film_id = f.film_id
left join film_category fc on f.film_id = fc.film_id
left join category c on fc.category_id = c.category_id
left join store s on i.store_id = s.store_id
join address a on a.address_id=s.address_id 
left join city on city.city_id=a.city_id
left join country on city.country_id=country.country_id
where r.rental_date between '2005-05-26 03:44:10.000' and '2005-08-19 06:04:07.000'
and f.film_id=862
and s.store_id=2
and c.category_id=4
and country.country_id=8
and city.city_id=576
group by s.store_id,c.category_id,f.film_id,country.country_id,city.city_id
order by count(r.rental_id)

--total revenue
select  s.store_id,c.category_id,f.film_id,city.city_id,country.country_id,sum(p.amount) as total_revenue from payment p
left join rental r on r.rental_id=p.rental_id
left join inventory i on r.inventory_id = i.inventory_id
left join film f on i.film_id = f.film_id
left join film_category fc on f.film_id = fc.film_id
left join category c on fc.category_id = c.category_id
left join store s on i.store_id = s.store_id
join address a on a.address_id=s.address_id 
left join city on city.city_id=a.city_id
left join country on city.country_id=country.country_id
where p.payment_date between '2005-05-26 03:44:10.000' and '2025-11-27 14:07:03.999'
and f.film_id=333
and s.store_id=2
and c.category_id=12
and country.country_id=8
and city.city_id=576
group by s.store_id,c.category_id,f.film_id,city.city_id,country.country_id
order by sum(p.amount)

--top 5 rented movies
select f.film_id,f.title, s.store_id,c.category_id,f.film_id,country.country_id,city.city_id,
count(r.rental_id) as total_rentals from rental r
left join inventory i on r.inventory_id = i.inventory_id
left join film f on i.film_id = f.film_id
left join film_category fc on f.film_id = fc.film_id
left join category c on fc.category_id = c.category_id
left join store s on i.store_id = s.store_id
join address a on a.address_id=s.address_id 
left join city on city.city_id=a.city_id
left join country on city.country_id=country.country_id
where r.rental_date between '2005-05-26 03:44:10.000' and '2005-08-19 06:04:07.000'
and s.store_id=2
and c.category_id=4
and country.country_id=8
and city.city_id=576
group by f.film_id,f.title, s.store_id,c.category_id,f.film_id,country.country_id,city.city_id
order by count(r.rental_id) desc
limit 5


-- rentals by category
select c.category_id,c.name, s.store_id,c.category_id,country.country_id,city.city_id,f.film_id,
count(r.rental_id) as total_rentals from rental r
left join inventory i on r.inventory_id = i.inventory_id
left join film f on i.film_id = f.film_id
left join film_category fc on f.film_id = fc.film_id
left join category c on fc.category_id = c.category_id
left join store s on i.store_id = s.store_id
join address a on a.address_id=s.address_id 
left join city on city.city_id=a.city_id
left join country on city.country_id=country.country_id
where r.rental_date between '2005-05-26 03:44:10.000' and '2005-08-19 06:04:07.000'
and s.store_id=2
and c.category_id=4
and country.country_id=8
and city.city_id=576
and f.film_id=611
group by  c.category_id,c.name,s.store_id,c.category_id,country.country_id,city.city_id,f.film_id
order by count(r.rental_id)

--.rentals per day
select s.store_id,c.category_id,f.film_id,country.country_id,city.city_id,r.rental_date,
count(r.rental_id) as total_rentals from rental r
left join inventory i on r.inventory_id = i.inventory_id
left join film f on i.film_id = f.film_id
left join film_category fc on f.film_id = fc.film_id
left join category c on fc.category_id = c.category_id
left join store s on i.store_id = s.store_id
join address a on a.address_id=s.address_id 
left join city on city.city_id=a.city_id
left join country on city.country_id=country.country_id
where r.rental_date ='2005-05-26 03:44:10.000'
and f.film_id=862
and s.store_id=2
and c.category_id=4
and country.country_id=8
and city.city_id=576
group by s.store_id,c.category_id,f.film_id,country.country_id,city.city_id,r.rental_date
order by count(r.rental_id)
