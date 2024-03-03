from bs4 import BeautifulSoup
import pandas as pd
import requests


url = "https://www.nike.com/ro/w/run-in-the-rain-22odc"
source = requests.get(url= url)
models = []
prices = []

content = source.content
soup = BeautifulSoup(content, features="html.parser")

for element in soup.find_all("div", attrs={"class": "product-card__info"}):
    model = element.find("div", attrs= {"class": "product-card__title"})
    price = element.find("div", attrs= {"class": "product-price"})
    price = price.get_text().replace('RON\xa0', ' ')
    models.append(model.get_text())  # Extract model text without extra spaces
    prices.append(price)

df = pd.DataFrame({"Product Name": models, "Product Price": prices})
df.to_csv("nike-products.csv", encoding="utf-8", index=False)
