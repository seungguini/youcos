# youcos

![GitHub](https://img.shields.io/github/license/seungguini/youcos)
![PyPI](https://img.shields.io/pypi/v/youcos)

youcos (**you**tube **co**mment **s**craper) is a simple Python package for scraping YouTube comments!


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

_If you call `youcos` often on the same query, you may wish to avoid duplicating data by re-scraping comments._
_By calling `scrape video` and `scrape_comments` separately, you can filter and choose_
_the particular videos to scrape comments from!_

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
Install with pip:
`pip install youcos`

## Features
:page_facing_up: save the following data are saved into the csv file:

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

## Credits
- Author: Seunggun Leez`
- Languages/Tools: Python3, [Selenium](https://www.selenium.dev/)