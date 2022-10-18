import bs4
import requests

result = requests.get('https://www.escueladirecta.com/courses')

soup = bs4.BeautifulSoup(result.text, 'html.parser')
# images = soup.select('.course-box-image')
images = soup.select('.course-box-image')[0]['src']
# for i in images:
#     print(i)

image_download = requests.get(images)

# wb = write bytes
f = open('image.jpg', 'wb')
f.write(image_download.content)
f.close()
