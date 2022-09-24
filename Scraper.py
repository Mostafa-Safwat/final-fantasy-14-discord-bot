#Web scraper
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def checkCategory(className):
    if("topics" in className):
        return "Topic"
    elif("info" in className):
        return "Info"
    elif("maintenance" in className):
        return "Maintenance"
    elif("update" in className):
        return "Update"
    elif("obstacle" in className):
        return "Status"
    else:
        return "Unknown"
    
def checkIcon(className):
    if("topics" in className):
        return "https://i.imgur.com/xYeSAJM.png"
    elif("info" in className):
        return "https://i.imgur.com/mJqbq6d.png"
    elif("maintenance" in className):
        return "https://i.imgur.com/xFuVmNW.png"
    elif("update" in className):
        return "https://i.imgur.com/vWTMAGu.png"
    elif("obstacle" in className):
        return "https://i.imgur.com/IGyinyX.png"
    else:
        return "https://ffxiv.gamerescape.com/w/images/b/b1/Player8_Icon.png"\
            
def checkColor(className):
    if("topics" in className):
        return "#80a4ed"
    elif("info" in className):
        return "#fafcfc"
    elif("maintenance" in className):
        return "#ffffc7"
    elif("update" in className):
        return "#1ac989"
    elif("obstacle" in className):
        return "#d90f2a"
    else:
        return "#000000"
    

def scraper():
    url = 'https://na.finalfantasyxiv.com/lodestone/news/'
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    news_content = soup.find(class_="news__content")
    all_uls = news_content.findAll("ul")
    all_news = all_uls[1].findAll("li")
    all_topics = all_uls[2].findAll("li")
    news_and_topics = all_news + all_topics

    result = []

    for news in news_and_topics:
        if(not(news.p)):
            continue
        
        time = news.find(class_="news__list--time")
        time = time.script.getText().split("strftime(")[1].split(",")[0]
        time = datetime.fromtimestamp(int(time))
        time = time.strftime("%d %b %Y")

        data = {}
        data["time"] = time
        data["title"] = news.p.getText()
        data["url"] = "https://na.finalfantasyxiv.com" + news.a["href"]
        
        if(news.a.has_attr("class")):
            data["color"] = checkColor(news.a["class"][1])
            data["icon"] = checkIcon(news.a["class"][1])
            data["type"] = checkCategory(news.a["class"][1])
        else:
            data["color"] = checkColor("topics")
            data["icon"] = checkIcon("topics")
            data["type"] = checkCategory("topics")
        
        result.append(data)
    
    return result
