# importing required modules
from datetime import date, timedelta, datetime
import requests

# storing api key for FinHub
api_key = "c0lb5ov48v6orbr11mgg"


class Article:
    """
    The Article class represents a news article
    """
    def __init__(self, category, article_date, headline, image, source, summary, url):
        self._category = category
        self._datetime = article_date
        self._headline = headline
        self._image = image
        self._source = source
        self._summary = summary
        self._url = url


    def get_category(self):
        """
          Gets the category of the article
          @return the category of the article as a string
          """
        return self._category


    def get_datetime(self):
        """
        Gets the datetime of the article
        @return the datetime of the article as a string
        """
        return self._datetime


    def get_headline(self):
        """
        Gets the headline of the article
        @return the headline of the article as a string
        """
        return self._headline


    def get_image(self):
        """
        Gets the image of the article
        @return a string url containing the image of the article
        """
        return self._image


    def get_url(self):
        """
         Gets a url to the article
         @return a link containing the url of the article
         """
        return self._url


    def get_source(self):
        """
        Gets the source of the article
        @return the source of the article as a string
        """
        return self._source


    def get_summary(self):
        """
        Gets a summary of the article
        @return a summary of the article as a string
        """
        return self._summary


class News:
    """
    The News class represents the latest news for a particular stock within a 3 day period
    @param ticker is the ticker symbol of the Stock to find news for
    """
    def __init__(self, ticker):
        self._ticker = ticker
        self._articles = []
        self._max_articles = 10

    def get_news(self):
        """
        Gets a list of the company news articles for a particular stock within a 3 day period and store it in the news list
        @return a list of company  news articles
        """
        end_date = date.today()  # the end date is the last day to get upto date news from
        start_date = end_date - timedelta(3)  # the start date is the starting date to get news from

        # converting the end_date and start_date into strings so we can use an api call to FinHub to get the latest news within the time period
        end_date = end_date.strftime("%Y-%m-%d")
        start_date = start_date.strftime("%Y-%m-%d")

        # use a request call from Finhub to obtain a list of dictionaries containing company news of a stock
        news = requests.get(
            'https://finnhub.io/api/v1/company-news?symbol=' + self._ticker + '&from=' + start_date + '&to=' + end_date + '&token=' + api_key).json()

        # go through the list of dictionaries and store news articles up till the max articles
        for x in range(self._max_articles):
            # get all article info from dictionary
            current_news = news[x]
            headline = current_news["headline"]
            article_date = datetime.utcfromtimestamp(int(current_news ["datetime"])).strftime("%Y-%m-%d")
            category = current_news["category"]
            image = current_news["image"]
            source = current_news["source"]
            summary = current_news["summary"]
            url = current_news["url"]

            # create new article with the needed attributes obtained from FinHub api
            article = Article(category, article_date, headline, image, source, summary, url)
            # store the created article into the list of news
            self._articles.append(article)


        # returning the list containing company news articles
        return self._articles


    def news_to_string(self):
        """
        Gets a list of the company news articles for a particular stock within a 3 day period and store it in the news list
        @return a list of company  news articles
        """
        news_string = "News for " + self._ticker + ' Stock\n'
        i = 0
        for article in self._articles:
            i += 1
            news_string = news_string + "\nArticle " + str(i) + ":\n" + " Headline: " + article.get_headline() + "\n Date: " + article.get_datetime() +  \
                          "\n Category: " + article.get_category() + "\n Source: " + article.get_source() + "\n URL: " + article.get_url() \
                          + "\n Image: " + article.get_image() + "\n Summary: " + article.get_summary()

        return news_string




n1 = News("AAPL")
j = n1.get_news()

print(n1.news_to_string())
