from __future__ import print_function

import urllib2
import bs4

import generate_addresses as generate
import get_info as get
import special_articles

#input file name
INPUT_FILE = "input_dates.txt"

#structures to hold the addresses
main_addr_arr = []
page_addr_arr = []
article_addr_arr = []

#generate the main addresses for all days or from days from a file
#generate.all_main_address(main_addr_arr)
generate.all_main_address_from_file(main_addr_arr, INPUT_FILE)

#generate all the urls
for url_i in main_addr_arr:
    try:
        main = urllib2.urlopen(url_i)
    except:
        print("finished getting all the addresses or hit an error")
        break
    
    bs4_main = bs4.BeautifulSoup(main, "lxml")
    page_addr_arr = []
    generate.page_address(bs4_main, url_i, page_addr_arr)
    
    for url_j in page_addr_arr:
        page = urllib2.urlopen(url_j)
        bs4_page = bs4.BeautifulSoup(page, "lxml")
        generate.article_address(bs4_page, url_i, article_addr_arr)

#archive articles to files (50 articles per file)
file = open("1_50.html", "a")
#show the chinese characters properly by using this header
file.write("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />")

#scrape the imporant data
count = 1
for url_i in article_addr_arr:
    #archive to files

    if (count % 50 == 0):
        file.close()
        file = open(str(count)+"_"+str(count+50)+".html", "a")
        file.write("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />")

    #some special cases for ads :/
    if (url_i == "http://epaper.bjnews.com.cn/html/2017-09/04/content_694345.htm?div=0"):
        print("advertising")
    elif (url_i == "http://epaper.bjnews.com.cn/html/2017-09/15/content_695526.htm?div=0"):
        print("advertising")
    elif (url_i == "http://epaper.bjnews.com.cn/html/2013-07/16/content_449197.htm?div=-1"):
        print("cartoon")
    elif (url_i == "http://epaper.bjnews.com.cn/html/2017-10/25/content_699364.htm?div=0"):
        print("advertising")
    elif (url_i == "http://epaper.bjnews.com.cn/html/2017-10/25/content_699364.htm?div=-1"):
        print("advertising")
    elif (url_i == "http://epaper.bjnews.com.cn/html/2017-11/27/content_703125.htm?div=0"):
        print("advertising")
    elif (url_i == "http://epaper.bjnews.com.cn/html/2017-12/07/content_704679.htm?div=0"):
        print("advertising")
    elif (url_i == "http://epaper.bjnews.com.cn/html/2017-12/11/content_705046.htm?div=0"):
        print("advertising")
    elif (url_i == "http://epaper.bjnews.com.cn/html/2017-12/08/content_704811.htm?div=-1"):
        print("advertising")
    elif (url_i == "http://epaper.bjnews.com.cn/html/2017-12/11/content_705046.htm?div=0"):
        print("advertising")
    elif (url_i == "http://epaper.bjnews.com.cn/html/2017-12/11/content_705046.htm?div=-1"):
        print("advertising")
    elif (url_i == "http://epaper.bjnews.com.cn/html/2013-11/13/content_477569.htm?div=-1"):
        print("cartoon")
    elif (url_i == "http://epaper.bjnews.com.cn/html/2013-11/28/content_480589.htm?div=-1"):
        print("cartoon")
    elif (url_i == "http://epaper.bjnews.com.cn/html/2013-12/13/content_483851.htm?div=-1"):
        print("cartoon")
    elif (url_i == "http://epaper.bjnews.com.cn/html/2017-12/11/content_705048.htm?div=-1"):
        print("unknown problem")
    elif (url_i == "http://epaper.bjnews.com.cn/html/2016-07/15/content_644227.htm?div=-1"):
        print("unknown problem http://epaper.bjnews.com.cn/html/2016-07/15/content_644227.htm?div=-1")
    else:
        article = urllib2.urlopen(url_i)
        bs4_article = bs4.BeautifulSoup(article, "lxml")
        #print the information
        print(str(count) + "," + get.date(url_i)+ "," + get.dayoftheweek(bs4_article) + "," + get.page(bs4_article) + "," + get.title(bs4_article) + "," + get.column(bs4_article) + "," + get.author_name(bs4_article) + "," + get.author_job(bs4_article) + ",=HYPERLINK(\"" + str(url_i) +"\")")

        if (get.title(bs4_article) == "\xe6\x9d\xa5\xe4\xbf\xa1"):
            special_articles.print_letter(count, bs4_article, url_i)

        if (get.title(bs4_article) == "\xE5\xBE\xAE\xE8\xA8\x80\xE5\xA4\xA7\xE4\xB9\x89"):
            special_articles.print_tweet(count, bs4_article, url_i)

        #archive the articles to files
        file.write("\n <h1> Article " + str(count) + "</h1> \n")
        file.write(get.title(bs4_article))
        file.write(get.date(url_i))
        file.write(str(bs4_article.find("founder-content")))
    
    count=count+1

