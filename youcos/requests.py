# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from dotenv import load_dotenv
import os

from googleapiclient.discovery import build

def ytSearch(query, API_KEY, maxResults=20):
    if not API_KEY:
        return '"Please provide "YouTube API Key"'
    
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    
    # Grab YouTube API results
    search_response = youtube.search().list(
        q='stocks',
        maxResults=maxResults,
        part='id,snippet',
        type='video'
    ).execute()
    items = search_response['items']
    
    if not items:
        return 'Error: No YouTube results'

    return list(map(filter_videos, items))
    
    
def filter_videos(video):
    title = video['snippet']['title']
    date = video['snippet']['publishedAt']
    url = "https://www.youtube.com/watch?v=" + video['id']['videoId']
    
    return {
        'title': title,
        'date': date,
        'url': url
    }
    
    
def main():
    load_dotenv()
    
    # Authenticate with YouTube API
    KEY = os.environ.get('API_KEY')
    
    query = 'stocks'
    
    video_list = ytSearch(query, API_KEY=KEY, maxResults=10)
    print(video_list)
    
if __name__ == "__main__":
    main()
