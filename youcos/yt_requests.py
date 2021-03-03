from googleapiclient.discovery import build

def yt_search(query, API_KEY, maxResults=20):
    """
    Request YouTube video search results for a particular query and return parsed data

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
    
    # Request search results
    search_response = youtube.search().list(
        q=query,
        maxResults=maxResults,
        part='id',
        type='video',
        order='viewCount'
    ).execute()
    search_items = search_response['items']
    
    videos = None
    
    if not search_items:
        return videos
    
    id_str = ""
    
    # Request video data
    for video in search_items:
        id_str = id_str + video["id"]["videoId"] + ","
    
    videos_response = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=id_str
    ).execute()
    video_items = videos_response['items']
    
    videos = list(map(parse_videos, video_items))
    
    return videos

def yt_comments(videoId, API_KEY):
    """
    Request YouTube comments for a particular video and return parsed data

    Parameters
    ----------
    videoId : string
        The ID of video to fetch comments
    API_KEY : string
        The API key to authenticate requests to YouTube Data API v3
    Returns
    ----------
    comments : list of dict or None
        The list of collected comments data, each dictionary with the comment's text, author, publish date, and number of likes, or None if
        no YouTube search results exist
    Notes
    ----------
    For more info on YouTube v3 API, please visit https://developers.google.com/youtube/v3
    """
    
    if not API_KEY:
        return '"Please provide "YouTube API Key"'
    
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    
    try:
        # Grab comments for videoId
        comments_response = youtube.commentThreads().list(
            part='id,snippet',
            videoId=videoId,
            maxResults=100,
            order="relevance"
    
        ).execute()
    
    except:
        return
    
    items = comments_response['items']
    comments = None
    
    if not items:
        return comments
    
    comments = list(map(parse_comments, items))
    
    return comments
    
def parse_videos(video):
    """
    Parse data from the video JSON structure
    
    Parameters
    ----------
    video : JSON object of strings
        The video search result requested from YouTube API v3
    Returns
    ----------
    video_dict : dictionary of strings
        The dictionary contianing video title, published date, id, views, likes, dislikes, and no. of comments
    """
    
    
    title = video['snippet']['title']
    date = video['snippet']['publishedAt']
    channel = video['snippet']['channelTitle']
    ID = video['id']
    stats = video['statistics']
    views = stats['viewCount']
    try:
        likes = stats['likeCount']
        dislikes = stats['dislikeCount']
    except:
        likes = 0
        dislikes = 0
    try:
        commentCount = stats['commentCount']
    except:
        commentCount = 0
    
    video_dict = {
        'title': title,
        'date': date,
        'channel': channel,
        'id': ID,
        'views': views,
        'likes': likes,
        'dislikes': dislikes,
        'comment_count': commentCount
    }
    
    return video_dict
    
def parse_comments(commentThread):
    """
    Parse data from the comment JSON structure
    
    Parameters
    ----------
    comment : JSON object of strings
        The comment resource requested from YouTube API v3
    Returns
    ----------
    comment_dict : dictionary of strings
        The dictionary contianing comment text, author, date, no. of likes
    """
    comment = commentThread['snippet']['topLevelComment']
    
    snippet = comment['snippet']
    text = snippet['textOriginal'].replace("\n", " ").replace("\t", " ").replace("\r", " ")
    author = snippet['authorDisplayName']
    date = snippet['publishedAt']
    likes = snippet['likeCount']
    
    comment_dict = {
        'text' : text,
        'author' : author,
        'date' : date,
        'likes' : likes
    }
    
    return comment_dict