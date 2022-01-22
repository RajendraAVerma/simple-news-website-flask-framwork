import requests

from classes.newsclass import NewsClass

class Api:
    newsList = []
    def __init__(self):
        url = "https://dnnews.in/wp-json/wp/v2/posts?_fields=author,id,excerpt,title,link,jetpack_featured_media_url"
        get = requests.get(url= url)
        json = get.json()


        for item in json:
            id = item['id']
            link = item['link']
            title = item['title']['rendered']
            content = item['excerpt']['rendered']
            imageLink = item['jetpack_featured_media_url']
            self.newsList.append(NewsClass(id=id, link = link, title = title, content = content, imageLink=imageLink))
        




