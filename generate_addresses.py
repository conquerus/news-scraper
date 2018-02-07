import numpy as np
import urllib2
import bs4

date = "2017-0"
base = "http://epaper.bjnews.com.cn/html/"

#strings of the sections included in the search (in Chinese)
SECTION_STRINGS = ["\xE7\xA4\xBE\xE8\xAE\xBA\xC2\xB7\xE6\x9D\xA5\xE4\xBF\xA1", "\xE7\xA4\xBE\xE8\xAE\xBA\xC2\xB7\xE6\x9D\xA5\xE8\xAE\xBA", "\xE6\x97\xB6\xE4\xBA\x8B\xE8\xAF\x84\xE8\xAE\xBA", "\xE4\xB8\x93\xE6\xA0\x8F", "\xE8\xB0\x83\xE6\x9F\xA5\x2F\xE8\xAF\x84\xE8\xAE\xBA", "\xE7\xA4\xBE\xE8\xAE\xBA", "\xE6\x96\xB0\xE8\xAF\x84\xE8\xAE\xBA"]

def generate_address(date):
    return base+date+"/node_1.htm"

def link_contains_string(url_str):
    for search_string in SECTION_STRINGS:
        if (str.find(url_str,search_string)>=0):
            return True
    return False

#the main address for the newspaper that day
def all_main_address(main_addr):
    for month in range(12, 13):
        if month < 10:
            date="2017-0"
        else:
            date="2017-"
            
        date = date + str(month)

        #adjust for different amount of days in a month
        if (month == 2):
            for day in range(1, 29):
                if (day<10): 
                    main_addr.append(generate_address(date + "/0" + str(day)))
                else:
                    main_addr.append(generate_address(date + "/" + str(day)))
        elif (month == 4 or month == 6 or month == 9 or month == 11):
            for day in range(1, 31):
                if (day < 10): 
                    main_addr.append(generate_address(date + "/0" + str(day)))
                else:
                    main_addr.append(generate_address(date + "/" + str(day)))
        else:
            for day in range(1, 32):
                if (day < 10): 
                    main_addr.append(generate_address(date + "/0" + str(day)))
                else:
                    main_addr.append(generate_address(date + "/" + str(day)))

#main addresses for days from a file
def all_main_address_from_file(main_addr, INPUT_FILE):
    date_array = np.loadtxt(INPUT_FILE, dtype=str)
    for date in date_array.flat:
        main_addr.append(generate_address(date))
    
#link to the full page                    
def page_address(bs4_main, main_addr, page_addr):
    for links in bs4_main.find_all("a"):
        temp = links.contents[0]
        temp_str = str(unicode(temp).encode('utf-8'))
        #filter the sections
        if link_contains_string(temp_str):
            page_addr.append(main_addr.rstrip("node_1.htm")+links.get("href"))

# links to individual articles
def article_address(bs4_page, main_addr, article_addr):
    for links in bs4_page.find_all("a"):
        temp = links.contents[0]
        temp_str = str(unicode(temp).encode('utf-8'))
        #the links to articles always? contain the word content
        if (str.find(links.get("href"),"content") >= 0 and temp_str != "\xE6\x9B\xB4\xE6\xAD\xA3\xE4\xB8\x8E\xE8\xAF\xB4\xE6\x98\x8E"): #exclude corrections articles
            article_addr.append(main_addr.rstrip("node_1.htm")+links.get("href"))

