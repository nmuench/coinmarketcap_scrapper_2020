import os
from bs4 import BeautifulSoup
import pandas as pd
import glob


def parseFile(fileName, df, scrapingTime):
    print("Parsing", fileName)
    marketFile = open(fileName, "rb")
    marketParser = BeautifulSoup(marketFile.read(), "html.parser")
    marketFile.close()

    currencyTableBody = marketParser.find("tbody")
    allCurrencyRows = currencyTableBody.find_all("tr")

    currencyDict = dict()



    for currencyRow in allCurrencyRows:
        currencyName = currencyRow.find("td", {"class" : "cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__name"}).find("a", {"class" : "cmc-link"}).text
        currencyPrice = currencyRow.find("td", {"class" : "cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price"}).find("a", {"class" : "cmc-link"}).text.replace(",", "").replace("$","")
        currencyMarketCap = currencyRow.find("td", {"class" : "cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__market-cap"}).text.replace(",", "").replace("$", "")
        currencySupply = currencyRow.find("td", {"class" : "cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__circulating-supply"}).find("div").text.replace(" * ", "")
        currencyAddress = currencyRow.find("td", {"class" : "cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__name"}).find("a", {"class" : "cmc-link"})["href"]
        df = df.append({
            'time' : scrapingTime,
            'name' : currencyName,
            'price' : currencyPrice,
            'marketCap' : currencyMarketCap,
            'supply' : currencySupply,
            'link' : currencyAddress
        }, ignore_index = True)

    return(df)

if not os.path.exists("parsed_files"):
    os.mkdir("parsed_files")

df = pd.DataFrame()

#htmlFiles = os.listdir
for one_file_name in glob.glob("html_files/*.html"):
    scrapingTime = os.path.basename(one_file_name).replace("coinMarketPage--", "").replace("html", "")
    df = parseFile(one_file_name, df, scrapingTime)
    df.to_csv("parsed_files/coinmarketcap_dataset.csv")
