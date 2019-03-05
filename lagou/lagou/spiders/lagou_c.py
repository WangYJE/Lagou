# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from lagou.items import LagouItem


class LagouCSpider(CrawlSpider):
    name = 'lagou_c'
    allowed_domains = ['lagou.com']
    start_urls = ['https://lagou.com/']

    rules = (
        Rule(LinkExtractor(allow=r'zhaopin/.*', restrict_css='.sidebar')),
        Rule(LinkExtractor(allow=r'jobs/\d+.html', restrict_css='.s_position_list'), callback='parse_item', follow=False),

    )



    custom_settings = {
        "COOKIES_ENABLED": False,
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'Cookie': '_ga=GA1.2.342629408.1545985016; user_trace_token=20181228161655-f08fe3f0-0a78-11e9-ad84-5254005c3644; LGUID=20181228161655-f08fe725-0a78-11e9-ad84-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; WEBTJ-ID=20190305121420-1694c0f3cc89f-0f5209a1ea7805-47e1137-1327104-1694c0f3ccbba; _gat=1; _gid=GA1.2.176741027.1551759261; LGSID=20190305121419-25bf91a7-3efd-11e9-927e-525400f775ce; PRE_UTM=m_cf_cpc_baidufs_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.0s0000a7HcV7X_Q0Lz4bDXNOCTWezh5YzJSbuSlQbc1i5OQRtmDObkvnUkq_1kp9lL8PWgF0cx2X1wFvtQw82XEfWl8W57blvQtSQ70y5OEqZwY1HRLoIoMv_zk5S6bUtqqYni-9cD8HmJ_UmiZ5tHQWrWhd0JGeW48WIyvguont7MZXi8wgLLQihB5paJQbwjONPEt9vXxqYfsA06.DR_NR2Ar5Od663rj6tJQrGvKD7ZZKNfYYmcgpIQC8xxKfYt_U_DY2yP5Qjo4mTT5QX1Bsp3SgZjdYtEUsng_3_A85-9kstEKNzqrEyhO_4mIdhHgvT8Z1lTr1dsePSZ1LmIMo9qxPHReiM-kl-9h9m3qP--B60.U1Yk0ZDqs2v4_sK9uZ745TaV8Un0mywkIjYz0ZKGm1Ys0Zfqs2v4V0KGUHYznjf0u1dsT1c0Iybqmh7GuZR0TA-b5HDv0APGujY1P1D0UgfqnH0kPdtknjD4g1DsnWPxnHDsPH7xn1msnfKopHYs0ZFY5H6zn6K-pyfqnHfdr7tznHDsrNtzrjR3P7tzrjRdPdtzrjRkr0KBpHYYnjFxnW0Yg1DdPfKVm1Y3nHRsnWR3nWwxnH0snNtkg1Dsn-ts0Z7spyfqn0Kkmv-b5H00ThIYmyTqn0K9mWYsg100ugFM5H00TZ0qrHD4PWmvnWTY0A4vTjYsQW0snj0snj0s0AdYTjYs0AwbUL0qn0KzpWYs0Aw-IWdsmsKhIjYs0ZKC5H00ULnqn0KBI1Ykn0K8IjYs0ZPl5fK9TdqGuAnqTZnVuyPJ0ZwdT1YkP1Rvn16Yn1m1nWcsPjf4P1T3P0Kzug7Y5HDdPHDLPHbzPHmkrjn0Tv-b5ycLnj7hP1m1nj0snW0LP1D0mLPV5RcLfWnLf1NDfWb1rHfvnW00mynqnfKsUWYs0Z7VIjYs0Z7VT1Ys0ZGY5H00UyPxuMFEUHYsg1Kxn7tsg100uA78IyF-gLK_my4GuZnqn7tsg1Kxn1fvrjbdP-ts0ZK9I7qhUA7M5H00uAPGujYs0ANYpyfqQHD0mgPsmvnqn0KdTA-8mvnqn0KkUymqnHm0uhPdIjYs0AulpjYs0Au9IjYs0ZGsUZN15H00mywhUA7M5HD0UAuW5H00mLFW5Hf4n1m4%26word%3D%25E6%258B%2589%25E9%2592%25A9%26ck%3D4451.4.87.225.144.559.271.290%26shh%3Dwww.baidu.com%26sht%3Dbaiduhome_pg%26us%3D1.0.1.0.1.302.0%26bc%3D110101; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpc_baidufs_pc%26m_kw%3Dbaidufs_cpc_wh_6ffeb4_c502f4_%25E6%258B%2589%25E5%258B%25BE; LGRID=20190305121419-25bf9430-3efd-11e9-927e-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1551347462,1551409472,1551759262; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1551759262',
            'Host': 'www.lagou.com',
            'Origin': 'https://www.lagou.com',
            'Referer': 'https://www.lagou.com/',
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        }
    }

    def remove_splash(self,value):

        return value.replace(r'/', '').strip()

    def parse_item(self, response):
        f = open("test.html","wb")
        f.write(response.body)
        f.close()
        item = LagouItem()  # 生成一个item对象
        item['url'] = response.url  # 这个response是详情页面的response，因为本次我们只对详情页面使用了回调函数，所以可以这样理解
        item['name'] = response.css('.name::text').extract_first()  # 用css选择器选择职位名称，因为结果是个列表，所以使用extract_first()提取第一个
        item['salary'] = response.css('.salary::text').extract_first()  # 用css选择器选择薪水，但是这个是一个string类型，后续可以进行优化
        location = response.xpath('//*[@class="job_request"]//span[2]/text()').extract_first()  # 使用xpath进行提取，span[2]代表多个平行span标签选择第二个
        print(location)
        item['location'] = self.remove_splash(location)  # 得到的文本带有/，还有多余的空格，使用remove_splash函数进行清除，当然这个函数需要自己定义
        work_exp = response.xpath('//*[@class="job_request"]//span[3]/text()').extract_first()  # 获取工作经验要求
        item['work_exp'] = self.remove_splash(work_exp)  # 使用remove_splash对数据清洗
        edu_background = response.xpath('//*[@class="job_request"]//span[4]/text()').extract_first()  # 获取学历要求
        item['edu_background'] = self.remove_splash(edu_background)
        item['type'] = response.xpath('//*[@class="job_request"]//span[5]/text()').extract_first()  # 获取职位类型，全职or兼职
        tags = response.css('.labels::text').extract()  # tags是一个列表类型，直接使用extract()进行提取，而不使用extract_first()
        item['tags'] = ','.join(tags)  # join函数是python内置函数，作用是把一个序列拼接起来，这里是用逗号把所有的tags标签拼接起来构成一个新的列表
        item['release_time'] = response.css(
            '.publish_time::text').extract_first()  # 获取发布时间，实际上这个发布时间存在很多种情况，有具体日期，也有几天前这种，后续进行优化
        advantage = response.css('.job-advantage p::text').extract()  # 职位诱惑
        item['advantage'] = '\n'.join(advantage)  # 用join进行拼接
        job_desc = response.css('.job_bt p::text').extract()  # 获取职位描述
        item['job_desc'] = '\n'.join(job_desc)
        work_addr = response.css('.work_addr a::text').extract()[:-1]  # 这个工作地址列表提取出来后，需要把最后一项去掉，最后一项是地图。。
        item['work_addr'] = ''.join(work_addr)
        item['company'] = response.css('.job_company img::attr(alt)').extract_first()  # 获取公司名称
        yield item
