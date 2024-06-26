FROM python:3.12.4-bullseye

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# very important
ENV PYTHONPATH="${PYTHONPATH}:/app"
RUN cd /app
CMD ["scrapy", "crawl", "housing", "-O", "/app/data/output.json", "-s", "LOG_FILE=/app/data/spider.log"]