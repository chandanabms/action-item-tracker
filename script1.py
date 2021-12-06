import csv
import requests
from bs4 import BeautifulSoup
from csv import writer
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
urls = ['https://www.fastenal.com/product/cutting-tools-and-metalworking/general-purpose-holemaking/chucking-reamers/603315?categoryId=603315&level=3&isExpanded=true&productFamilyId=25393',
'https://www.fastenal.com/product/cutting-tools-and-metalworking/general-purpose-holemaking/chucking-reamers/603315?categoryId=603315&level=3&isExpanded=true&productFamilyId=25394',
'https://www.fastenal.com/product/cutting-tools-and-metalworking/general-purpose-holemaking/chucking-reamers/603315?categoryId=603315&level=3&isExpanded=true&productFamilyId=25396']
# response = requests.get(urls, headers=headers, timeout=5, allow_redirects = True)
for url in range(0,3):
    req = requests.get(urls[url])
    print(req)
    soup = BeautifulSoup(req.text, 'html.parser')
    # print(req.text[0])
    a=(req.status_code)
    print(a)
    product =[]
    soup = soup.find('table',class_='cb-ui-table')
    for i in soup:
        head = soup.find('tr',class_='cb-sub-header-tr').text
        print(head)
        break
with open("product.csv","w")as f:
    csv_writer=writer(f)
    csv_writer.writerow(urls)
    csv_writer.writerow(head)