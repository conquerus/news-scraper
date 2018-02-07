#get the important info from the letters

import urllib2
import bs4
import string

def title(article):
    article.find("founder-content").find_all("p")
    
