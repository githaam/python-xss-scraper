from domain import get_base_url, fixed_url
from bs4 import BeautifulSoup
import requests

class Finder:

    def __init__(self, page_url): #tambah disini
        super().__init__()
        self.page_url = page_url
        self.links = set()
        self.find_link(self.page_url) #tambah dsiini

    def find_link(self, page_url): #tambah dsiini
        try:
            response = requests.get(self.page_url)
        except Exception as e:
            print(str(e))
            return set(), str(e)
        else:
            soup = BeautifulSoup(response.text, 'html.parser')

            for urls in soup.find_all('a', href=True):
                url = str(urls['href'].replace(" ","").replace("\n",""))
            
                if url[0] == "/" and page_url[-1:] == "/":
                    url = self.page_url[:-1] + url
                elif url[0] == "/" and page_url[-1:] != "/":
                    url = get_base_url(page_url) + url
                else:
                    url = fixed_url(page_url, url)
                self.links.add(url)
        #return self.links, self.result #RETURN INI DITAMBAH

    #def find_pattern(self, soup, patterns)

    def page_links(self): #ERROR DISINI JUGA
        return self.links #tambah dsiini
    
    def error(self, message):
        pass

    # AKU HARUS LIAT LAGI VIDEO YANG ADA DI YOUTUBE