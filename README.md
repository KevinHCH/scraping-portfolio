# Web Scraping Portfolio

## About This Repository

Welcome to my web scraping portfolio! This repository showcases a collection of Scrapy spiders I've developed, demonstrating my skills and experience in web scraping and data extraction.

As a freelance web scraping specialist, I've created these spiders to illustrate my ability to extract data from various types of websites efficiently and ethically.

## Projects

Each folder in this repository represents a different scraping project. Here's a brief overview of what you'll find:

1. [**RightMove Housing Data**](https://www.rightmove.co.uk): A spider that extracts property listing data from RightMove from all the regions of UK.
   - Technologies: Scrapy, Python
   - Features: Pagination handling, data cleaning, JSON export
   - [See the spider here](./rightmove.co.uk/)


## Skills Demonstrated

- Efficient use of Scrapy framework
- Handling of JavaScript-rendered content
- Respectful scraping practices (respecting robots.txt, rate limiting)
- Data cleaning and normalization
- Handling of pagination and infinite scroll
- Error handling and robustness
- Output in various formats (JSON, CSV, etc.)

## How to Run These Spiders

Each project folder contains its own README with specific instructions, but generally:

1. Clone this repository
2. Navigate to the project folder
3. Install requirements: `pip install -r requirements.txt`
4. Run the spider: `scrapy crawl spider_name`

Or just move to the spider you want to run and use this command: `docker compose build && docker compose up`

## Ethical Considerations

All spiders in this repository are designed with ethical web scraping practices in mind. They respect robots.txt files, implement appropriate rate limiting, and are intended for educational and portfolio purposes only.

## Contact Me

If you're interested in hiring me for your web scraping needs, please contact me at **hi@buildwithkev.com**