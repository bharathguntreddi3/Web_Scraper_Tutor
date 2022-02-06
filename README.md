<p align="center"><img height = "200" src = "https://user-images.githubusercontent.com/95229816/152684469-0f6f1fef-d66b-4e8d-b9a6-c4fcf418358e.jpg"></p>

### <h1><p align = "center">Web Scraper Tutor</p></h1>

This repo basically contains details on how to work with WEB SCRAPER and different application of Web scraping.

## web scrapping makes web data extraction easy and accessible for everyone.

Our main goal is to make the web data extraction as simple as possible.

To configure Scraper all you need is just point and click the elements on your desired webpage.

![config](https://user-images.githubusercontent.com/95229816/152686761-0a127849-8c01-4ec1-a7cc-757e76452497.jpg)

<h3>Its requires zero coding knowledge(browser extension).</h3>
 
Of course you can create your own scraper by using python and other programming languages where you need to do some sort coding stuff.


## What does actually web scrapping means ?
  
Suppose you want some information from a website? Let’s say a paragraph on Narendra Modi! What do you do? Well, you can copy and paste the information from Wikipedia to your own file. But what if you want to get large amounts of information from a website as quickly as possible? Such as large amounts of data from a website to train a [`Machine Learning`](https://towardsdatascience.com/web-scraping-for-machine-learning-5fffb7047f70) algorithm? In such a situation, copying and pasting will not work! And that’s when you’ll need to use Web Scraping.

![ML_scrap](https://user-images.githubusercontent.com/95229816/152687120-9b108aae-3f84-4dc6-88b4-6f5342f3dd66.png)


<h4>Unlike the long and mind-numbing process of manually getting data, Web scraping uses intelligence automation methods to get thousands or even millions of data sets in a smaller amount of time.</h4>

# What is Web Scraping?

Web scraping is an automatic method to obtain large amounts of data from websites. Most of this data is unstructured data in an HTML format which is then converted into structured data in a spreadsheet or a database so that it can be used in various applications. There are many different ways to perform web scraping to obtain data from websites. These include using online services, particular API’s or even creating your code for web scraping from scratch. Many large websites, like [Google](https://www.google.com/), [Twitter](https://twitter.com/), [Facebook](https://www.facebook.com/), [StackOverflow](https://stackoverflow.com/), etc. have [API’s](https://www.mulesoft.com/resources/api/what-is-an-api#:~:text=API%20is%20the%20acronym%20for,you're%20using%20an%20API.) that allow you to access their data in a structured format. This is the best option, but there are other sites that don’t allow users to access large amounts of data in a structured form or they are simply not that technologically advanced. In that situation, it’s best to use Web Scraping to scrape the website for data.

![Python-Web-Scraping](https://user-images.githubusercontent.com/95229816/152687770-cc346743-e709-4751-b576-cc691bce4ca3.gif)

## Required Parts

Crawler : 
The crawler is an artificial intelligence algorithm that browses the web to search for the particular data required by following the links across the internet.

scraper : 
The scraper, on the other hand, is a specific tool created to extract data from the website. The design of the scraper can vary greatly according to the complexity and scope of the project so that it can quickly and accurately extract the data.


![crawlevsscraper](https://user-images.githubusercontent.com/95229816/152688053-d24f5330-9226-421e-ab87-d647f55caf5c.jpg)

# How Web Scraper Works?

Web Scrapers can extract all the data on particular sites or the specific data that a user wants. Ideally, it’s best if you specify the data you want so that the web scraper only extracts that data quickly.

When a web scraper needs to scrape a site, first the URLs are provided. Then it loads all the HTML code for those sites and a more advanced scraper might even extract all the CSS and Javascript elements as well. Then the scraper obtains the required data from this HTML code and outputs this data in the format specified by the user.

[<h3>`Web Scraper`</h3>](https://www.parsehub.com/blog/what-is-web-scraping/)

### Web Scraping Tools

Various tools are provided in the market for webscraping. Here I am going to present you the best web scarping tools.

1.[ParseHub](https://hevodata.com/learn/8-best-web-scraping-tools/#ParseHub)

2.[Scrapy](https://hevodata.com/learn/8-best-web-scraping-tools/#Scrapy)

3.[Octoparse](https://hevodata.com/learn/8-best-web-scraping-tools/#OctoParse)

4.[scraper API](https://hevodata.com/learn/8-best-web-scraping-tools/#ScraperAPI)

5.[Mozenda](https://hevodata.com/learn/8-best-web-scraping-tools/#Mozenda)

6.[Webhose.io](https://hevodata.com/learn/8-best-web-scraping-tools/#Webhose.io)

7.[Content Grabber](https://hevodata.com/learn/8-best-web-scraping-tools/#ContentGrabber)

8.[Common Crawl](https://hevodata.com/learn/8-best-web-scraping-tools/#CommonCrawl)

# Python For Web Scraping

Though there are many other programming languages, but python is being used by most developers for scraping with variety of libraries that are created specially for Web Scraping.

### Frameworks used for web Scraping

1.[Scrapy](https://scrapy.org/) is open source and collaborative framework for extracting the data you need from websites. In a fast, simple, yet extensible way.

![scrapy](https://user-images.githubusercontent.com/95229816/152689575-efdcc915-a946-4f6e-bc72-07ee11ef96ee.png)

pip install the below command to install necessary libraries for web scrap

```python
pip install scrapy
```

And import the scrapy by 

```python
import scrapy
```

Deploying to [zyte scrapy cloud](https://www.zyte.com/scrapy-cloud/):

```python
pip install shub
shub login
shub deploy
shub schedule blogspider
```

Build and run your [web spiders](https://towardsdatascience.com/how-to-scrape-the-web-using-python-with-scrapy-spiders-e2328ac4526) for web scraping.



2.[Beautifulsoup4](https://pypi.org/project/beautifulsoup4/) is another free and open source framework library that makes it easy to scrape information from web pages.

![beautifulsoup](https://user-images.githubusercontent.com/95229816/152691374-4adc7bf5-2d91-41c9-947d-a393e5162713.png)

pip install the below command to install necessary libraries for web scrap

```python
pip install beautifulsoup4
```

And import the beautifulsoup4 by

```python
from bs4 import beautifulsoup
```

About [PARSER](https://webscraper.io/documentation/web-scraper-cloud/parser#:~:text=Parser%20is%20a%20feature%20which,manually%20in%20a%20spreadsheet%20software.&text=If%20parser%20is%20set%2C%20data%20will%20always%20be%20parsed%20when%20downloaded.)

Installing parser for bs4

```python
pip install lxml
```

### What is Web Scrapig used for?

1. Price Monitoring
2. Market Research
3. News Monitoring
4. Sentiment Analysis
5. Email Marketing

<p align = "center"><img height = "300" width = "500" src = "https://user-images.githubusercontent.com/95229816/152691713-239b294d-8a1e-4ddf-a1f7-270c2db8dfe7.png"></p>

<p align = "center">(images and other source : google.com)</p>

<h3>If any necessary commits are required to increase the elegance of this repo! i'm always open for a PR.</h3>

If you are not satisfied with this information you can check out [WEB SCRAPER](https://webscraper.io/)

### <h2>With this signing off..!!,BHARATH GUNTREDDI ..🤞</h2>
