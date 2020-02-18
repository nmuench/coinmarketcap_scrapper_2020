import urllib.request
import os
import time
import datetime
from bs4 import BeautifulSoup

if not os.path.exists("html_files"):
    os.mkdir("html_files")
def MakeHourlyRequest():
    while True:
        coinMarketUrl = "https://coinmarketcap.com/"
        coinMarketPage = MakeRequest(coinMarketUrl)
        time.sleep(10)

def MakeRequest(urlString):
    fileName = "html_files/coinMarketPage--" + datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S") + ".html"
    marketPage = urllib.request.urlopen(urlString)
    with open(fileName, "wb") as marketFile:
        marketFile.write(marketPage.read())
    marketFile.close()
    print("Wrote to", fileName)

MakeHourlyRequest()

# fileName = "html_files/coinMarketPage--20200128163320.html"
# with open(fileName, "rb") as marketFile:
#     coinMarketHtml = marketFile.read()
# marketFile.close()
#
# marketParser = BeautifulSoup(coinMarketHtml, "html.parser")
# tableRows = marketParser.find_all("tr", class_="cmc-table-row")
#
# for tableRow in tableRows:
#     tableCells = tableRow.contents
#     currencyName = tableCells[1].contents[0].contents[1].text
#     currencyPrice = tableCells[1]
#     print(currencyPrice)
