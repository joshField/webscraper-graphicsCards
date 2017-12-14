from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.com/Product/ProductList.aspx?Submit=StoreIM&Depa=1&Category=38"

# opening up connection, grabbing page
uClient =  uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each product
containers = page_soup.findAll("div",{"class":"item-container"})

filename = "graphicscards.csv"
f = open(filename, "w")
headers = "brand, product_name, price, shipping\n"
f.write(headers)


for container in containers:
    # gets the brand name
    brand = container.div.div.img["title"]

    # gets the title of the card
    title_container = container.findAll("a",{"class":"item-title"})
    product_name = title_container[0].text

    # gets the price of the card
    price_container = container.findAll("li", {"class":"price-current"})
    price_string = price_container[0].text.strip()
    price = price_string[3:9]

    # gets the shipping cost of the card
    shipping_container = container.findAll("li", {"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    print("brand: " + brand)
    print("product_name: " + product_name)
    print("price: " + price)
    print("shipping: " + shipping)

    # puts data into each column
    f.write(brand.replace(",", "|") + "," + product_name.replace(",", "|") + "," + price + "," + shipping + "\n")

f.close()
