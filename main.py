import sys
from bs4 import BeautifulSoup
import requests
import os
from dotenv import find_dotenv,load_dotenv

def getting_user_input():
    '''year = input("Enter Year: ")
    month = input("Enter Month: ")
    # Handling if User inputs month names instead of numbers
    months_dict = {
        "january": '01',
        "february": '02',
        "march": '03',
        "april": '04',
        "may": '05',
        "june": '06',
        "july": '07',
        "august": '08',
        "september": '09',
        "october": 10,
        "november": 11,
        "december": 12
    }
    try:
        month = int(month)
        month = "0"+str(month)
    except ValueError:
        month = months_dict[month.lower()]
    day = int(input("Enter Day: "))
    if day<10 and day>-1:
        day = "0"+str(day)
    elif day >=0 and day >28 and month == "02":
        if day == 29:
            if not (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                sys.exit("Incorrect Data entered")
            elif day>29:
                sys.exit("Incorrect Data entered")
    elif not (day >=10 and day <31):
        sys.exit("Incorrect Data entered")'''
    day = "01"
    month="01"
    year = "2009"
    return f"https://www.billboard.com/charts/hot-100/{year}-{month}-{day}/"

def billboard(user_input):
    try:
       response = requests.get(user_input)
       response.raise_for_status()
       web_page = response.text
       soup = BeautifulSoup(web_page,"html.parser")
       names_list = []
       for e in soup.find_all(class_= 'o-chart-results-list-row-container'):
            names_list.append(e.h3.get_text().strip())
       spotify()
    except:
        print(f"Unexpected Error Occured - Status = {response.status_code}")


def spotify():
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)
    client_id = os.getenv("spotifyclient_id")
    client_secret = os.getenv("spotifyclient_secret")





def main():
    user_input = getting_user_input()
    billboard(user_input)

if __name__ == "__main__":
    main()