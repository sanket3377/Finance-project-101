import requests
from bs4 import BeautifulSoup
BASE_URL = "https://www.screener.in"

def search_company(company_name):
    if company_name == "None":
        return None
    headers = {
    "User-Agent": "Mozilla/5.0"
}

    url = f"https://www.screener.in/{company_name}/consolidated/"

    response = requests.get(
    url,
    headers=headers,
    timeout=20
)
    companies = response

    if response.status_code != 200:
        return None

    print("Company searched:", company_name)
    print("Results:", companies)
    return url

    

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