import requests
import json
import re
from lxml import etree
from selenium import webdriver
import time

def get_source(url):
    hds={
    'Connection': 'Keep-Alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'User-Agent': 'Googlebot/2.1 (+http://www.googlebot.com/bot.html)',
    'Host': 'www.tianyancha.com',
    'Referer': 'http://antirobot.tianyancha.com/captcha/verify?return_url=http://www.tianyancha.com/search/%E6%B1%9F%E8%A5%BF%20%20%20%E4%BA%BA%E5%8A%9B%E8%B5%84%E6%BA%90/11'
}
    req = requests.post(url, data=None, headers=hds)
    response = req.text
    return response
def get_company_source(company_url):
    driver = webdriver.PhantomJS(executable_path=r'D:\phantomjs\bin\phantomjs.exe')
    driver.get(company_url)  # 打开url
    time.sleep(2)  # 延迟3s. 该动态网页使用ajax设置了一个2s的延迟, 2s之后页面会发生变化
    return driver.page_sources
def get_url_group(source):
    page = etree.HTML(source)
    hrefs = page.xpath('//a[@class="query_name search-new-color"]')
    company_url_group = []
    for i in hrefs:
        company_url_group.append(i.attrib.get('href'))
    return company_url_group


def get_info(company_source):
    page = etree.HTML(source)
    hrefs = page.xpath('//a[@class="query_name search-new-color"]')
    company_url_group = []
    for i in hrefs:
        company_url_group.append(i.attrib.get('href'))
    return company_url_group

def companyInfo(company_url):
    try:
        pass
    except IndexError:
       pass

if __name__ == '__main__':
    url = 'http://linyi.tianyancha.com/search'
    a=get_source(url)
    b=get_url_group(a)
    print(b)
