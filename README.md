![GitHub](https://img.shields.io/github/license/seungguini/youcos)
![PyPI](https://img.shields.io/pypi/v/youcos)

# youcos

youcos (**you**tube **co**mment **s**craper) is a simple Python package for scraping YouTube videos and comments!

:four_leaf_clover: **Lightweight YouTube v3 API Wrapper** - Simply provide your [YouTube v3 API Key](https://developers.google.com/youtube/v3/getting-started), and youcos will take care of the rest!
No additional code needed to configure API and process fetched JSON data.

:earth_asia: **Diverse Language Support** - Search, scrape, and save videos & comments in different languges with youcos.

:rocket: **Fast Performance** - Request and write approximately 4,000 comments, just within 1 minute.

:chart_with_upwards_trend: **Minimized Quota Usage** - Scrape comments without exhausting YouTube v3 quota through the built-in Selenium module with youcos!

## Table of Contents
- [Demo](#demo)

- [Installation](#installation)

- [Features](#features)

- [Dependencies](#dependencies)

- [Documentation](#documentation)

- [Credits](#credits)

- [To Do](#to-do)

## Demo
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
```shell
pip install youcos
```

## Features

- Collected Data

| Video Data | Comment Data |
| ----------- | ----------- |
| URL         | text        |
| title       | author      |
| channel name| date        |
| upload date | no. of replies|
| no. of likes| no. of upvotes|
| no. of dislikes| # of comments | 

## Dependencies
- [Selenium](https://www.selenium.dev/)
- [google-api-python-client](https://developers.google.com/youtube/v3/quickstart/python)

```shell
pip install --upgrade selenium google-api-python-client
```

## Documentation
Check ___ for specific API documentation. This project was documented following the [numpy docstring conventions](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt),
which are supported by common documentation tools like [Sphynx](https://www.sphinx-doc.org/) while also maintaining readability.

## Contributing
Package author and maintainer is Seunggun Lee ([seungguini@gmail.com](mailto:seungguini@gmail.com)).
Contributions and feedback are more than welcome.

## Credits
- Author: Seunggun Lee
- Languages/Tools: Python3, [Selenium](https://www.selenium.dev/)