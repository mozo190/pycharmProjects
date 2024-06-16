import mail_manager
import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/58.0.3029.110 Safari/537.3"}
response = requests.get(url, headers=headers)
web_page = response.text

soup = BeautifulSoup(web_page, "lxml")
# print(soup.prettify())
# price = soup.find(name="span", class_="a-price-whole")
product_name = soup.find(name="span", id="productTitle").get_text().strip()
price = soup.find(class_="a-offscreen").getText()
print(product_name)
print(price)

subject = "This is the new price!\n\n"
customer_name = "Dear Zoltan,"
message = f"The price of {product_name} is {price} now."
sign = "Best regards,\n\nMolnar Zoltan\nPhone: +36 309 776 039"
body = f"{customer_name}\n\n{message}\n\n{sign}"

mail_manager.send_email(subject, body)
