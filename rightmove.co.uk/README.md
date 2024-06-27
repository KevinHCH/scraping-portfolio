# RightMove.co.uk Property Data Scraper

## Overview

This Scrapy spider is designed to extract comprehensive property sale data from RightMove.co.uk, one of the UK's leading real estate websites. It covers all regions of the UK, providing a rich dataset of property transactions.

## Data Extracted

For each property listing, the spider collects the following information:

- Full property address
- Sale date
- Sale price
- URL of the property listing
- District/Region
- Latitude and Longitude
- Property type (e.g., detached, semi-detached, flat)

## Features

### Comprehensive Coverage

This spider is configured to crawl through all regions of the UK listed on RightMove.co.uk, ensuring a complete dataset of property sales across the country.

### Pagination Handling

The spider efficiently handles pagination, allowing it to navigate through all pages of results for each region. This ensures that no property listing is missed, regardless of how deep it is in the search results.

### Large Dataset Generation

When run to completion, this spider is capable of generating a dataset with over 500,000 rows of property data. This makes it an excellent tool for large-scale property market analysis, trend identification, and machine learning projects focused on the UK real estate market.

### Data Cleaning and Formatting

The extracted data is cleaned and formatted to ensure consistency and usability. Dates are standardized, prices are converted to numerical values, and geographical data is properly formatted for easy integration with mapping tools.

**IMPORTANT**: If you run this project you will have more than 500k leads