# https://rapidapi.com/asepscareer/api/investing4/

import requests
from django.http import HttpResponse

rapid_api_key = "df54535147msh0db5d0d6390a581p1e580cjsn039b8b7786a3"
rapid_api_host = "investing4.p.rapidapi.com"
base_url = "https://" + rapid_api_host + "/"

def headers():
    return {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": rapid_api_key,
        "X-RapidAPI-Host": rapid_api_host,
    }


def investing_finance_api_call(request, investing_finance_model):
    url = base_url + investing_finance_model["end_point"]
    payload = ""
    for key, value in investing_finance_model["params"].items():
        if payload:
            payload = payload + "&"
        payload = payload + key + "=" + value
    response = requests.request(
        investing_finance_model["request_type"], 
        url, 
        data=payload, 
        headers=headers()
    )
    return HttpResponse(response.text)


def popular_markets(request):
    investing_finance_model = {
        "end_point": "main/popular-markets",
        "request_type": "GET",
        "params": {
        }
    }
    return investing_finance_api_call(request, investing_finance_model)


def historical_data(request, ticker):
    investing_finance_model = {
        "end_point": "stocks/historical-data",
        "request_type": "POST",
        "params": {
            "name": ticker,
            "from_date": "01%2F03%2F2021",
            "to_date": "04%2F03%2F2022",
            "interval": "Daily",
            "country": "United%20States"
        }
    }
    return investing_finance_api_call(request, investing_finance_model)
    

def dividends(request, ticker):
    investing_finance_model = {
        "end_point": "stocks/dividen",
        "request_type": "POST",
        "params": {
            "symbol": ticker,
            "country": "United%20States"
        }
    }
    return investing_finance_api_call(request, investing_finance_model)


def stock_countries(request):
    investing_finance_model = {
        "end_point": "stocks/get-stock-countries",
        "request_type": "GET",
        "params": {
        }
    }
    return investing_finance_api_call(request, investing_finance_model)


def test(request, ticker):
    investing_finance_model = {
        "end_point": "economic-calendar",
        "request_type": "POST",
        "params": {
            "symbol": ticker,
            "country": "United%20States"
        }
    }
    return investing_finance_api_call(request, investing_finance_model)