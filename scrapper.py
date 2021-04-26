import requests
from bs4 import BeautifulSoup

oyo_url="https://www.oyorooms.com/search?location=Bangalore%2C%20Karnataka%2C%20India&city=Bangalore&searchType=city&checkin=25%2F04%2F2021&checkout=26%2F04%2F2021&roomConfig%5B%5D=2&guests=2&rooms=1&filters%5Bcity_id%5D=4"

req = requests.get(oyo_url)
content=req.content
soup = BeautifulSoup(content, "html.parser")
all_hotels = soup.find_all("div",{"class":"hotelCardListing"})

for hotel in all_hotels:
    hotel_name = hotel.find("h3",{"class":"listingHotelDescription__hotelName"}).text
    hotel_address = hotel.find("span",{"itemprop":"streetAddress"}).text
    print(hotel_name,hotel_address)
