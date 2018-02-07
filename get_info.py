#get the important info from the articles

import urllib2
import bs4
import string

#remove some garbage characters
def cleaner(string):
    string = string.replace("\xE2\x96\xA0", "")
    string = string.replace("\xE2\x96\xA1", "")
    string = string.replace("\xEF\xBC\x89", "")
    string = string.replace("\xE3\x80\x80", "")
    string = string.replace("\xC2\xA0", "")
    string = string.replace("\x20", "")
    string = string.replace("\x3C\x70\x3E", "")
    return string

def date(url):
    url = url.split("/")
    date = url[4]+"-"+url[5]
    date = cleaner(date)
    return date

def dayoftheweek(article):
    return str.split(str(unicode(article.find("li").string).encode('utf-8')))[1]

def title(article):
    return str(unicode(article.find("h1").string).encode('utf-8'))

def page(article):
    page = (article.find_all("dl")[4].find("dd").string)
    page = str(unicode(page).encode('utf-8'))
    page = page.strip()
    return page

def column(article):
    content = article.find_all("founder-content")
    if len(content[0].p.string) < 20:
        content = str(unicode(content[0].p.string).encode('utf-8'))
        content = content.strip()
        content = cleaner(content)
        return content
    else:
        return "\xE6\x9D\xA5\xE8\xAE\xBA"  #special case for no column specified

def author_name(article):
    #print "Author name:"
    content = article.find_all("founder-content")
    author = content[0].find_all("p")
    author = author[len(author)-1].string
    author = str(unicode(author).encode('utf-8'))
    
    if str.find(author, "\xef\xbc\x88") < 0:
        return "maybe no author"
    else:
        #split between name and job at "(" and remove "("
        author = author.split("\xef\xbc\x88")
        author = author[0].strip()
        author = cleaner(author)
        if len(author) < 20:
            return str(author)
        else:
            return "maybe no author"

def author_job(article):
    content = article.find_all("founder-content")
    author = content[0].find_all("p")
    author = author[len(author)-1].string
    author = str(unicode(author).encode('utf-8'))
    
    if str.find(author, "\xef\xbc\x88") < 0:
        return "maybe no author"
    else:
        #split between name and job at "(" and remove "("
        author = author.split("\xef\xbc\x88")
        author = author[1].replace("\xEF\xBC\x89", "")
        author = author.strip()
        if len(author) < 50:
            return str(author)
        else:
            return "maybe no author"

def content(article):
    content = article.find("founder-content")
    return str(content)
