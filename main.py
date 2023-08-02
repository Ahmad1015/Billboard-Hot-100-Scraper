from bs4 import BeautifulSoup

def getting_user_input():
    year = input("Enter Year: ")
    month = input("Enter Month: ")
    # Handling if User inputs month names instead of numbers
    months_dict = {
        "January": '01',
        "February": '02',
        "March": '03',
        "April": '04',
        "May": '05',
        "June": '06',
        "July": '07',
        "August": '08',
        "September": '09',
        "October": 10,
        "November": 11,
        "December": 12
    }
    try:
        month = int(month)
        month = "0"+str(month)
    except TypeError:
        month = months_dict[month]
    day = input("Enter Day: ")
    return f"https://www.billboard.com/charts/hot-100/{year}-{month}-{day}/"

def billboard(user_input):
   pass


def main():
    user_input = getting_user_input()
    billboard(user_input)

if __name__ == "__main__":
    main()