# CompareCarPrices

Project Objective: 

A web application for comparing the prices of best selling cars with 3 website CarTrade(http://www.cartrade.com/), CarWale(http://www.carwale.com/) and CarDekho (http://www.cardekho.com/ )

This is application must be developed considering Trivago (Compare hotel prices on 280 booking sites at once)

Project Description:

1. This web application will have different search filters to search and compare the cars prices. Like City, Model, price range, Model Year, etc.

2. It will show the results from 3 websites listed above.

3. To achive this, need to scrap the data every day from above listed websites. 


Technology Stack:

1. Github
2. Django, Mysql, Angular JS
3. ElasticSearch, Selenium for scrapping , Celery and RabbitMQ with periodic tasks to run the scrapping every day and saving to database. Use Proxy servers(to hide our IP and preventing from blocking IP when scrapping)
4. Heroku(Live server), Nginx and gunicorn servers
5. Test suite to test the functionality (Django unit testing and selenium testing)