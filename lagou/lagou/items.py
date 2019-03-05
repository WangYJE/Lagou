# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    url = scrapy.Field()   #详情页面的url地址
    name = scrapy.Field() #岗位名称
    salary = scrapy.Field() #薪水
    location = scrapy.Field() #地址
    work_exp = scrapy.Field() #工作经验
    edu_background = scrapy.Field() #学历要求
    type = scrapy.Field() #工作类型
    tags = scrapy.Field() #标签
    release_time = scrapy.Field() #发布时间
    advantage = scrapy.Field() #职位诱惑
    job_desc = scrapy.Field()  #职位描述
    work_addr = scrapy.Field() #工作地址
    company = scrapy.Field() #公司名称
    pass
