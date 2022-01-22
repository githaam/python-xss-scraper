from bs4 import BeautifulSoup
import requests
from KMPSearch import *

import concurrent.futures

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
            
            # self.result = KMPSearch(pattern[8], str(soup))
            # print (pattern)
            with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
                list_hasil = executor.map(KMPSearch, pattern, str(soup))
            
            for hasil in list_hasil:
                # print (f'ini hasilnya {hasil}')
                self.result.add(str(hasil))
            
            #     if self.result == 'Not Found': self.result = ''
            
            # PAKAI THREAD LAGI
            
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