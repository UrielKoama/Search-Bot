create DATABASE if NOT exists searchbotDB;
    
create TABLE movies(
movie_id int PRIMARY KEY,
movie_name VARCHAR(200)
);
	
create TABLE keywords_movies(
keyword_id int PRIMARY key,
movie_name VARCHAR(200),
constraint movies_fk
	foreign key (movie_name) REFERENCES movies(movie_name)
);

create TABLE sports(
sports_id int primary KEY,
sports_name VARCHAR(200)

);

create TABLE keywords_sports(
id int PRIMARY key,
sports_name VARCHAR(200),

constraint sports_fk
	foreign key (sports_name) REFERENCES sports(sports_name)
);
 
create table music(
music_id int primary KEY,
music_name VARCHAR(200)

);

create TABLE keywords_music(
music_keyID int PRIMARY key,
music_name VARCHAR(200),

constraint music_fk
	foreign key (music_name) REFERENCES music(music_name)
);

