import urllib.request
import os
import pandas as pd
import time

if not os.path.exists("deep_link_html"):
    os.mkdir("deep_link_html")

base_url = "http://coinmarketcap.com"
df = pd.read_csv("parsed_files/coinmarketcap_dataset.csv")
#Could also loop like this:
# for link in df['link']:
#     print(base_url + link)
#
#Doing this for practice
for row in df.itertuples():
    currencyLink = base_url + row.link
    # currencyName = currencyLink[currencyLink.find("currencies/") + 11 : -1]
    currencyName = currencyLink.replace(base_url, "").replace("currencies/", "").replace("/", "")
    fileName = "deep_link_html/" + currencyName + ".html"
    if not os.path.exists(fileName):
        response = urllib.request.urlopen(currencyLink)
        html = response.read()
        with open(fileName + ".temp", "wb") as currencyFile:
            currencyFile.write(html)
        currencyFile.close()
        os.rename(fileName + ".temp", fileName)
        print("Wrote to :", fileName)
        time.sleep(20)
    else:
        print(fileName + " exists")
