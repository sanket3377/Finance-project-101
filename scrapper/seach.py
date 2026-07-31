import requests

BASE_URL = "https://www.screener.in"


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
        return {
            "success": False,
            "message": "Search request failed."
        }

    companies = response.json()

    if len(companies) == 0:
        return {
            "success": False,
            "message": "Company not found."
        }

    company = companies[0]

    return {
        "success": True,
        "name": company["name"],
        "url": BASE_URL + company["url"]
    }
