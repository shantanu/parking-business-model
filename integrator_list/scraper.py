import pandas as pd
from bs4 import BeautifulSoup

print("hi")
# Load HTML file

filenames = [f"list{i}.html" for i in range(1, 18)]

# Initialize lists to store extracted data
company_names = []
company_descriptions = []
company_locations = []

for filename in filenames:
    with open(filename, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    # Extract information for each company
    company_divs = soup.find_all("div", class_="h3 mt-2")

    for company_div in company_divs[: len(company_divs) // 2]:
        company_name_tag = company_div.find("a")
        company_names.append(company_name_tag.text.strip())
        company_descriptions.append(
            company_div.parent.parent.parent.find(
                "p", class_="one-line-text"
            ).text.strip()
        )
        company_locations.append(
            company_div.parent.parent.parent.find(
                "div", class_="col pr-0 py-0 companies-links font-italic"
            ).text.strip()
        )

# Create DataFrame
df = pd.DataFrame(
    {
        "Company Name": company_names,
        "Description": company_descriptions,
        "Location": company_locations,
    }
)

print(df.head())

# Write to CSV
df.to_csv("company_info.csv", index=False)
