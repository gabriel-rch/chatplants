import requests
import bs4
import re
from services.ecocrop_services import (
    scrape_description_table,
    scrape_ecology_table,
    scrape_cultivation_table,
    scrape_uses_table,
)

ECOCROP_URL = "https://ecocrop.apps.fao.org/ecocrop/srv/en"


def search_plant(name: str) -> dict:
    """
    Search for a plant by its name using the ECOCROP website.
    """
    response = requests.get(
        f"{ECOCROP_URL}/cropListDetails",
        params={"relation": "matches", "name": name, "quantity": 1},
    )

    soup = bs4.BeautifulSoup(response.content, "html.parser")
    service_link = soup.find("a", {"class": "serviceLink"})
    if not service_link:
        # Plant not found
        raise ValueError(f"Plant '{name}' not found in ECOCROP database.")

    # Regex pattern to extract the ID from either href or onclick attributes
    # Try to find ID in href attribute
    id_pattern = r"id=(\d+)"
    id_match = re.search(id_pattern, service_link.get("href", ""))
    id = id_match.group(1) if id_match else None

    response = requests.get(f"{ECOCROP_URL}/dataSheet?id={id}")
    soup = bs4.BeautifulSoup(response.content, "html.parser")

    plant_data = {}
    for table in soup.find_all("table"):
        first_row: bs4.Tag = table.find("tr")

        # Single-header tables
        if len(first_row.find_all("th")) == 1:
            header = first_row.find("th").get_text(strip=True)
            if header == "Description":
                description = scrape_description_table(table)
                plant_data.update(description)
            elif header == "Ecology":
                ecology = scrape_ecology_table(table)
                plant_data.update(ecology)
            elif header == "Cultivation":
                cultivation = scrape_cultivation_table(table)
                plant_data.update(cultivation)
            elif header == "Uses":
                uses = scrape_uses_table(table)
                plant_data.update(uses)
        else:
            # Special table without a header
            # Scrapes the same way as the description table
            plant_data.update(scrape_description_table(table))

    return plant_data
