from turtle import end_poly
import requests
from django.http import HttpResponse

# https://rapidapi.com/asepscareer/api/yahoo-finance97/

rapid_api_key = "df54535147msh0db5d0d6390a581p1e580cjsn039b8b7786a3"
rapid_api_host = "yahoo-finance97.p.rapidapi.com"
base_url = "https://" + rapid_api_host + "/"

def headers():
    return {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": rapid_api_key,
        "X-RapidAPI-Host": rapid_api_host,
    }


def yahoo_finance_api_call(request, yahoo_finance_model):
    url = base_url + yahoo_finance_model["end_point"]
    payload = ""
    for key, value in yahoo_finance_model["params"].items():
        if payload:
            payload = payload + "&"
        payload = payload + key + "=" + value
    response = requests.request(
        yahoo_finance_model["request_type"], 
        url, 
        data=payload, 
        headers=headers()
    )
    # return HttpResponse(response.text)
    return response.text
    

def ticker(request, ticker):
    yahoo_finance_model = {
        "end_point": "stock-info",
        "request_type": "POST",
        "params": {
            "symbol": ticker
        }
    }
    return yahoo_finance_api_call(request, yahoo_finance_model)


def prices(request, ticker, start, end):
    yahoo_finance_model = {
        "end_point": "price-customdate",
        "request_type": "POST",
        "params": {
            "symbol": ticker,
            "start": start, # 2022-01-01
            "end": end # 2022-04-30
        }
    }
    return yahoo_finance_api_call(request, yahoo_finance_model)


def dividends(request, ticker):
    yahoo_finance_model = {
        "end_point": "dividends",
        "request_type": "POST",
        "params": {
            "symbol": ticker
        }
    }
    return yahoo_finance_api_call(request, yahoo_finance_model)


def earnings(request, ticker):
    yahoo_finance_model = {
        "end_point": "earnings",
        "request_type": "POST",
        "params": {
            "symbol": ticker
        }
    }
    return yahoo_finance_api_call(request, yahoo_finance_model)


def quarterly_earnings(request, ticker):
    yahoo_finance_model = {
        "end_point": "quarterly-earnings",
        "request_type": "POST",
        "params": {
            "symbol": ticker
        }
    }
    return yahoo_finance_api_call(request, yahoo_finance_model)


def analyst_recommendations(request, ticker):
    yahoo_finance_model = {
        "end_point": "recommendations",
        "request_type": "POST",
        "params": {
            "symbol": ticker
        }
    }
    return yahoo_finance_api_call(request, yahoo_finance_model)


def news(request, ticker):
    yahoo_finance_model = {
        "end_point": "news",
        "request_type": "POST",
        "params": {
            "symbol": ticker
        }
    }
    return yahoo_finance_api_call(request, yahoo_finance_model)