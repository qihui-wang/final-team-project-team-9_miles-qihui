'''
# Assignment title: Final Project- Web-scraping Weather Forecast
# Date: 10/02/2019
# Description: The script web-scrapes the weather.gov website to extract the 5-Day weather forecast for a given location
# Inputs: Latitude & Longitude in Decimal Degrees
# Outputs: 5-Day Weather Forecast
'''
# import required libraries
import requests
from bs4 import BeautifulSoup

# List to store response
forecast = []

#Ask user to provide the latitude and longitude for the location to check the weather for
## Lat/lon in decimal degrees provided for Worcester, MA
print('Please input a latitude:')
#Get the latitude and convert it to strings
lat = str(input())
#example:lat =str(42.2634)

print('Please input a longitude:')  
#Get the longitude and convert it to strings
lon =str(input()) 
#example:lon =str(-71.8022)

# Create url for the requested location through string concatenation
url = 'https://forecast.weather.gov/MapClick.php?lat='+lat+"&lon="+lon
# Check if the URL exists
# print url

# Send request to retrieve the web-page using the get() function from the requests library
# The page variable stores the response from the web-page
page = requests.get(url)

# Create a BeautifulSoup object with the response from the URL
# Access contents of the web-page using .content
# html_parser is used since our page is in HTML format
soup=BeautifulSoup(page.content,"html.parser")

# Locate elements on page to be scraped
# findAll() locates all occurrences of div tag with the given class name
# stores it in the BeautifulSoup object
weather_forecast = soup.findAll("li", {"class": "forecast-tombstone"})

# Loop through the BeautifulSoup object to extract text text from every class instance using .text
# Store results in a list

#method 1:
for i in weather_forecast:
    i = i.text
#preserve space between the words
    i=i.replace('L',' L')
    i=i.replace('C',' C')
    i=i.replace('H',' H')
    i=i.replace('N',' N')
    i=i.replace('M',' M')
    i=i.replace('A',' A')
    i=i.replace('S',' S')
    i=i.replace('P',' P')
    i=i.replace(' then',', then')
    i=i.replace(' High',', High')
    i=i.replace(' Low',', Low')
    i=i.replace('\n\n ','\n\n')
    i=i.replace('  ',' ')
#change all characters to upperclass
    i=i.upper()
    forecast.append(i)
    
# Print list to remove unicode characters
for day in forecast:
    print day
