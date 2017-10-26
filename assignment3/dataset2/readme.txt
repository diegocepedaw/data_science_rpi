ownership: RPI, Yiqing Guo
date: 17/10/2017 version number: 1.0.0
update: create the database and import the data.
datasource: worldbank, https://data.worldbank.org/data-catalog/world-development-indicators
data format: mysql database
Server version: 5.7.18-log
system: win64
Dump completed: 2017-10-22 14:41:35
character set client: utf8
ENGINE: InnoDB
data year: 1960-2016
last update: 2017
table: 
country: 
	`Country_Code` text, ISO 3166-1 standard
  	`Country_Name` text,
  	`Region` text, 8 region, Europe & central Asia, East Asia and Pacific, Latin America & Carribean, Middle east & North Africa, North America, South Asia and Sub-Saharan African. 
data: 
	`Country_Code` text, ISO 3166-1 standard
  	`year` int(11) DEFAULT NULL, 4 digit year from 1960-2016
  	`gdp` text, in usd
  	`population` bigint(20) DEFAULT NULL

 The RPI have the ownership to this dataset, and Yiqing Guo have the right to produce, modify and explain the dataset.