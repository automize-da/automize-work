# -*- coding: utf-8 -*-
#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time


binary = FirefoxBinary("C:\\Users\\Hanna\\AppData\\Local\\Mozilla Firefox\\firefox.exe")


class Crawler(object):
    
    def startBrowser(self):
        self.browser = webdriver.Firefox(firefox_binary=binary)
        self.browser.wait = WebDriverWait(self.browser, 5)
        return self.browser
    
    def getContent(self, url):
        try:
            self.browser.get(url)
            time.sleep(5)
            return self.browser.page_source
        except Exception as e:
            self.browser.quit()
            print(e, e.args)
            return ''
    
    def getContentByCss(self, css):
        try:
            elem = self.browser.find_element_by_css_selector(css)
            time.sleep(5)
            return elem
        except Exception as e:
            self.browser.quit()
            print(e, e.args)
            return 'Css Selector was not founded'
    
    def searchInput(self, css, key):
        searchElem = self.browser.find_element_by_css_selector(css)
        
        try:
            search = searchElem.send_keys(key)
            time.sleep(3)
            search.submit()
    
        except Exception as e:
            self.browser.quit()
            print(e, e.args)
            return 'Search not completed'
        
    def shutDown(self):
        return self.browser.quit()


if __name__ == '__main__':
    content = Crawler()
    content.startBrowser()
    time.sleep(5)
    content.getContent('http://google.com')
    #content.shutDown()
    #cssClick = content.getContentByCss('.main > div:nth-child(1) > ul:nth-child(18) > li:nth-child(2) > a:nth-child(1)')
    #cssClick.click()
    dosearch = content.searchInput('.gLFyf', 'hanna')
    
