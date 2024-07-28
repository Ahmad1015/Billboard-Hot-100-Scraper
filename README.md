# Billboard Hot 100 Scraper
This project allows users to scrape the Billboard Hot 100 chart for a specific date and retrieve the list of song titles. The project utilizes Python, BeautifulSoup, and requests to fetch and parse the data from the Billboard website.

## Features
- User Input: Prompt the user to input a specific date (year, month, day).
- Error Handling: Ensures valid date input, including leap year validation.
- Web Scraping: Uses BeautifulSoup and requests to scrape the Billboard Hot 100 chart for the given date.
- Song Titles: Extracts and displays the list of song titles from the chart.
## Prerequisites
- Python 3.x
- BeautifulSoup4
- Requests
You can install the necessary packages using the following command:
```bash
pip install beautifulsoup4 requests
```
Usage
1. Clone the repository and navigate to it:
```bash
git clone https://github.com/Ahmad1015/Billboard-Hot-100-Scraper.git
cd Billboard-Hot-100-Scraper
```
2. Run the Script:
```python
python main.py
```
3. Enter the year, month, and day when prompted. The script will handle both numeric and named month inputs.
4. The script will fetch the Billboard Hot 100 chart for the specified date and display the list of song titles.
