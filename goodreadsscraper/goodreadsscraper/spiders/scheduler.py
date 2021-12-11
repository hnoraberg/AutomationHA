import threading
import datetime
import time
import os
from goodreads import GoodreadsSpider
from googledrive import export_file
from get_top_five import get_top_five

class Scheduler(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run_scipts(self):
        try:
            process = CrawlerProcess()
            process.crawl(GoodreadsSpider)
            process.start()
            get_top_five('book_data.csv', 'book_data_top_five.csv')
            export_file('book_data_top_five.csv', '1qp790Jhx8sciXBLWGCfHy8lR5u_ZybsT')
        except Exception as e:
            print(e)

    def run(self):
        while True:
            current_week = str(datetime.date.today().isocalendar().week)
            if os.path.isfile(current_week):
                pass
            else:
                self.run_scipts()
            time.sleep(604800)

if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.start()