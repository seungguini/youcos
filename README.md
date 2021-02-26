# youcos

![GitHub](https://img.shields.io/github/license/seungguini/youcos)
![PyPI](https://img.shields.io/pypi/v/youcos)

:bar_chart: youcos (**you**tube **co**mment **s**craper) is a simple Python package for scraping YouTube comments!

:four_leaf_clover: **Easy YouTube v3 API Wrapper** - Simply provide your [YouTube v3 API Key](https://developers.google.com/youtube/v3/getting-started), and youcos will take care of the rest!
No additional code needed to configure API and process fetched JSON data.

:earth_asia: **Diverse Language Support** - Search, scrape, and save videos & comments in different languges with youcos.

:test_tube:	**Configurable Search Settings** - Adjust search location and search method.

:chart_with_upwards_trend: **Minimized Quota Usage** - Scrape comments without exhausting YouTube v3 quota through the built-in Selenium module with youcos!

## Demo
There are **two** main ways to scrape comments:

1. Scraping video titles and comments together
```python
from youcos import scrape_youtube

KEY = 'YOUR_YOUTUBE_V3_API_KEY'

# Call YouTube v3 API to request the first 30 videos search results for 'stocks'
# and scrape each video's top __ comments
scrape_youtube('stocks', KEY)
```

2. Scraping video titles and comments separately
```python
from youcos import scrape_videos, scrape_comments

KEY = 'YOUR_YOUTUBE_V3_API_KEY'

# Call YouTube v3 API to request the first 30 videos search results for 'stocks'
videos = scrape_videos("stocks", KEY)

# Filter videos to avoid re-scraping comments
filtered_videos = foo(videos)

# Scrape comments for filtered videos
scrape_comments(filtered_videos)

def foo(videos):
    # function to filter videos
```
## Installation   
`pip install youcos`

## Features
The following data are saved into the csv file:

_each row in the csv file corresponds to a comment_

- Url
- Title
- Channel name
- No. of views
- Date Uploaded
- No. of likes
- No. of dislikes
- Comment Text
- Comment Author
- Comment Date
- No. of replies to comment
- No. of upvotes for comments

## Dependencies
- [Selenium](https://www.selenium.dev/)

## Documentation
Check ___ for specific API documentation. This project was documented following the [numpy docstring conventions](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt),
which are supported by common documentation tools like [Sphynx](https://www.sphinx-doc.org/) while also maintaining readability.

## Credits
- Author: Seunggun Lee
- Languages/Tools: Python3, [Selenium](https://www.selenium.dev/)

## To Do
### Functionalities
- search based on different filters
- selenium dependency support for all drivers
- choose to filter comments based on relevancy & top comments
- headless browser scraping (option)
- maximum number of videos to scrape
- maximum number of comments to scrape
- method to skip video authentication
### Deployment
- use Sphynx to build documentation

