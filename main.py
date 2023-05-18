from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="C:/Users/deepa/Downloads/virus.ico",
        timeout=10
    )


def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
    while True:
        myHtmlData = getData('https://www.mohfw.gov.in/')

        soup = BeautifulSoup(myHtmlData, 'html.parser')
        tbody_elements = soup.find_all('tbody')

        if len(tbody_elements) > 1:
            myDataStr = ""
            for tr in tbody_elements[1].find_all('tr'):
                myDataStr += tr.get_text()
            myDataStr = myDataStr[1:]
            itemList = myDataStr.split("\n\n")

            states = ['Chandigarh', 'Telangana', 'Uttar Pradesh']
            for item in itemList:
                dataList = item.split('\n')
                if dataList[1] in states:
                    nTitle = 'Cases of Covid-19'
                    nText = f"State {dataList[1]}\nIndian: {dataList[2]} & Foreign: {dataList[3]}\nCured: {dataList[4]}\nDeaths: {dataList[5]}"
                    notifyMe(nTitle, nText)
                    time.sleep(2)
        else:
            print("Unable to find the desired data.")

        time.sleep(3600)
