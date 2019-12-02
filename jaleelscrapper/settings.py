BOT_NAME = 'jaleelscrapper'

SPIDER_MODULES = ['jaleelscrapper.spiders']
NEWSPIDER_MODULE = 'jaleelscrapper.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure item pipelines
ITEM_PIPELINES = {
    'jaleelscrapper.pipelines.JaleelscrapperPipeline': 300,
}

# Enable and configure HTTP caching (disabled by default)
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = [301, 302, 404]
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
