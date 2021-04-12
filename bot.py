# Do not write this
from bs4 import BeautifulSoup
from selenium.webdriver import Firefox

driver = Firefox()
driver.get("https://www.amazon.ca/s?k=seeds&ref=nb_sb_noss_2")
content = driver.page_source
driver.quit()
print(content)

# Next Week Material
soup = BeautifulSoup(content, "html.parser")
products = soup.findAll("h2", {"class": "a-size-mini a-spacing-none a-color-base s-line-clamp-4"})

for product in products:
    print(product.text)

input()
