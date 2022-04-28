from bs4 import BeautifulSoup
import requests
from KMPSearch import *

import concurrent.futures, itertools

class Scanner:

    def __init__(self, page_url, pattern):
        super().__init__()
        self.page_url = page_url
        self.result = set()
        self.scan_page(pattern)
    
    def scan_page(self, pattern):
        try:
            response = requests.get(self.page_url)
        except Exception as e:
            print(str(e))
            return str(e)
        else:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            with concurrent.futures.ThreadPoolExecutor() as executor: #Add max_workers=50
                list_hasil = executor.map(KMPSearch, pattern, itertools.repeat(str(soup)))
            
            for hasil in list_hasil:
                self.result.add(str(hasil))
                # print (f'ini hasilnya {hasil}')
                # if "Not Found" not in hasil:
                #     self.result.add(str(hasil))

            
            self.result.remove("Not Found")
            #     if self.result == 'Not Found': self.result = ''
            
    # def iter_scan(self, soup, pattern):
    #     print (pattern)
    #     hasil = KMPSearch(pattern, str(soup))
    #     if hasil != "Not Found":
    #         print(f"{pattern} | {self.result}")

    def scan_result(self):
        return self.result
    
    def error(self, message):
        pass
# CROSSCHECK APAKAH BENAR SCANNING