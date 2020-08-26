# CHALLENGE 1
SELECT authors.au_id as "Author ID" ,au_lname as "Last Name", au_fname as "First name", Title, pub_name as "Publisher" FROM authors
 LEFT JOIN titleauthor ON titleauthor.au_id = authors.au_id
    LEFT JOIN titles ON titles.title_id = titleauthor.title_id
    LEFT JOIN publishers ON publishers.pub_id = titles.pub_id
    
# CHALLENGE 2
SELECT titleauthor.au_id, au_lname, au_fname,  pub_name, au_ord FROM authors
	LEFT JOIN titleauthor ON titleauthor.au_id = authors.au_id
    LEFT JOIN titles ON titles.title_id = titleauthor.title_id
    LEFT JOIN publishers ON publishers.pub_id = titles.pub_id
     ORDER BY au_ord DESC
    
# CHALLENGE 3
SELECT authors.au_id, au_lname, au_fname, qty FROM authors
	LEFT JOIN titleauthor ON titleauthor.au_id = authors.au_id
	LEFT JOIN titles ON titles.title_id = titleauthor.title_id
    LEFT JOIN publishers ON publishers.pub_id = titles.pub_id
     LEFT JOIN sales ON titleauthor.title_id = sales.title_id
     ORDER BY qty DESC
     LIMIT 3
     
# CHALLENGE 4
SELECT authors.au_id, au_lname, au_fname, qty FROM authors
	LEFT JOIN titleauthor ON titleauthor.au_id = authors.au_id
	LEFT JOIN titles ON titles.title_id = titleauthor.title_id
    LEFT JOIN publishers ON publishers.pub_id = titles.pub_id
     LEFT JOIN sales ON titleauthor.title_id = sales.title_id
     ORDER BY qty DESC

# BONUS
# :/




