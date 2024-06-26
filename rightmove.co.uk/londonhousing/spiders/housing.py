import json
import scrapy
from rich import print
from londonhousing.items import LondonhousingItem
from flatten_json import flatten


class HousingSpider(scrapy.Spider):
    name = "housing"
    allowed_domains = ["rightmove.co.uk"]
    start_urls = [
        "https://www.rightmove.co.uk/house-prices-in-Central-London.html",
        "https://www.rightmove.co.uk/house-prices-in-East-London.html",
        "https://www.rightmove.co.uk/house-prices-in-North-East-London.html",
        "https://www.rightmove.co.uk/house-prices-in-North-London.html",
        "https://www.rightmove.co.uk/house-prices-in-North-West-London.html",
        "https://www.rightmove.co.uk/house-prices-in-South-East-London.html",
        "https://www.rightmove.co.uk/house-prices-in-South-London.html",
        "https://www.rightmove.co.uk/house-prices-in-South-West-London.html",
        "https://www.rightmove.co.uk/house-prices-in-West-London.html",
    ]

    def __init__(self, *args, **kwargs):
        super(HousingSpider, self).__init__(*args, **kwargs)
        self.collected_links = []

    def parse(self, response):
        if "house-prices/" in response.url:
            yield from self.parse_item(response)
        else:
            yield from self.get_links(response)

    def get_links(self, response):
        links = response.css(
            "li[class*='highlightMapRegion'] > a::attr(href)"
        ).extract()
        absolute_links = [response.urljoin(link) for link in links]
        self.collected_links.extend(absolute_links)

        for link in absolute_links:
            yield response.follow(link, callback=self.parse)

    def parse_item(self, response):
        script_content = response.css(
            'script:contains("window.__PRELOADED_STATE__")::text'
        ).get()

        if script_content:
            print(f"Processing {response.url}")
            json_str = script_content.split("window.__PRELOADED_STATE__ = ")[1]
            json_data = json_str.replace("\n", "").replace("£", "")
            all_data = json.loads(json_data)
            data = all_data.get("results")
            district = data.get("title").split("House Prices in ")[1]
            total_houses = data.get("resultCount")

            for value in data.get("properties"):
                item = LondonhousingItem(
                    url=value.get("detailUrl", None),
                    district=district,
                    total_houses=total_houses,
                    address=value.get("address", None),
                    property_type=value.get("propertyType", None),
                    has_floor_plan=value.get("hasFloorPlan", None),
                    transactions=value.get("transactions", None),
                    location=value.get("location", None),
                )
                yield item

        total_pages = all_data.get("pagination").get("last")
        current_page = all_data.get("pagination").get("current")
        next_page = int(current_page) + 1
        if next_page <= int(total_pages):
            next_page_url = response.urljoin(f"?page={next_page}")
            yield response.follow(next_page_url, callback=self.parse)

    # def closed(self, reason):
    #     print("Collected links:", self.collected_links)
