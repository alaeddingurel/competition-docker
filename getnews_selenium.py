import lxml.html
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re
import codecs
import json

with codecs.open("urls.txt","r","utf-8") as f:
    links = f.readlines()

browser = webdriver.PhantomJS("/usr/local/bin/phantomjs")

browser.set_page_load_timeout(30)

for url in links:

    url = re.sub(r'\n|\r| |"', r'', url)

    try:
        browser.get(url)
    except TimeoutException:
        print("Couln't load page : " + url)
        continue

    delay = 3 # seconds
    try:
        myElem = WebDriverWait(browser, delay).until(EC.staleness_of(browser.find_element_by_tag_name("html")))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")

    filename = re.sub(r"\/|:", r"_", url)
    with codecs.open("news/" + filename, "w", "utf-8") as g:
        g.write(browser.page_source)

    print("Finished : " + url)
