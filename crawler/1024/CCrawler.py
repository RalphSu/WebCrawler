## __author__ = 'liasu'

from pyquery import PyQuery as pq
import urllib2

class PostReader:
    def __init__(self, init_url):
        self.init_url = init_url
        self.next_page = init_url
        self.post_author = ""
        self.full_content = ""
        self.title = ""
        # this could be stored as restart index.
        self.current_index = 0
        pass

    def craw_text(self):
        d = pq(url=self.next_page)

        print d("title").text()
        print urllib2.unquote(d("title").text())

        print urllib2.unquote(d("td").text())

        # get next page url
        pass



if __name__ == "__main__":
    r = PostReader("http://news.baidu.com/advanced_news.html")
    r.craw_text()