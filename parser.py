from csv import reader
import mysql.connector

# If you're going to parse data by yourself, fill the crednetials below
db = mysql.connector.connect(host = 'localhost', database = 'your_db', user = 'root', password = 'your_pass')

cities = {}

# Load cities into memory and create a list of countries
with open('worldcities.csv', 'r') as read_file:
    csv_reader = reader(read_file)
    for city_data in csv_reader:
        country = city_data[4]
        if country in cities:
            cities[country].append(city_data)
        else:
            cities[country] = [city_data]

# Insert countries into DB to get primary keys
for country in cities.keys():
    cursor = db.cursor()
    statement = "INSERT INTO countries(country) VALUES(\"{0}\")".format(country)
    cursor.execute(statement)
    db.commit()
    country_id = cursor.lastrowid

    for city_data in cities[country]:
        city, city_ascii, lat, lng, country, iso2, iso3, admin_name, capital, population, id = city_data
        population = 0 if population == '' else population
        statement = "INSERT INTO cities(city, country_id, latitude, longitude, population) VALUES(\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\")".format(city_ascii, country_id, lat, lng, population)
        cursor.execute(statement)
        db.commit()

print('Simplemaps data was parsed successfully')
