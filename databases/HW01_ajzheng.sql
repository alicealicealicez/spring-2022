
CREATE TABLE Coach(
	cid int not null auto_increment,
	name varchar(20),
	end_date date,
	PRIMARY KEY(cid)
	)engine = innodb;
	
CREATE TABLE Team (
	tid int not null auto_increment,
	name varchar(20),
	stadium varchar(20),
	city varchar(20),
	coach int not null,
	PRIMARY KEY(tid),
	FOREIGN KEY(coach) References Coach(cid)
	)engine = innodb;
	
CREATE TABLE Player(
	pid int not null auto_increment,
	name varchar(20),
	number int,
	position varchar(20),
	team int,
	PRIMARY KEY(pid),
	FOREIGN KEY(team) References Team(tid)
	)engine = innodb;
	
CREATE TABLE Game(
	home int not null,
	away int not null, 
	week int not null,
	home_qb int not null,
	away_qb int not null,
	PRIMARY KEY(home, week),
	FOREIGN KEY(home) References Team(tid),
	FOREIGN KEY(away) References Team(tid),
	FOREIGN KEY(home_qb) References Player(pid),
	FOREIGN KEY(away_qb) References Player(pid)
	)engine = innodb;

INSERT INTO Coach(name, end_date)
VALUES ("Big Potato", DATE'2025-12-05'),
("Big Chicken", DATE'2025-12-04'),
("Big Bread", DATE'2025-12-03'),
("Big Soup", DATE'2025-12-02');
	
INSERT INTO Team(name, stadium, city, coach)
VALUES ("Pittsburg Potatoes", "Oven Stadium", "Pittsburg", 1),
("Chicago Chickens", "Pan Stadium", "Chicago", 2),
("Boston Bread", "Toaster Stadium", "Boston", 3),
("Seattle Soups", "Pot Stadium", "Seattle", 4);

INSERT INTO Player(name, number, position, team)
VALUES ("French Fry", 1, "QB", 1),
("Roasted Chicken", 2, "QB", 2),
("Golden Toast", 3, "QB", 3),
("Clam Chowder", 4, "QB", 4),
("Mashed Potato", 5, "Kicker", 1),
("Chicken Salad", 6, "LB", 2),
("French Baguette", 7, "LB", 3),
("Tomato Bisque", 8, "LB", 4);

INSERT INTO Game
VALUES (1, 2, 1, 1, 2),
(3, 4, 2, 3, 4),
(1, 3, 3, 1, 3);

SELECT name, stadium, city
FROM Team

SELECT name, number
FROM Player
WHERE position = "QB"

SELECT Coach.Name, Team.name, Coach.end_date
FROM Coach
JOIN Team ON Coach.cid = Team.coach
ORDER BY end_date DESC

SELECT Player.name, Player.position, Team.name 
FROM Player
JOIN Team ON Team.tid = Player.team
ORDER BY Team.name, Player.name

SELECT Team.name AS "Home", Team.stadium, Game.week 
FROM Game 
JOIN Team ON Game.home = Team.tid 

SELECT Team.name AS "Away", Team.stadium, Game.week 
FROM Game 
JOIN Team ON Team.tid = Game.away

