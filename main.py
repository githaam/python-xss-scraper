# 1.  proses crawling ga usah dimasukin ke flowchart (karena prosesnya dikerjakan)
#     jadi langsung saja dari crawling ke scrapping dan scanning
#  
# 2.  lebih baik bicara ke dosen terkait ini

import threading, time
from queue import Queue
from spider import Spider
from domain import *
from general import *

# create workers thread (will die when exits)
def create_workers():
    for _ in range(NUMBER_OF_THREAD):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

# do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()

# each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

#check if there an item in the queue, if so crawl html
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue.')
        create_jobs()
    else:
        print(f"Done. Crawled {len(Spider.crawled)} page(s)")
        print(f"Pattern found on {len(Spider.found)} page(s)")

if __name__ == '__main__':
    TARGET, DEEP_LEVEL = 'https://blog.devtiersoftware.com/posts/ipsam-voluptatum-nisi-magni-et', 0 #change this
    
    #ts = datetime.datetime.now()
    start = time.process_time()
    PROJECT_NAME = str(create_project_name(TARGET)) + time.strftime(" %Y%m%d %H%M")

    try:
        PATTERN = read_pattern()
    except OSError as err:
        print("OS error: {0}".format(err))
        print ("pattern.txt not found")
    else:
        try:        
            QUEUE_FILE = PROJECT_NAME + '/queue.txt'
            CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
            FOUND_FILE = PROJECT_NAME + '/found.txt'
        except:
            print ("can't create project file")
        else:

            NUMBER_OF_THREAD = 15
            
            queue = Queue()
            Spider(PROJECT_NAME, TARGET, DEEP_LEVEL, PATTERN)
            
            create_workers()
            crawl()
            print(f"Execute time: {count_time(time.process_time() - start)}")