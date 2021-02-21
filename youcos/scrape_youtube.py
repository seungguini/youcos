# import required libraries
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

def scrape_videos(query, driver_path="C:/WebDriver/bin/chromedriver.exe"):
    """
    Scrape top _ YouTube videos for query and return object of urls,  titles, and queries.

    Keyword arguments:
    query -- the query to search for on YouTube
    driver_path -- the browser path for Selenium (default "C:/WebDriver/bin/chromedriver.exe")
    """

    link = "https://www.youtube.com/results?search_query=" + query
            
    driver = webdriver.Chrome(executable_path=driver_path,chrome_options=chrome_options)
    driver.get(link)
    
    print("=" * 40)
    print("Scraping " + link)    
    
    time.sleep(5)
    
    for i in range(0,5):  # Scroll to load comments
        driver.execute_script("window.scrollTo(0,Math.max(document.documentElement.scrollHeight,document.body.scrollHeight,document.documentElement.clientHeight))")
        print("scrolling to load more comments")
        time.sleep(4)

    video_list = driver.find_elements_by_xpath('//*[@id="video-title"]')  # Scrape video title
    
    urls = []
    titles = [] 
    queries = []
    
    for video in video_list: # store URL and video titles
        urls.append(video.get_attribute('href'))
        titles.append(video.get_attribute('title'))
        queries.append(query.replace('+',' '))
        print("scraped ", video.get_attribute('title'))
    
    return {'urls' : urls, 'titles' : titles, 'queries' : queries}
    
    
def scrape_youtube(urls_titles, driver_path, csv_path="../comments.csv"):
    """
    Scrape YouTube video and comment info and write data to a csv file.

    Keyword arguments:
    urls_titles -- the query to search for on YouTube
    driver_path -- the browser path for Selenium (default "C:/WebDriver/bin/chromedriver.exe")
    csv_path -- the file path to save csv file (default "../comments.csv")
    """
    
    urls = urls_titles['urls']
    titles = urls_titles['titles']
    queries = urls_titles['queries']
    
    path = csv_path
    csv_file = open(csv_path,'w', encoding="UTF-8", newline="")
    writer = csv.writer(csv_file)    
    # write header names
    writer.writerow(['url', 'link_title', 'channel', 'no_of_views', 'time_uploaded', 'comment', 'author', 'comment_posted', 'no_of_replies','upvotes','downvotes'])
    
    driver = webdriver.Chrome(executable_path=driver_path)

    videocounter = 0
    for url in urls:
        
        print("=" * 40)
        print("video title : ",titles[videocounter])
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
    
        print("+" * 40)  # Shows in terminal when details of a new video is being scraped
        print("Scraping child links ")
        #scroll down to load comments
        driver.execute_script('window.scrollTo(0,390);')
    
        # let comments load
        time.sleep(2)
    
        try:
            print("sorting by top comments")
            sort= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div#icon-label")))
            sort.click()
                
            topcomments =driver.find_element_by_xpath("""//*[@id="menu"]/a[1]/paper-item/paper-item-body/div[1]""")
            topcomments.click()
            
    
            # Loads 20 comments , scroll five times to load next set of 40 comments. 
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
            
            # loop through each comment and scrape info
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
                    comment_posted = driver.find_elements_by_xpath('//*[@id="published-time-text"]/a')[ccount].text
                except:
                    comment_posted = ""
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
                    
                youtube_dict['query'] = queries[videocounter]
                youtube_dict['url'] = url
                youtube_dict['link_title'] = titles[videocounter]
                youtube_dict['likes'] = v_likes
                youtube_dict['dislikes'] = v_dislikes
                youtube_dict['channel'] = v_channel
                youtube_dict['no_of_views'] = v_views
                youtube_dict['time_uploaded'] = v_timeUploaded
                youtube_dict['comment'] = comment
                youtube_dict['author'] = authors
                youtube_dict['comment_posted'] = comment_posted
                youtube_dict['no_of_replies'] = replies
                youtube_dict['upvotes'] = upvotes
                writer.writerow(youtube_dict.values())
                
                # increment comment counter
                ccount = ccount + 1
        # if video errors out, move onto the next one
        except TimeoutException as e:
            print(titles[videocounter], "  errored out: ",str(e))
            print("moving onto next video")
        # counter for the videos
        videocounter = videocounter+1
        
    # close writer and file