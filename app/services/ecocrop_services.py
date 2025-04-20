# Services for the web scraping of Ecocrop data
import bs4


def parse_key(key: str) -> str:
    """
    Parse the key to a more readable format.
    """
    # Remove leading and trailing whitespace
    key = key.strip()
    # Remove dots and commas
    key = key.replace(".", "").replace(",", "")
    # Remove special characters
    key = key.replace("(", "").replace(")", "")
    # Replace spaces with underscores
    key = key.replace(" ", "_")
    # Convert to lowercase
    key = key.lower()

    return key


def scrape_description_table(table: bs4.Tag) -> dict:
    return {
        parse_key(th.text): td.text.strip()
        for row in table.find_all("tr")[1:]
        for th, td in zip(row.find_all("th"), row.find_all("td"))
    }


def scrape_ecology_table(table: bs4.Tag) -> dict:
    data = {}
    for row in table.find_all("tr")[2:]:
        headers: bs4.Tag = row.find_all("th")
        # Soil depth or Light intensity
        if len(headers) == 1:
            header = headers[0].text.strip()
            if "Soil depth" in header:
                data["soil_depth"] = {
                    "optimal": row.find_all("td")[-2].text.strip(),
                    "absolute": row.find_all("td")[-1].text.strip(),
                }
            elif "Light intensity" in header:
                data["light_intensity"] = {
                    "optimal": {
                        "min": row.find_all("td")[0].text.strip(),
                        "max": row.find_all("td")[1].text.strip(),
                    },
                    "absolute": {
                        "min": row.find_all("td")[2].text.strip(),
                        "max": row.find_all("td")[3].text.strip(),
                    },
                }

        # All other rows have two headers
        # The first header has four values:
        #   (optimnal min, optimal max, absolute min, absolute max)
        # The second header has two values:
        #   (optimal, absolute)
        elif len(headers) == 2:
            first_header = parse_key(headers[0].text.strip())
            second_header = parse_key(headers[1].text.strip())

            data[first_header] = {
                "optimal": {
                    "min": row.find_all("td")[0].text.strip(),
                    "max": row.find_all("td")[1].text.strip(),
                },
                "absolute": {
                    "min": row.find_all("td")[2].text.strip(),
                    "max": row.find_all("td")[3].text.strip(),
                },
            }

            data[second_header] = {
                "optimal": row.find_all("td")[4].text.strip(),
                "absolute": row.find_all("td")[5].text.strip(),
            }

        else:
            # Skip rows with more than two headers
            continue

    return data


def scrape_cultivation_table(table: bs4.Tag) -> dict:
    # Only interested in crop cycle
    for row in table.find_all("tr")[1:]:
        for header in row.find_all("th"):
            if "Crop cycle" in header.text:
                return {
                    "crop_cycle": {
                        "min": row.find_all("td")[-2].text.strip(),
                        "max": row.find_all("td")[-1].text.strip(),
                    }
                }
    return {}


def scrape_uses_table(table: bs4.Tag) -> dict:
    rows = table.find_all("tr")[2:]
    uses = []
    for row in rows:
        cells = row.find_all("td")
        if len(cells) == 3:
            uses.append(
                {
                    "main_use": cells[0].text.strip(),
                    "detailed_use": cells[1].text.strip(),
                    "used_part": cells[2].text.strip(),
                }
            )

    return {"uses": uses}
