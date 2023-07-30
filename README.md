Free for commercial use countries and cities data perfectly suited for using with autocomplete. Parsed from [SimpleMaps](https://simplemaps.com/data/world-cities)

239 countries and 42905 cities.

The data is much cleaner than Geonames or several similar sources of geo data and perfectly suited for using with autocomplete (sort by population when doing a query).

The SQL file contains indexes and foreign key constraint and is ready to use.

I've also included parser, feel free to modify it for your own needs. Data source file is also included, or you can download a fresh copy from [SimpleMaps](https://simplemaps.com/data/world-cities)

`countries` table structure

| id | country |
| - | - |

`cities` table structure

| id | city | country_id | latitude | longitude | population |
| - | - | - | - | - | - |

