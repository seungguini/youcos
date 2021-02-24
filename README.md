# youcos

youcos (**you**tube **co**mment **s**craper) is a simple Python package for scraping YouTube comments!

:page_facing_up: **youcos** the following data into a csv file:
_each row corresponds to a comment_
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

## Demo
There are **two** main ways to scrape comments:

1. Scraping video titles and comments together
```python
from youcos import scrape_youtube

KEY = 'YOUR_YOUTUBE_V3_API_KEY'

scrape_youtube('stocks', KEY)
```

2. Scraping video titles and comments separately
_If you call `youcos` often on the same query, you may wish to avoid duplicating data by re-scraping comments._
_By calling `scrape video` and `scrape_comments` separately, you can filter and choose_
_the particular videos to scrape comments from!_

```python
from youcos import scrape_videos, scrape_comments

KEY = 'YOUR_YOUTUBE_V3_API_KEY'

videos = scrape_videos("stocks", KEY)

filtered_videos = foo(videos)

scrape_comments(filtered_videos)

foo(videos):
    # function to filter videos
```
    
## To Do
### Features
- search based on different filters
- selenium dependency support for all drivers
- choose to filter comments based on relevancy & top comments
- headless browser scraping (option)
- maximum number of videos to scrape
- maximum number of comments to scrape
- method to skip video authentication
### Deployment
- use Sphynx to build documentation

# Credits
- Year: 2021
- Author: Seunggun Lee
- Languages/Tools: Python3, [Selenium](https://www.selenium.dev/)