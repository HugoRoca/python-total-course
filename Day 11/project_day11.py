# website for scraping https://toscrape.com
import bs4
import requests

url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# list titles
titles_list = []

for i in range(1, 51):
    # create soup each page
    result = requests.get(url_base.format(i))
    soup = bs4.BeautifulSoup(result.text, 'html.parser')
    # select data books
    books = soup.select('.product_pod')
    # loop books
    for k in books:
        # verify they have five or four stars
        if len(k.select('.star-rating.Four')) != 0 or len(k.select('.star-rating.Five')) != 0:
            # save title in variable
            book_title = k.select('a')[1]['title']
            # append title in list
            titles_list.append(book_title)

# print books four or five stars
f = open('title.txt', 'w')
for i in titles_list:
    f.write(f'{i}\n')
    print(i)

f.close()



