import pandas as pd
from bs4 import *
import  requests
page = requests.get("https://forecast.weather.gov/MapClick.php?"
                    "lat=33.93680995224785&lon=-118.24891999999994#.XuFT02gzbIU")
soup = BeautifulSoup(page.content,"html.parser")
week = soup.find_all(id = "seven-day-forecast-body")
#print(week)
clas = soup.find_all(class_ = "tombstone-container")
print(clas[0].find(class_="period-name").get_text())
period_names = [item.find(class_="period-name").get_text()
                for item in clas]
short_desc = [item.find(class_="short-desc").get_text()
                for item in clas]
temperature = [item.find(class_="temp").get_text()
                for item in clas]

weather_stuff  = pd.DataFrame({
    'period' : period_names ,
    'short-description' : short_desc ,
    'temperature' : temperature
})
print(weather_stuff)
weather_stuff.to_csv('weather.csv')