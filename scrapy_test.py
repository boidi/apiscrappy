import scrapy
from scrapy.crawler import CrawlerProcess
from bs4 import BeautifulSoup as bs



import mysql.connector
from mysql.connector import errorcode

# Connect to the database
try:
  connection = mysql.connector.connect(user='root',
                                password= 'root',
                                host= '127.0.0.1',
                                database='mydb')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)



tab_quote = {}

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    tab_quote = {}


    #def get_data(self):

     #   return self.my_data


    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)



    def parse(self, response):
        print("parse", response)
        global tab_quote
        
        tab_quote['comment'] = []
        tab_quote['author'] = []
        tab_quote['tag'] = []
        result = bs(response.body, 'html.parser')
        quotes = result.find_all('div', {'class': 'quote'})
        quotes_dict = {}
        for quote in quotes:
            span = quote.span
            comment = span.text
            comment = quote.find('span', {'class': 'text'}).text
            #print('comment:', comment)
            tab_quote['comment'].append(comment)
            author_span = span.next_sibling.next_sibling
            author_elem = author_span.small.text
            #print('author:', author_elem)
            tab_quote['author'].append(author_elem)
            tag_div = author_span.next_sibling.next_sibling
            tag_links = tag_div.find_all('a')
            tags = [link.text for link in tag_links]
            #print('tags:', tags)
            tab_quote['tag'].append(tags)
            #print('-----------')
        print(len(tab_quote['comment']))
        print(len(tab_quote['author']))
        print(len(tab_quote['tag']))
        #self.tab_quote = tab_quote
            # print(quote.prettify())
            # print('----------------------------')
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

        # self.log('Saved file %s' % filename)
        #self.my_data = tab_quote
        

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})


spider = QuotesSpider()
process.crawl(spider)
process.start()

#print("________________________________comment_____________",tab_quote['comment'])

#the_data = spider.get_data()



cursor = connection.cursor()
# query =" INSERT INTO mydb.authors (author) VALUES('toto');"
# cursor.execute(query)


#print("-----------------------------------------------------------------hgsdfg<uidhsghdihgi<difd<oif",tab_quote)

for i in range(len(tab_quote['comment'])):
    comment = tab_quote['comment'][i]
    print("______________________",comment)
    author = tab_quote['author'][i]
    print(author)
    tag = tab_quote['tag'][i]
    print(tag)

# Create a new record
    add_author = "INSERT INTO mydb.authors (author) VALUES ('"+str(author)+"');"
    cursor.execute(add_author)

    add_comment = 'INSERT INTO mydb.comments (comment, authors_id) VALUES ("'+str(comment)+'",'+str(cursor.lastrowid)+');'
    cursor.execute(add_comment)

    id_comment=cursor.lastrowid
    for j in tag:

        add_tag = 'INSERT INTO mydb.tags (tag, comments_id) VALUES ("'+str(j)+'", '+str(id_comment)+');'
        cursor.execute(add_tag)
        print('----------------',add_tag)
        

   # connection is not autocommit by default. So you must commit to save
    #your changes.
connection.commit()

cursor.close()
connection.close()
