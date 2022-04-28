from urllib.parse import urlparse

def create_project_name(url):
    try:
        url = urlparse(url)
        url = url.netloc.replace(".","-")
        return url
    except:
        return ''

def get_base_url(url):
    try:
        url = urlparse(url)
        url = url.scheme + "://" + url.netloc

        # dont forget to add '/' after the netloc value 
        # when adding the path while scraping the link

        return url
    except:
        return ''

def fixed_url(page_url, url):
    sanitizeURL = urlparse(url)

    if sanitizeURL.scheme == '' and sanitizeURL.netloc == '' and sanitizeURL.path != '':
        url = get_base_url(page_url) + "/" +url
    
    return url

def remove_slash(url):
    if url[-1:] == "/":
        return url[:-1]
    else:
        return url