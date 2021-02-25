from googleapiclient.discovery import build

def yt_search(query, API_KEY, maxResults=20):
    """
    Request YouTube video search results and return their titles, publish dates, and urls

    Parameters
    ----------
    query : string
        The query to search for on YouTube
    API_KEY : string
        The API key to authenticate requests to YouTube Data API v3
    maxResults : int, optional
        The maximum number of videos to scrape
    Returns
    ----------
    videos : list of dict or None
        The list of collected video data, each dictionary with the video's url and title, or None if
        no YouTube search results exist
    Notes
    ----------
    For more info on YouTube v3 API, please visit https://developers.google.com/youtube/v3
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
    
    videos = None
    
    if not items:
        return videos
    
    videos = list(map(filter_videos, items))
    
    return videos
    
def filter_videos(video):
    """
    Extract video title, publish date, and url from YouTube search results
    
    Parameters
    ----------
    video : JSON object of strings
        The video search result requested from YouTube API v3
    Returns
    ----------
    video_dict : dictionary of strings
        The dictionary contianing video title, published date, and url
    """
    
    title = video['snippet']['title']
    date = video['snippet']['publishedAt']
    url = "https://www.youtube.com/watch?v=" + video['id']['videoId']
    
    video_dict = {
        'title': title,
        'date': date,
        'url': url
    }
    
    return video_dict
    
