import scrapy
import os


class LocalSpider(scrapy.Spider):
    name = 'ds4aspider'
    start_urls = ['file://{}'.format(os.path.abspath('content.html'))]
    
    custom_settings = {
        'ITEM_PIPELINES': {'scrapy.pipelines.files.FilesPipeline': 1},
        'FILES_EXPIRES' : 120,
        'FILES_STORE' : './files'
    }

    def parse(self, response):
        files_to_download = {"file_urls": []}
        for link in response.xpath('//a[contains(@href, "s3")]/@href'):
            files_to_download['file_urls'].append(link.get())
        return files_to_download
