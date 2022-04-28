from urllib.request import urlopen
from bs4.element import ResultSet
from finder import Finder
from scanner import Scanner
from general import *
from domain import *

class Spider:

    #Class variables (shared among all instances)
    project_name = ''
    target = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    deep_loop = 0  # simpan value
    edge = 0        # pembatas
    queue = set()
    crawled = set()
    temp = set()
    found = set()
    pattern = []
    
    def __init__(self, project_name, target, edge, pattern):
        Spider.project_name = project_name
        Spider.target = target
        Spider.base_url = get_base_url(target)
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        Spider.found_file = Spider.project_name + '/found.txt'
        Spider.deep_loop = 0
        Spider.edge = edge
        Spider.pattern = pattern
        self.boot()

        self.crawl_page('First Spider', Spider.target) 
 
    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.target)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)
        Spider.found = file_to_set(Spider.found_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if (page_url not in Spider.crawled):
            print (thread_name + ' now crawling ' + page_url)
            print ('Queue '+ str(len(Spider.queue)) + ' | Crawled ' + str(len(Spider.crawled)))
            try:
                links = Spider.gather_links(page_url)
                result = Spider.gather_result(page_url, Spider.pattern)
            except:
                Spider.queue.remove(page_url)
            else:
                Spider.add_links_to_temp(links) #tambah disini SELESAIKAN DISINI

                if result: 
                #     # Bikin prose jadi lelet v
                    list_result = [str(s) for s in result] # Move set to list
                    final_result = ", " . join(list_result) # Join the list
                    # Bikin proses jadi lelet ^

                # Spider.found.add(page_url)
                    Spider.found.add(final_result + " on " + page_url + "\n")
                    # Add the list string to the file
                
                Spider.queue.remove(page_url)
                Spider.crawled.add(page_url)
                
                if len(Spider.queue) == 0 and (Spider.deep_loop != Spider.edge):
                    Spider.queue.update(Spider.temp)
                    Spider.deep_loop += 1
                    Spider.temp.clear()
                Spider.update_files()
    
    @staticmethod
    def gather_links(page_url): #tambah disini
        try:
            finder = Finder(page_url) #tambah disini
        except Exception as e:
            return set()
        return finder.page_links() #ERROR DISINI

    @staticmethod
    def gather_result(page_url, pattern):
        try:
            result = Scanner(page_url, pattern)
        except Exception as e:
            return str(e)
        return result.scan_result()

    @staticmethod
    def add_links_to_temp(links):
        for url in links:
            if (url in Spider.queue) or (url in Spider.crawled) or (url in Spider.temp):
                continue
            Spider.temp.add(url)

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if (url in Spider.queue) or (url in Spider.crawled):
                continue
            Spider.queue.add(url)
    
    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
        set_to_file(Spider.found, Spider.found_file)