create table country_news_table(
	id serial key,
	country_code varchar(50) not null,
	publish_date timestamp not null,
	link varchar(250),
	source varchar(250),
	title text
)

create table latest_update_table(
	source varchar(250),
	time timestamp
)
