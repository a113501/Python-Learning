import requests
from lxml import etree
import os

class spider():

    def get_url(self,url):
        url_list=[]
        self.sources_rc = requests.get(url)
        self.source = etree.HTML(self.sources_rc.text)
        self.div_page = self.source.xpath('//a[@class="portfolio-image"]')
        for href in self.div_page:
            url_list.append(href.attrib.get('href'))
        return url_list

    def get_story(self,url):
        story = []
        self.content = []
        self.sources_rc = requests.get(url)
        self.source = etree.HTML(self.sources_rc.text)
        self.title = self.source.xpath('//*[@id="sub-header-content"]/h1')
        self.content_rc = self.source.xpath('//*[@id="single"]/div[3]/p')
        for content in self.content_rc:
            self.content.append(content.text)
        story.append(self.title[0].text)
        story.append(self.content)
        return story

    def save_as_file(self,file):
        path_now = os.getcwd()
        fname=file[0]+r'.txt'
        try:
            os.mkdir(dir_new)
        except:
            pass
        texts = file[0] + '\n'
        for text in file[1]:
            try:
                texts = texts + text
            except:
                pass
        with open(fname,'w') as fp:
            try:
                fp.write(texts)
                fp.close()
            except:
                return print(fname+'下载失败')
        return print('已下载'+fname)

if __name__ == '__main__':
    lee = spider()
    for i in range(6):
        url = 'http://www.fqpai.com/writing/page/'+'%s'% i
        list = lee.get_url(url)
        for div_url in list:
            try:
                content = lee.get_story(div_url)
                lee.save_as_file(content)# print(content)
            except:
                print(div_url+'连接失败')
