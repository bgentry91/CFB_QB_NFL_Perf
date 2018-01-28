# College Football Quarterback First Year NFL Performance
For this project, I am attempting to predict college football quarterback performance in their first year in the NFL. The response variable is the first year ["passer rating"](https://en.wikipedia.org/wiki/Passer_rating) of a given quarterback and I am using a number of their college football stats and personal attributes to attempt to predict this.

All data was scraped from [sports-reference.com](https://www.sports-reference.com/) using a combination of BeautifulSoup, Scrapy, and Selenium.

The project involved creating a linear model, which initially was extremely overfit due to a large number of features. Attempts at ElasticNet Regularization failed to improve to predictive ability of the model, as did numerous Box-Cox transformations on features.