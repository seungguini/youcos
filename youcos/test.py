from dotenv import load_dotenv
import os
import time
from scrape_youtube import comments_to_csv, request_videos, request_comments, scrape_comments

def main():
    load_dotenv()
    
    # Authenticate wit h YouTube API
    KEY = os.environ.get('API_KEY')
    
    
    #q = "coronavirus|covid%7C19|pandemic|vaccine"
    q="bts"
    month=str(7)
    year=str(2020)
    for day in range(1,31):
        driver_path = "C:/WebDriver/bin/chromedriver.exe"
        #csv_path = "./data/covid_2020_dec/" + 'covid' + "_2020_12_" + str(i) + ".csv"
        csv_path = "./data/" + q + "_" + year + "_" + month + "/" + q + "_" + year + "_" + month + "_" + str(day) + ".csv"
        publishedAfter = year + "-" + month + "-" + str(day) + "T00:00:00.00-05:00"  # March 2nd, 9:30AM
        publishedBefore = year + "-" + month + "-" + str(day+1) + "T00:00:00.00-05:00"
        print("scraping ", q)
        start = time.time()
        comments_to_csv(query=q, API_KEY=KEY, publishedBefore=publishedBefore, publishedAfter=publishedAfter,csv_path=csv_path)
        end = time.time()
        print("time elapsed: ", end - start)
        
if __name__ == "__main__":
    main()