# from load_csv import load
# print(load("../life_expectancy_years.csv"))



import requests
# url ="https://cdn.intra.42.fr/document/document/15948/population_total.csv"
# url = "https://cdn.intra.42.fr/document/document/15949/life_expectancy_years.csv"
url = "https://cdn.intra.42.fr/document/document/15950/income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
response = requests.get(url)

if response.status_code == 200:
    with open("income_per_person_gdppercapita_ppp_inflation_adjusted.csv", 'wb') as file:
        file.write(response.content)
