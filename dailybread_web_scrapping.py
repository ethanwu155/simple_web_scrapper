import requests
from bs4 import BeautifulSoup as bs
import datetime as d
import re

full_date = d.date.today()
string_date = str(full_date)

# format date into proper format
format_date = string_date[0:4] + '/TW/' + string_date[5:7] +'/' + string_date[8:]
daily_devo_url = "https://odb.org/" + format_date
url = "https://api.experience.odb.org/devotionals/podcast/?country=TW"
r = requests.get(url)

soup = bs(r.content, 'lxml')
devotional = soup.find('description').text
# print(devotional)

TAG_RE = re.compile(r']]>')
content = TAG_RE.sub('', devotional)
print(content)