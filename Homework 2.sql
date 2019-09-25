USE sakila;

SELECT f.title, f.description, a.first_name, a.last_name
FROM film f
WHERE (title LIKE "zo%")
JOIN film_actor fa
ON f.film_id = fa.film_id
JOIN actor a
ON a.actor_id = fa.actor_id


