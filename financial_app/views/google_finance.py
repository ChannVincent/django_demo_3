import requests
from django.http import HttpResponse

rapid_api_key = "df54535147msh0db5d0d6390a581p1e580cjsn039b8b7786a3"
rapid_api_host = "google-finance4.p.rapidapi.com"
base_url = "https://" + rapid_api_host + "/"

def ticker(request, ticker):
    url = base_url + "ticker/"
    query = {
        "t":ticker,
        "hl":"en",
        "gl":"US"
    }
    headers = {
        "X-RapidAPI-Key": rapid_api_key,
        "X-RapidAPI-Host": rapid_api_host,
    }
    response = requests.request("GET", url, headers=headers, params=query)
    return HttpResponse(response.text)


def search(request, needle):
    url = base_url + "search/"
    query = {
        "q":needle,
        "hl":"en",
        "gl":"US"
    }
    headers = {
        "X-RapidAPI-Key": rapid_api_key,
        "X-RapidAPI-Host": rapid_api_host,
    }
    response = requests.request("GET", url, headers=headers, params=query)
    return HttpResponse(response.text)