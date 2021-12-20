import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as soup
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd


browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://nypost.com/tag/car-crashes/")

time.sleep(5)
#button = browser.find_element_by_link_text("See More Stories")
button = browser.find_element_by_link_text(" See More Stories ")
button.click()

time.sleep(3)
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://nypost.com/tag/car-crashes/")

time.sleep(5)
#button = browser.find_element_by_link_text("See More Stories")
button = browser.find_element_by_class_name('button',{'class':'button button--solid see-more'})
button.click()

time.sleep(3)

def executeTest():
    global driver
    driver.get('https://nypost.com/tag/car-crashes/')
    time.sleep(7)
    element = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/section/div/div[2]/article/div[2]/button')
    element.click()
    time.sleep(3)

def startWebDriver():
    global driver
    options = Options()
    options.add_argument("--disable-infobars")
    driver = webdriver.Chrome(chrome_options=options)

if __name__ == "__main__":
    startWebDriver()
    executeTest()
    driver.quit()


nypost_url = "https://nypost.com/tag/car-crashes/"
#print(nypost_url)

html = requests.get("https://nypost.com/tag/car-crashes/")

#b = soup(html.content, "lxml")

links = ['https://nypost.com/tag/car-crashes/', 'https://nypost.com/tag/car-crashes/page/2/', 'https://nypost.com/tag/car-crashes/page/3/', 'https://nypost.com/tag/car-crashes/page/4/',
         'https://nypost.com/tag/car-crashes/page/5/', 'https://nypost.com/tag/car-crashes/page/6/', 'https://nypost.com/tag/car-crashes/page/7/', 'https://nypost.com/tag/car-crashes/page/8/',
         'https://nypost.com/tag/car-crashes/page/9/', 'https://nypost.com/tag/car-crashes/page/10/', 'https://nypost.com/tag/car-crashes/page/11/', 'https://nypost.com/tag/car-crashes/page/12/',
         'https://nypost.com/tag/car-crashes/page/13/', 'https://nypost.com/tag/car-crashes/page/14/', 'https://nypost.com/tag/car-crashes/page/15/', 'https://nypost.com/tag/car-crashes/page/16/',
         'https://nypost.com/tag/car-crashes/page/17/', 'https://nypost.com/tag/car-crashes/page/18/', 'https://nypost.com/tag/car-crashes/page/19/', 'https://nypost.com/tag/car-crashes/page/20/',
         'https://nypost.com/tag/car-crashes/page/21/', 'https://nypost.com/tag/car-crashes/page/22/', 'https://nypost.com/tag/car-crashes/page/23/', 'https://nypost.com/tag/car-crashes/page/24/',
         'https://nypost.com/tag/car-crashes/page/25/', 'https://nypost.com/tag/car-crashes/page/26/', 'https://nypost.com/tag/car-crashes/page/27/', 'https://nypost.com/tag/car-crashes/page/28/',
         'https://nypost.com/tag/car-crashes/page/29/', 'https://nypost.com/tag/car-crashes/page/30/', 'https://nypost.com/tag/car-crashes/page/31/', 'https://nypost.com/tag/car-crashes/page/32/',
         'https://nypost.com/tag/car-crashes/page/33/', 'https://nypost.com/tag/car-crashes/page/34/', 'https://nypost.com/tag/car-crashes/page/35/', 'https://nypost.com/tag/car-crashes/page/36/',
         'https://nypost.com/tag/car-crashes/page/37/', 'https://nypost.com/tag/car-crashes/page/38/', 'https://nypost.com/tag/car-crashes/page/39/', 'https://nypost.com/tag/car-crashes/page/40/',
         'https://nypost.com/tag/car-crashes/page/41/', 'https://nypost.com/tag/car-crashes/page/42/', 'https://nypost.com/tag/car-crashes/page/43/', 'https://nypost.com/tag/car-crashes/page/44/',
         'https://nypost.com/tag/car-crashes/page/45/', 'https://nypost.com/tag/car-crashes/page/46/', 'https://nypost.com/tag/car-crashes/page/47/', 'https://nypost.com/tag/car-crashes/page/48/',
         'https://nypost.com/tag/car-crashes/page/49/', 'https://nypost.com/tag/car-crashes/page/50/', 'https://nypost.com/tag/car-crashes/page/51/', 'https://nypost.com/tag/car-crashes/page/52/',
         'https://nypost.com/tag/car-crashes/page/53/', 'https://nypost.com/tag/car-crashes/page/54/', 'https://nypost.com/tag/car-crashes/page/55/', 'https://nypost.com/tag/car-crashes/page/56/',
         'https://nypost.com/tag/car-crashes/page/57/', 'https://nypost.com/tag/car-crashes/page/58/', 'https://nypost.com/tag/car-crashes/page/59/', 'https://nypost.com/tag/car-crashes/page/60/',
         'https://nypost.com/tag/car-crashes/page/61/', 'https://nypost.com/tag/car-crashes/page/62/', 'https://nypost.com/tag/car-crashes/page/63/', 'https://nypost.com/tag/car-crashes/page/64/',
         'https://nypost.com/tag/car-crashes/page/65/', 'https://nypost.com/tag/car-crashes/page/66/', 'https://nypost.com/tag/car-crashes/page/67/', 'https://nypost.com/tag/car-crashes/page/68/',
         'https://nypost.com/tag/car-crashes/page/69/', 'https://nypost.com/tag/car-crashes/page/70/', 'https://nypost.com/tag/car-crashes/page/71/', 'https://nypost.com/tag/car-crashes/page/72/',
         'https://nypost.com/tag/car-crashes/page/73/', 'https://nypost.com/tag/car-crashes/page/74/', 'https://nypost.com/tag/car-crashes/page/75/', 'https://nypost.com/tag/car-crashes/page/76/',
         'https://nypost.com/tag/car-crashes/page/77/', 'https://nypost.com/tag/car-crashes/page/78/', 'https://nypost.com/tag/car-crashes/page/79/', 'https://nypost.com/tag/car-crashes/page/80/',
         'https://nypost.com/tag/car-crashes/page/81/', 'https://nypost.com/tag/car-crashes/page/82/', 'https://nypost.com/tag/car-crashes/page/83/', 'https://nypost.com/tag/car-crashes/page/84/',
         'https://nypost.com/tag/car-crashes/page/85/', 'https://nypost.com/tag/car-crashes/page/86/', 'https://nypost.com/tag/car-crashes/page/87/', 'https://nypost.com/tag/car-crashes/page/88/',
         'https://nypost.com/tag/car-crashes/page/89/', 'https://nypost.com/tag/car-crashes/page/90/', 'https://nypost.com/tag/car-crashes/page/91/', 'https://nypost.com/tag/car-crashes/page/92/']

for url in links:
    html = requests.get(url)
    b = soup(html.content, "lxml")
    
    #for news in b.findAll("h3"):
    #    news.text
    #x  = "Headline : {}".format(link.text)
    links = []
    for i in b.findAll('h3',{'class':'story__headline'}):
        links.append(i.a['href'])
        #print(links[-1])
    #for news in b.findAll("h3"):
        #print (news.text)
        #print(main_links)
    for link in links:
        page = requests.get(link)
        b = soup(page.content)
        for news in b.findAll('div',{'class':'single__content entry-content m-bottom'}):
            print(news.text.strip())

print(df)
#print(df.shape)

"""
#THIS WORKS TO GET GOOD CODE
for url in links:
    html = requests.get(url)
    b = soup(html.content, "lxml")
    x = url
    for news in b.findAll("h3"):
        print (news.text)
    #x  = "Headline : {}".format(link.text)
    links = []
    for i in b.findAll('h3',{'class':'story__headline'}):
        links.append(i.a['href'])
    print(links)
    for link in links:
        page = requests.get(link)
        b = soup(page.content)
        for news in b.findAll('div',{'class':'single__content entry-content m-bottom'}):
            print(news.text.strip(), end="NEW BODY")


for news in b.findAll("h3"):
    print (news.text)
    #x  = "Headline : {}".format(link.text)

links = []
for i in b.findAll('h3',{'class':'story__headline'}):
    links.append(i.a['href'])

print(links)


for news in b.findAll("h3"):
    print (news.text)
    #x  = "Headline : {}".format(link.text)

links = []
for i in b.findAll('h3',{'class':'story__headline'}):
    links.append(i.a['href'])

print(links)

for link in links:
    page = requests.get(link)
    b = soup(page.content)
    for news in b.findAll('div',{'class':'single__content entry-content m-bottom'}):
        print(news.text.strip())
"""
