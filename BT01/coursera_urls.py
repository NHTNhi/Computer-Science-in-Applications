import xml.etree.ElementTree as ET
import requests

r = requests.get('https://www.coursera.org/sitemap~www~courses.xml')
root = ET.fromstring(r.text)

f = open('coursera_urls.txt', 'w')
for url_tag in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
    url = url_tag[0].text
    f.write(f'{url}\n')
f.close()