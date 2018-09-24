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
    
    def shutDown(self):
        return self.browser.quit()


if __name__ == '__main__':
    content = Crawler()
    content.startBrowser()
    time.sleep(5)
    content.getContent('https://www.google.com')
    content.shutDown()