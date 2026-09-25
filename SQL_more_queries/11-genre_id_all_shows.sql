-- List all shows contained in the database hbtn_0d_tvshows
-- This script uses a LEFT JOIN to display NULL for shows without a genre
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
