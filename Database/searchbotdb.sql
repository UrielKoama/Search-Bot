drop DATABASE if exists searchbotDB;
create DATABASE if NOT exists searchbotDB;
use searchbotDB;

create TABLE if not exists movies(
movie_id int Not NULL,
PRIMARY KEY(movie_id),
movie_name VARCHAR(200)
);

create TABLE if NOT exists keyword_movies(
movie_id int not NULL PRIMARY key,
movie_name VARCHAR(200),
constraint movies_fk
	foreign key (movie_id) REFERENCES movies(movie_id)
);

create TABLE if NOT EXISTS sports(
sports_id int NOT NULL,
primary KEY (sports_id),
sports_name VARCHAR(200)
);

create TABLE if NOT EXISTS keyword_sports(
sports_id int NOT NULL, 
PRIMARY key(sports_id),
sports_name VARCHAR(200),
constraint sports_fk
	foreign key (sports_id) REFERENCES sports(sports_id)
);
 

create table if not exists music(
music_id int NOT NULL,
primary KEY(music_id),
music_name VARCHAR(200)
);

create TABLE if not EXISTS keyword_music(
music_keyID int PRIMARY key,
music_name VARCHAR(200),
constraint music_fk
	foreign key (music_keyID) REFERENCES music(music_id)
);

