"""
Commands to test
"""

import searchengine
pagelist = ['http://saurabhbuddha.blogspot.in/']
crawler = searchengine.Crawler('')
crawler.crawl(pagelist)
