## JaleelScrapper

This is a Web scrapper pipeline that outputs the weather at destinations of flights leaving Vienna
airport from this [website](https://www.viennaairport.com/passagiere/ankunft__abflug/abfluege).


### Functionalites

  - Storing the **Destination**, **Time**, **Temperature** and **Notes** of the Flights from Vienna in the database.
  - Caching Scrapy requests.

## Getting Started.

This is how you can setup the project on your local machine.

#### Installation.

Ensure that you are having Android studio, then clone the project with the following command :

```
     git clone git@github.com:huxaiphaer/JaleelScrapperApp.git
```

After cloning the repository, `cd jaleelscrapper` in the command or terminal , then Activate the virtual environment as below : 

##### On Windows command :
`virtualenv env` , then `\env\Scripts\activate.bat`

##### On Linux & Mac:
`venv env` , then `/env/bin/python`

finally , 
open the project and run the following command to start scrapping :

```
    scrapy crawl flight_destinations
```

### Running unit tests

type the folling in the terminal or command :
```
nosetests  
```

If you want to run tests with coverage, run the following command :

```
nosetests --with-coverage
```

### Languages/Libraries/Architecture Used.

- Python
- [Scrapy Library](https://scrapy.org/)
- Mysql
- Mysql-Connector
- [Weather Api](https://weatherstack.com/)

### Author
  - Lutaaya Huzaifah Idris
