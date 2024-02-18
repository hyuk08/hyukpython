import requests
from bs4 import BeautifulSoup
import json


res = requests.get('https://s.search.naver.com/p/image/46/search.naver?ac=0\u0026aq=0\u0026display=100\u0026json_type=6\u0026mode=\u0026nlu_query=%7B%22r_category%22%3A%2212\u002b7%22%7D\u0026nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22people_star%22%2C%22os%22%3A%22159229%22%2C%22pkid%22%3A%221%22%7D%7D%7D\u0026nso=so%3Ar%2Cp%3Aall%2Ca%3Aall\u0026nx_search_query=%EC%95%84%EC%9D%B4%EC%9C%A0\u0026query=%EC%95%84%EC%9D%B4%EC%9C%A0\u0026section=image\u0026spq=1\u0026where=image')


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