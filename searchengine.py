import urllib2
from urlparse import urljoin

from BeautifulSoup import *
from constants import *

class Crawler:
    """Crawler class
        TODO: DOC
    """

    # Initialize the crawler with the name of database
    def __init__(self, dbname):
        pass

    def __del__(self):
        pass

    def dbcommit(self):
        pass

    # Auxilliary function for getting an entry id and adding it if it's not present
    def getentryid(self, table, field, value, createnew=True):
        return None

    # Index an individual page
    def addtoindex(self, url, soup):
        print 'Indexing %s' % url

    # Extract the text from an HTML page (no tags)
    def gettextonly(self, soup):
        return None

    # Separate the words by any non-whitespace character
    def separatewords(self, text):
        return None

    # Return true if this url is already indexed
    def isindexed(self, url):
        return False

    # Add a link between two pages
    def addlinkref(self, urlFrom, urlTo, linkText):
        pass

    # Starting with a list of pages, do a breadth first search to the given depth, indexing pages as we go
    def crawl(self, pages, depth=2):
        pass

    # Create the database tables
    def createindextables(self):
        pass

    def crawl(self, pages, depth=2):
        """crawl method
        """
        for i in range(depth):
            newpages = set()
            for page in pages:
                try:
                    c = urllib2.urlopen(page)
                except:
                    print "Could not open %s" % page
                    continue

                soup = BeautifulSoup(c.read())
                self.addtoindex(page, soup)

                links = soup('a')
                print 'links=', links
                raw_input("Press Enter to continue...")

                for link in links:
                    if 'href' in dict(link.attrs):
                        print 'page=', page
                        print 'link["href"]=', link['href']
                        url = urljoin(page, link['href'])
                        print 'url=', url

                        if url.find("'") != -1:
                            continue
                        url = url.split('#')[0]  # remove location portion

                        if url[0:4] == 'http' and not self.isindexed(url):
                            newpages.add(url)

                        linkText = self.gettextonly(link)
                        self.addlinkref(page, url, linkText)

                self.dbcommit()

            pages = newpages