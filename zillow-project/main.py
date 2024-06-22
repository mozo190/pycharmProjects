import os

import requests

research_link = os.environ.get('RESEARCH_LINK')
zillow_link = os.environ.get('ZILLOW_ClONE')

response = requests.get(research_link)
yc_web_page = response.text
print(yc_web_page)
