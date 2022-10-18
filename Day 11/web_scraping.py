# don't forget install this
import bs4
import requests

result = requests.get('https://escueladirecta-blog.blogspot.com')

# print(result.text)
soup = bs4.BeautifulSoup(result.text, 'html.parser')

# print(soup)
# print(soup.select('title'))
# print(soup.select('title')[0].getText())
# print(soup.select('p'))
#
# text = soup.select('p')[3].getText()
# print(text)

column = soup.select('.content p')

for i in column:
    print(i.getText())


