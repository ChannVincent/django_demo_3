from django.urls import path
from django.urls.resolvers import URLPattern
from .views import home, google_finance, yahoo_finance, investing_finance

urlpatterns = [
    path("", home.home, name="finance_home"),
    path("enterprise/<ticker>/", home.enterprise, name="enterprise_info"),
    path("dividends/<ticker>/", home.dividends, name="enterprise_dividends"),
    path("shares/<ticker>/", home.shares, name="enterprise_shares"),

    path("finance/google/ticker/<ticker>/", google_finance.ticker, name="google_finance_ticker"),
    path("finance/google/search/<needle>/", google_finance.search, name="google_finance_search"), 

    path("finance/yahoo/ticker/<ticker>/", yahoo_finance.ticker, name="yahoo_finance_ticker"),
    path("finance/yahoo/prices/<ticker>/<start>/<end>/", yahoo_finance.prices, name="yahoo_finance_price"),
    path("finance/yahoo/dividends/<ticker>/", yahoo_finance.dividends, name="yahoo_finance_dividends"),
    path("finance/yahoo/earnings/<ticker>/", yahoo_finance.earnings, name="yahoo_finance_earnings"),
    path("finance/yahoo/quarterly_earnings/<ticker>/", yahoo_finance.quarterly_earnings, name="yahoo_finance_quarterly_earnings"),
    path("finance/yahoo/analyst_recommendations/<ticker>/", yahoo_finance.analyst_recommendations, name="yahoo_finance_analyst_recommendations"),
    path("finance/yahoo/news/<ticker>/", yahoo_finance.news, name="yahoo_finance_news"),

    path("finance/investing/popular_markets/", investing_finance.popular_markets, name="investing_finance_popular_markets"),
    path("finance/investing/dividends/<ticker>/", investing_finance.dividends, name="investing_finance_dividends"),
    path("finance/investing/test/<ticker>/", investing_finance.test, name="investing_finance_test"),
]