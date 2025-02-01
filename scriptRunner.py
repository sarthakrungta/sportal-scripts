from sqlScraper import connect_db, get_club_info
from selenium import webdriver

data_sets = [
    {
        "url": "https://www.playhq.com/cricket-australia/org/cucc-kings/6e4ab302",
        "email": "test@cucckings.com"
    },
    {
        "url": "https://www.playhq.com/cricket-australia/org/carnegie-cricket-club/df628a00",
        "email": "test@carnegie.com"
    },
    {
        "url": "https://www.playhq.com/cricket-australia/org/ashburton-willows-cricket-club/55f5bdce",
        "email": "test@ashburton.com"
    },
    {
        "url": "https://www.playhq.com/cricket-australia/org/ashburton-willows-cricket-club/55f5bdce",
        "email": "timmurphy1181@gmail.com"
    },
]

if __name__ == "__main__":
    driver = webdriver.Safari()
    for data in data_sets:
        conn = connect_db()  # Establish database connection
        get_club_info(conn, data["url"], data["email"], driver)  # Call function with each set of URL and email
        conn.close()  # Close the database connection
