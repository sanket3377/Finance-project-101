import requests
from bs4 import BeautifulSoup
BASE_URL = "https://www.screener.in"

def search_company(company_name):
    if not company_name:
        return None

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        f"{BASE_URL}/api/company/search/",
        params={"q": company_name},
        headers=headers,
        timeout=20
    )

    if response.status_code != 200:
        return None

    companies = response.json()

    print("Search results:", companies)   # Debug

    if not companies:
        return None

    # Look for an exact name match first
    for company in companies:
        if company["name"].strip().lower() == company_name.strip().lower():
            return BASE_URL + company["url"]

    # Otherwise return the first result
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