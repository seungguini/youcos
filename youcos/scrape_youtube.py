from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
import time
import csv

from yt_requests import yt_search, yt_comments

def comments_to_csv(query, API_KEY, maxResults=49, driver_path="C:/WebDriver/bin/chromedriver.exe", csv_path="./youtube_comments.csv", useAPI=True):
    """
    Search YouTube video and comment info based on query search results and write data to a csv file.
    If `useAPI` is set to False, `youcos` will scrape the comments for each video using Selenium.
    
    Parameters
    ----------
    query : string
        The query to search for on YouTube
    API_KEY : string
        The API key to authenticate requests to YouTube Data API v3
    maxResults : int, optional
        The maximum number of videos to scrape
    driver_path : string, optional
        The browser path for Selenium (the default is "C:/WebDriver/bin/chromedriver.exe", which is the typical location for Chrome drivers)
    csv_path : string, optional
        The file path to save csv file (the default is "../comments.csv", which saves the file in the directory above the current one)
    useAPI : boolean, optional
        If False, `youcos` scrapes comments for each video using Selenium (the default is True, which makes `youcos` use YouTube v3 API to request comments)
    """
    
    video_list = request_videos(query, API_KEY, maxResults=maxResults, driver_path=driver_path)
    
    if (useAPI):
        request_comments(video_list, API_KEY, csv_path)
    else:
        scrape_comments(video_list, driver_path, csv_path)

def request_videos(query, API_KEY, maxResults=49, driver_path="C:/WebDriver/bin/chromedriver.exe"):
    """
    Search YouTube videos based on the given query and return a list of dictionaries containing url, title, and search query.

    Parameters
    ----------
    query : string
        The query to search for on YouTube
    API_KEY : string
        The API key to authenticate requests to YouTube Data API v3
    driver_path : string, optional
        The browser path for Selenium (the default is "C:/WebDriver/bin/chromedriver.exe", which is the typical location for Chrome drivers)
    Returns
    ----------
    video_list : list of dict
        The list of collected video data, each dictionary with the video's url, title, and search query 
    Notes
    ----------
    For more info on YouTube v3 API, please visit https://developers.google.com/youtube/v3
    """
    
    video_list = yt_search(query,API_KEY,maxResults)
    
    # Check if there are no video results
    if not video_list:
        return
    
    for video in video_list:
        video['query'] = query
    return video_list

def request_comments(video_list, API_KEY, csv_path="../comments.csv"):
    """
    Request comment data using the YouTube v3 API, then write video and comment data to a csv file.

    Parameters
    ----------
    video_list : list of dict
        The list of videos to fetch comments
    API_KEY : string
        The API key to authenticate requests to YouTube Data API v3
    csv_path : string, optional
        The location to save the csv file containing comments data
    """
    
    csv_file = open(csv_path,'w', encoding="UTF-8", newline="")
    writer = csv.writer(csv_file)    
    
    writer.writerow(['query', 'url', 'title', 'upload_date', 'channel', 'views', 'likes', 'dislikes', 'comment_count', 'comment_text', 'comment_author', 'comment_date', 'comment_likes'])    

    for video in video_list:
        
        # Grab all comments for video
        comments = yt_comments(video['id'], API_KEY)
        
        # Skip video if comments are disabled
        if not comments:
            continue
        
        for comment in comments:
            youtube_dict = {}
            
            # Write scraped data to csv file
            youtube_dict['query'] = video['query']
            youtube_dict['url'] = "https://www.youtube.com/watch?v=" + video['id']
            youtube_dict['title'] = video['title']
            youtube_dict['upload_date'] = video['date']
            youtube_dict['channel'] = video['channel']
            youtube_dict['views'] = video['views']
            youtube_dict['likes'] = video['likes']
            youtube_dict['dislikes'] = video['dislikes']
            youtube_dict['comment_count'] = video['comment_count']
            youtube_dict['comment_text'] = comment['text']
            youtube_dict['comment_author'] = comment['author']
            youtube_dict['comment_date'] = comment['date']
            youtube_dict['comment_likes'] = comment['likes']
        
            writer.writerow(youtube_dict.values())
    
def scrape_comments(video_list, driver_path="C:/WebDriver/bin/chromedriver.exe", csv_path="../comments.csv"):
    """
    Scrape YouTube video and comment info using Selenium, then write data to a csv file.

    Parameters
    ----------
    video_list : list of dict
        The list of videos to scrape
    driver_path : string, optional
        The browser path for Selenium (the default is "C:/WebDriver/bin/chromedriver.exe", which is the typical location for Chrome drivers)
    csv_path : string, optional
        The location to save the csv file containing comments data
    """
    
    csv_file = open(csv_path,'w', encoding="UTF-8", newline="")
    writer = csv.writer(csv_file)    
    
    writer.writerow(['query', 'url', 'title', 'upload_date', 'channel', 'no_of_views', 'likes', 'dislikes', 'comment', 'author', 'comment_date', 'no_of_replies','upvotes'])    
    driver = webdriver.Chrome(executable_path=driver_path)

    for video in video_list:
        
        url = video['url']
        title = video['title']
        upload_date = video['date']
        query = video['query']
        
        # Scrape basic video data
        print("=" * 40)
        print("video title : ", title)
        driver.get(url)
        v_channel = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div#upload-info yt-formatted-string"))).text
        print("channel : ",v_channel)    
        v_views = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div#count span.view-count"))).text
        print("no. of views : ",v_views)
        v_timeUploaded = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div#date yt-formatted-string"))).text
        print("time uploaded : ",v_timeUploaded)
        w = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div#top-level-buttons yt-formatted-string")))
        w = driver.find_elements_by_css_selector("div#top-level-buttons yt-formatted-string")
        v_likes = w[0].text
        v_dislikes = w[1].text
        print("video has ", v_likes, "likes and ", v_dislikes, " dislikes")
        
        youtube_dict ={}
    
        print("+" * 40)
        print("Scraping child links ")
        
        # Load comments section
        driver.execute_script('window.scrollTo(0,390);')
        time.sleep(2)
        
        try:
            # Sort by top comments
            print("sorting by top comments")
            sort= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div#icon-label")))
            sort.click()
            topcomments =driver.find_element_by_xpath("""//*[@id="menu"]/a[1]/paper-item/paper-item-body/div[1]""")
            topcomments.click()
            
            # Loads more comments
            for i in range(0,5):
                driver.execute_script("window.scrollTo(0,Math.max(document.documentElement.scrollHeight,document.body.scrollHeight,document.documentElement.clientHeight))")
                print("scrolling to load more comments")
                time.sleep(4)
    
            # Count total number of comments and set index to number of comments if less than 50 otherwise set as 50. 
            totalcomments= len(driver.find_elements_by_xpath("""//*[@id="content-text"]"""))
    
            if totalcomments < 100:
                index= totalcomments
            else:
                index= 100 
            
            # Loop through each comment and scrape info
            print("scraping through comments")
            ccount = 0
            while ccount < index: 
                try:
                    comment = driver.find_elements_by_xpath('//*[@id="content-text"]')[ccount].text
                except:
                    comment = ""
                try:
                    authors = driver.find_elements_by_xpath('//a[@id="author-text"]/span')[ccount].text
                except:
                    authors = ""
                try:
                    comment_date = driver.find_elements_by_xpath('//*[@id="published-time-text"]/a')[ccount].text
                except:
                    comment_date = ""
                try:
                    replies = driver.find_elements_by_xpath('//*[@id="more-text"]')[ccount].text                    
                    if replies =="View reply":
                        replies= 1
                    else:
                        replies =replies.replace("View ","")
                        replies =replies.replace(" replies","")
                except:
                    replies = ""
                try:
                    upvotes = str(driver.find_elements_by_xpath('//*[@id="vote-count-middle"]')[ccount].text)
                except:
                    upvotes = ""
                
                              
                # Write scraped data to csv file
                youtube_dict['query'] = query
                youtube_dict['url'] = url
                youtube_dict['title'] = title
                youtube_dict['upload_date'] = upload_date
                youtube_dict['channel'] = v_channel
                youtube_dict['no_of_views'] = v_views
                youtube_dict['likes'] = v_likes
                youtube_dict['dislikes'] = v_dislikes
                youtube_dict['comment'] = comment
                youtube_dict['author'] = authors
                youtube_dict['comment_date'] = comment_date
                youtube_dict['no_of_replies'] = replies
                youtube_dict['upvotes'] = upvotes
                writer.writerow(youtube_dict.values())
                
                ccount = ccount + 1
        
        # If video errors out, move onto the next one
        except TimeoutException as e:
            print(title, "  errored out: ",str(e))
            print("moving onto next video")
            