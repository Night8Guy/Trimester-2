-- imports the database dump from hbtn_0d_tvshows to your local MySQL server
SELECT DISTINCT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;