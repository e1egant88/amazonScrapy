from enum import Enum

class CategoryName(Enum):
    Phone_Smart_Watches_Accessories = "Phone, Smart Watches & Accessories"
    Computer_Tablets_Networking = "Computer, Tablets & Networking"
    Video_Games_Consoles = "Video Games & Consoles"
    Electronics = "Electronics"
    Home_Entertainment = "Home Entertainment"
    Headphones_EarBuds = "Headphones & Earbuds"
    Camera = "Camera"


dic = {
    "Mobile Phones & Communication": CategoryName.Phone_Smart_Watches_Accessories.value,
    "Telephones, VoIP & Accessories": CategoryName.Phone_Smart_Watches_Accessories.value,
    "Wearable Technology": CategoryName.Phone_Smart_Watches_Accessories.value,
    "Tablets": CategoryName.Computer_Tablets_Networking.value,
    "Computers, Components & Accessories": CategoryName.Computer_Tablets_Networking.value,
    "Legacy Systems": CategoryName.Video_Games_Consoles.value,
    "Linux Games": CategoryName.Video_Games_Consoles.value,
    "Nintendo Switch": CategoryName.Video_Games_Consoles.value,
    "Online Game Services": CategoryName.Video_Games_Consoles.value,
    "PC": CategoryName.Video_Games_Consoles.value,
    "PlayStation 4": CategoryName.Video_Games_Consoles.value,
    "PlayStation 5": CategoryName.Video_Games_Consoles.value,
    "Xbox One": CategoryName.Video_Games_Consoles.value,
    "Xbox Series X & S": CategoryName.Video_Games_Consoles.value,
    "Car & Vehicle Electronics": CategoryName.Electronics.value,
    "Household Batteries & Chargers": CategoryName.Electronics.value,
    "Power Accessories": CategoryName.Electronics.value,
    "Portable Sound & Vision": CategoryName.Electronics.value,
    "Radio Communication": CategoryName.Electronics.value,
    "Sat Nav, GPS, Navigation & Accessories": CategoryName.Electronics.value,
    "TVs, Home Cinema & Video": CategoryName.Home_Entertainment.value,
    "Hi-Fi & Home Audio": CategoryName.Home_Entertainment.value,
    "Camera & Photo": CategoryName.Camera.value,
    "Headphones, Earbuds & Accessories": CategoryName.Headphones_EarBuds.value,


    "Phones, smart Watches & Accessories": CategoryName.Phone_Smart_Watches_Accessories.value,
    "Computers, Tablets & Network Hardware": CategoryName.Computer_Tablets_Networking.value,
    "Video Games & Consoles": CategoryName.Video_Games_Consoles.value,
    "Electronics": CategoryName.Electronics.value,
    "Smart Home & Surveillance Electronics": CategoryName.Electronics.value,
    "TVs": CategoryName.Electronics.value,
    "Home Entertainment": CategoryName.Home_Entertainment.value,
    "Cameras": CategoryName.Camera.value,
    "Portable Audio & Headphones": CategoryName.Headphones_EarBuds.value,
    "Smart Home & Surveillance Electronics": CategoryName.Electronics.value,
}