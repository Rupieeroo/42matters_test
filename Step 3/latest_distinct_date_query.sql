SELECT DISTINCT ON (a.title) * 
FROM apps a
ORDER BY a.title, a.last_update_date DESC;