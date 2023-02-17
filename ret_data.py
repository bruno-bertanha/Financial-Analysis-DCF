"""
This code will use the free version of the FMP API to get the data for the analysis.
Data provided by Financial Modeling Prep (https://financialmodelingprep.com/developer/docs/)

"""

#IMPORTS
import json
from urllib.request import urlopen

#FUNCTIONS
def get_api_key():
    """
    Get the API key from the file 'api_key.txt'.
    """
    with open("api_key.txt", "r") as f:
        api_key = f.read()
    return api_key

def api_url_request(data_type, ticker, apikey):
    """
    Create the url for the request.
    args:
    data_type: the type of data to request. Can be 'profile', 'income-statement', 'balance-sheet-statement', 'cash-flow-statement', 'key-metrics', 'enterprise-value', 'rating', 'discounted-cash-flow', 'financial-statement-growth', 'financial-ratios'
    ticker: the ticker of the company.
    apikey: the api key to use.
    """
    url = f'https://financialmodelingprep.com/api/v3/{data_type}/{ticker}?apikey={apikey}'
    return url


def get_jsonparsed_data(url):
    """
    Fetch url, return parsed json. 
    args:
        url: the url to fetch.
    
    returns:
        parsed json
    """
    try: response = urlopen(url)
    except Exception as e:
        print(f"Error retrieving {url}:")
        try: print("\t%s"%e.read().decode())
        except: pass
        raise
    data = response.read().decode('utf-8')
    json_data = json.loads(data)
    if "Error Message" in json_data:
        raise ValueError("Error while requesting data from '{url}'. Error Message: '{err_msg}'.".format(
            url=url, err_msg=json_data["Error Message"]))
    return json_data

def ev(ticker):
    url = api_url_request("enterprise-value", ticker, get_api_key())
    return get_jsonparsed_data(url)

def income(ticker):
    url = api_url_request("income-statement", ticker, get_api_key())
    return get_jsonparsed_data(url)

def balance(ticker):
    url = api_url_request("balance-sheet-statement", ticker, get_api_key())
    return get_jsonparsed_data(url)

def cashflow(ticker):
    url = api_url_request("cash-flow-statement", ticker, get_api_key())
    return get_jsonparsed_data(url)

def keymetrics(ticker):
    url = api_url_request("key-metrics", ticker, get_api_key())
    return get_jsonparsed_data(url)

def stock_price(ticker):
    url = api_url_request("quote-short", ticker, get_api_key())
    return get_jsonparsed_data(url)


