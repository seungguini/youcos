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

## Demo
There are **two** ways to scrape comments, each catered for different purposes
1. Scraping video titles and comments separately
```python
import youcos

videos = youcos.scrape_videos("stocks")
filtered_videos = foo(videos)
youcos = scrape_comments()

foo(videos):
    # function to return filtered videos #
```
    
2. Scraping video titles and comments together
```python
import youcos

scrape_youtube(videos)
```

## Notes
- How does YouTube display / recommend their videos?

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