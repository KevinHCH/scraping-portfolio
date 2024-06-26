from scrapy.statscollectors import StatsCollector
from scrapy.utils.serialize import ScrapyJSONEncoder


class StatsCollector(StatsCollector):
    def _persist_stats(self, stats, spider):
        encoder = ScrapyJSONEncoder()
        with open("./data/crawled_stats.json", "w") as file:
            data = encoder.encode(stats)
            file.write(data)
