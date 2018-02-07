from __future__ import print_function
import get_info as get

#special type of article: tweet (weibo)
def print_tweet(count, article, url_i):
    content = article.find("founder-content").find_all("p")

    for i in range(0, len(content)-1):
        author_position = str(content[i]).find("\xEF\xBC\x9A\x23") #the wierd box thing
        if (author_position >= 0):
            print(str(count) + "," + get.date(url_i)+ "," + get.dayoftheweek(article) + "," + get.page(article) + "," + get.title(article) + ",", end ='')
            print("\xE5\xBE\xAE\xE8\xA8\x80\xE5\xA4\xA7\xE4\xB9\x89", end='')
            print(",", end='')

            author = content[i]
            author = author.string
            author = str(unicode(author).encode('utf-8'))
            author = author.split("\xEF\xBC\x9A\x23")
            if (len(author)>1):
                author_name = get.cleaner(author[0])
                print(str(author_name) + ",", end='')
                print("\xE8\x81\x8C\xE5\x91\x98", end='')
                print(",=HYPERLINK(\"" + str(url_i) +"\")")
            else:
                print("author error, author error" + ",=HYPERLINK(\"" + str(url_i) +"\")")

#special type of article: letter
def print_letter(count, article, url_i):
    content = article.find("founder-content").find_all("p")
    print(str(count) + "," + get.date(url_i)+ "," + get.dayoftheweek(article) + "," + get.page(article) + ",", end ='')
    content_string = str(unicode(content[0].string).encode('utf-8'))
    content_string = get.cleaner(content_string)
    content_string = content_string.strip()
    print(content_string, end='')
    print(",", end='')
    print("\xE6\x9D\xA5\xE4\xBF\xA1", end='')
    print(",", end='')

    for i in range(0, len(content)-1):
        author_position = str(content[i]).find("\xE2\x96\xA1") #the wierd box thing
        if (author_position >= 0):
            author = content[i]
            author = author.string
            author = str(unicode(author).encode('utf-8'))
            author = author.split("\xE2\x96\xA1")
            if (str(author[1]).find("\xef\xbc\x88") >= 0):
                author = author[1].split("\xef\xbc\x88")
            if (str(author[1]).find("\x28") >=0 ):
                author = author[1].split("\x28")
            if (len(author)>1):
                author_name = get.cleaner(author[0])
                author_position = get.cleaner(author[1])
                print(str(author_name) + "," + str(author_position) + ",=HYPERLINK(\"" + str(url_i) +"\")")
            else:
                print("author error, author error" + ",=HYPERLINK(\"" + str(url_i) +"\")")
            i = i + 1
            if (str(content[i]).find("\x40")<0):
                print(str(count) + "," + get.date(url_i)+ "," + get.dayoftheweek(article) + "," + get.page(article) + ",", end ='')
                content_string = get.cleaner(content_string)
                content_string = content_string.strip()
                content_string = str(unicode(content[i].string).encode('utf-8'))
                print(content_string, end='')
                print(",", end='')
                print("\xE6\x9D\xA5\xE4\xBF\xA1", end='')
                print(",", end='')

    i = len(content)-1
    author_position = str(content[i]).find("\xE2\x96\xA1") #the wierd box thing
    if (author_position >= 0):
        author = content[i]
        author = author.string
        author = str(unicode(author).encode('utf-8'))
        author = author.split("\xE2\x96\xA1")
        author = author[1].split("\xef\xbc\x88")
        author_name = get.cleaner(author[0])
        author_position = get.cleaner(author[1])
        if (len(author)>1):
            print(str(author_name) + "," + str(author_position) + ",=HYPERLINK(\"" + str(url_i) +"\")")
        else:
            print("author error, author error" + ",=HYPERLINK(\"" + str(url_i) +"\")")
