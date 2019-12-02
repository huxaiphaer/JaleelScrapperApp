## JaleelScrapper

This is a Web scrapper pipeline that outputs the weather at destinations of flights leaving Vienna
airport from this [website](https://www.viennaairport.com/passagiere/ankunft__abflug/abfluege).


### Functionalites

  - Storing the **Destination**, **Time**, **Temperature** and **Notes** of the Flights from Vienna in the database.
  - Caching Scrapy requests.

## Getting Started.

This is how you can setup the project on your local machine.

#### Installation.

1 . Ensure that you are having Android studio, then clone the project with the following command :

```
   $  git clone git@github.com:huxaiphaer/JaleelScrapperApp.git
```

2. After cloning the repository,then install **Mysql** and create a Database called `flights_db`.

3. Create a `.env` file in this `JaleelScrapperApp/jaleelscrapper/` directory, and add the following `VARIABLES` :

```
HOST= YOUR_HOST_NAME
USER_NAME= YOUR_DB_USER_NAME
PASSWORD= YOUR_PASSOWRD
DATABASE= flights_db
WEATHER_API_KEY= YOUR_WEATHER_API_KEY
```

Regarding the variable `WEATHER_API_KEY` , you can create an account on this [WEATHER API SITE](https://weatherstack.com/) and get the Weather API key on the dashboard
once you've signed up, it takes few minutes and the paste it alongside `WEATHER_API_KEY` variable e.g `WEATHER_API_KEY=6ydyyfy84bf84bf844HY84`. This is done because most of the API sites have limitations on requests.


4.Then, run `cd jaleelscrapper` (to change the directory) in the command or terminal , so to Activate the virtual environment use the command below : 

##### On Windows command :
`$ virtualenv env` , then `$ \env\Scripts\activate.bat`

##### On Linux & Mac:
first install pip `sudo apt-get install python3-pip`, then install virtual env `sudo pip3 install virtualenv `, the create it
`venv env` , finally activate it `/env/bin/python`

finally , 
open the project and run the following command to start scrapping :

```
   $ scrapy crawl flights_destinations
```

### Running unit tests

type the following in the terminal or command :
```
$ nosetests  
```

If you want to run tests with coverage, run the following command :

```
$ nosetests --with-coverage
```

#### Running Scrapy Tests with Test-Scrapy Library

Type the following command to run with [Scrapy Test Library](https://pypi.org/project/scrapy-test/) against live data

```
$ scrapy-test
```

Then , run the following to run against cached data :

```
$ scrapy-test --cache
```

### Languages/Libraries/Architecture Used.

- Python
- [Scrapy Library](https://scrapy.org/)
- Mysql
- Mysql-Connector
- [Weather Api](https://weatherstack.com/)

### Author
  - Lutaaya Huzaifah Idris
