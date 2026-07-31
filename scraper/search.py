import requests
from bs4 import BeautifulSoup
from gemini import get_stock_json

BASE_URL = "https://www.screener.in"


def search(user_input):
    # Ask Gemini to extract the stock name
    command = get_stock_json(user_input)

    # Get the company name from the JSON
    company_name = command["stock"]

    # Use your existing function
    company_url = search_company(company_name)

    return company_url

def search_company(company_name):

    company_name = company_name.strip()

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    params = {
        "q": company_name
    }

    response = requests.get(
        f"{BASE_URL}/api/company/search/",
        params=params,
        headers=headers,
        timeout=20
    )

    if response.status_code != 200:
        return None

    companies = response.json()

    if len(companies) == 0:
        return None

    return BASE_URL + companies[0]["url"]


def get_company_soup(company_name):

    company_url = search_company(company_name)

    if company_url is None:
        return None

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        company_url,
        headers=headers,
        timeout=20
    )

    if response.status_code != 200:
        return None

    soup = BeautifulSoup(
        response.text,
        "lxml"
    )

    return soup