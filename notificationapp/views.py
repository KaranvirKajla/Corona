from django.shortcuts import render
from plyer import notification
import requests
from bs4 import BeautifulSoup
from bs4 import Comment
# Create your views here.

def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = None,
        timeout = 10
    )
    
def getData(url):
    r= requests.get(url)
    return r.text
def notify(request):
    # notifyMe("Karan","fhshdfihidshfisiof")
    html = getData('https://www.mohfw.gov.in/')

    
    # print(soup.prettify)
    soup = BeautifulSoup(html , 'lxml')

    for tr in soup.find_all('tr'):
        comment = tr.find(text=lambda text:isinstance(text, Comment))
        commentsoup = BeautifulSoup(comment , 'lxml')
        print(commentsoup)
        # views = commentsoup.find('span', {'class': 'views'})
        # shares= commentsoup.find('span', {'class': 'shares'})
        # print (views.get_text(), shares['data-shares'])