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

---

# Demo
```python
import youcos


videos = youcos.scrape_videos('query')
```
---

## API
There are **two** ways to scrape comments, each catered for different purposes
1. Scraping video titles and comments separately

_When scraping for a search query multiple times, you may want to avoid re-scraping the same videos
from before._

```

```
    - methods: `scrape_videos` & `scrape_youtube`
    - good for authenticating scraped titles to prevent
    
2. Scraping video titles and comments together
---

## Notes
- How does YouTube display / recommend their videos?

---

## To Do
- switch youtube title list as a list of JSON style objects [{url, title, query}]
- search based on different filters
- selenium dependency support for all drivers
- choose to filter comments based on relevancy & top comments
- headless browser scraping (option)
- maximum number of videos to scrape
- maximum number of comments to scrape
- method to skip video authentication

# Credits
- Year: 2021
- Author: Seunggun Lee
- Languages/Tools: Python3, [Selenium](https://www.selenium.dev/)