from googleapiclient.discovery import build

def ytSearch(query, API_KEY, maxResults=20):
    """
    Request YouTube video search results and return their titles, publish dates, and urls

    Keyword arguments:
    query -- the query to search for on YouTube
    API_KEY  -- the API key to authenticate requests to YouTube Data API v3
    maxResults -- the maximum number of videos to request
    """
    
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
        return

    return list(map(filter_videos, items))
    
def filter_videos(video):
    """
    Extract video title, publish date, and url from YouTube search results
    
    Keyword arguments:
    video -- the video search result requested from YouTube API v3
    """
    
    title = video['snippet']['title']
    date = video['snippet']['publishedAt']
    url = "https://www.youtube.com/watch?v=" + video['id']['videoId']
    
    return {
        'title': title,
        'date': date,
        'url': url
    }
    
