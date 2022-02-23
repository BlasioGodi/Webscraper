
# import module
from array import array
import csv
import requests
import pandas as pd
import xlsxwriter
from bs4 import BeautifulSoup

# f = open('C:/Users/user/Desktop/FX Calendar Info/Reserve Bank of Australia/RBA Calendar.csv', 'w', newline='')
# writer = csv.writer(f)
  
# link for extract html data
def getdata(url):
    r = requests.get(url)
    return r.text
  
htmldata = getdata("https://www.ecb.europa.eu/press/calendars/mgcgc/html/index.en.html")
soup = BeautifulSoup(htmldata, 'html.parser')
extrasoup = soup.find_all("dl")
df = pd.DataFrame(columns=['cell'])
data = ''

for data in extrasoup:
    print(data.get_text())
    array = [data.get_text()]
    print(array)

  




