import scrapy


class JobSpider(scrapy.Spider):
    name = 'jobs'
    start_urls = [
        'https://www.work.ua/ru/jobs-kyiv-python/'
    ]

    def parse(self, response):

        for job in response.css('#pjax-job-list h2 a::text').getall():
            yield {
                'title': job
            }
