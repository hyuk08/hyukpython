import requests
from bs4 import BeautifulSoup
import json


res = requests.get('')


soup = BeautifulSoup(res.text, 'html.parser')


hdline_titles = soup.select('.tile_item ._fe_image_tab_content_tile')
# print(hdline_titles)
# exit()

json_data = json.loads(soup.text)

print(json_data)

# for item in json_data["items"]:
#     print(item["title"])
#     print(item["viewerThumb"] )
#     print('')