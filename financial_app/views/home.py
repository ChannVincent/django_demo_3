from genericpath import exists
from django.shortcuts import render
from django.http import HttpResponse
import json
from datetime import date, datetime
from financial_app.models.enterprise import Dividend, Enterprise, Share
from . import google_finance, yahoo_finance, investing_finance


def home(request):
    response = {
        'id': 1,
        'status': 'success'
    }
    return HttpResponse(json.dumps(response), content_type="application/json")


def enterprise(request, ticker):
    finance = json.loads(yahoo_finance.ticker(request, ticker))
    data = finance["data"]
    if not data:
        return HttpResponse("no data")
    try:
        enterprise = Enterprise.objects.get(ticker=data["symbol"])
        enterprise.name=data["longName"]
        enterprise.description=data["longBusinessSummary"]
        enterprise.sector=data["sector"]
        enterprise.website=data["website"]
        enterprise.logo_url=data["logo_url"]
        enterprise.share_count=data["sharesOutstanding"]
        enterprise.save()
        return HttpResponse("success udapte")
    except Enterprise.DoesNotExist:
        enterprise = Enterprise(
            name=data["longName"],
            ticker=data["symbol"],
            description=data["longBusinessSummary"],
            sector=data["sector"],
            website=data["website"],
            logo_url=data["logo_url"],
            share_count=data["sharesOutstanding"],
        )
        enterprise.save()
        return HttpResponse("success create")


def dividends(request, ticker):
    finance = json.loads(yahoo_finance.dividends(request, ticker))
    data = finance["data"]
    if not data:
        return HttpResponse("no data")
    try:
        enterprise = Enterprise.objects.get(ticker=ticker)
        for dividend in data:
            timestamp = dividend["Date"]
            try:
                d = Dividend.objects.get(
                    enterprise=enterprise,
                    date=datetime.utcfromtimestamp(timestamp/1000)
                )
                d.price = dividend["Dividends"]
                d.save()
            except Dividend.DoesNotExist:
                d = Dividend(
                    enterprise=enterprise,
                    date=datetime.utcfromtimestamp(timestamp/1000),
                    price=dividend["Dividends"]
                )
                d.save()
        return HttpResponse("success create")
    except Enterprise.DoesNotExist:
        return HttpResponse("no enterprise")

    
def shares(request, ticker):
    current_date = date.today().strftime("%Y-%m-%d")
    finance = json.loads(yahoo_finance.prices(request, ticker, "2022-01-01", current_date))
    data = finance["data"]
    if not data:
        return HttpResponse("no data")
    try:
        enterprise = Enterprise.objects.get(ticker=ticker)
        for share in data:
            timestamp = share["Date"]
            try:
                s = Share.objects.get(
                    enterprise=enterprise,
                    date=datetime.utcfromtimestamp(timestamp/1000)
                )
                s.price = share["Close"]
                s.volume = share["Volume"]
                s.save()
            except Share.DoesNotExist:
                s = Share(
                    enterprise=enterprise,
                    date=datetime.utcfromtimestamp(timestamp/1000),
                    price=share["Close"],
                    volume=share["Volume"],
                )
                s.save()
        return HttpResponse("success create")
    except Enterprise.DoesNotExist:
        return HttpResponse("no enterprise")