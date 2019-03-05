#!/usr/bin/env python*- coding: utf-8 -*-
"""
@Name: Mr.Wang
@file: cookie_process
@time: 2019/2/2817:48
"""
class Process:

    def __init__(self, cookie):
        self.cookie = cookie

    def pro(self):
        dict1 = {}
        items = self.cookie.split(";")
        for item in items:
            key = item.split("=")[0].replace(' ', '')
            value = item.split("=")[1]
            dict1[key] = value
        return dict1


if __name__ == '__main__':
    cookie = "_ga=GA1.2.342629408.1545985016; user_trace_token=20181228161655-f08fe3f0-0a78-11e9-ad84-5254005c3644; LGUID=20181228161655-f08fe725-0a78-11e9-ad84-5254005c3644; WEBTJ-ID=20190228175102-1693383af9f34d-0d2e0d26af7d6f-47e1137-1327104-1693383afa12a; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1551347462; _gat=1; _gid=GA1.2.1178596277.1551347462; LGSID=20190228175056-5834669c-3b3e-11e9-8866-5254005c3644; PRE_UTM=m_cf_cpc_baidufs_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.a00000apJPO0FYNyJzoP4Vw8zlEPTHyKhNW98xrngERwPh3mLiXdb3DDNKxBOgx6QlvXSFd5Wc-SDnjUT7Tb-vVgn_FUTVk5ar8dxvvYaJ5SH1c_StGIrBO0V6LomIBkCsaWkBzD1tGBO-wt5UUXdmyE3W-uIvHXj-ZktJnt678-dwMu5p1KvA3CRcB6vRoeTNRtBRT7DANC83kHWs.7R_NR2Ar5Od663rj6tJQrGvKD7ZZKNfYYmcgpIQC8xxKfYt_U_DY2yP5Qjo4mTT5QX1Bsp3SgZjdYtEUsng_3_A85-9kstEKNzvI5WTMG4IYnrzEIzYyIH_ahGv-5QWdQjPakbvUPz6.U1Yk0ZDqUA7MULR0TA-W5H00Ijd_myIEIfKGUHYznWR0u1dBugK1n0KdpHdBmy-bIfKspyfqnHm0mv-b5HnLnfKVIjYknjDLg1DsnH-xnW0vn-tknjc1g1nsnjIxn1msnfKopHYs0ZFY5H6zn6K-pyfqnHfdr7tznHDsrNtzrjR3P7tzrjRdPdtzrjRkr7tzrjfknsKBpHYYnjFxnW0Yg1DdPfKVm1Y3nHRsnWR3nWwxnH0snNtknjDzn1DzPjcdg17xnH0zg100TgKGujYs0Z7Wpyfqn0KzuLw9u1Ys0A7B5HKxn0K-ThTqn0KsTjY4nHbvPWmzP1f0UMus5H08nj0snj0snj00Ugws5H00uAwETjYs0ZFJ5H00uANv5gKW0AuY5H00TA6qn0KET1Ys0AFL5HDs0A4Y5H00TLCq0A71gv-bm1dsTzd8p6KYIgnqPjn4Pjb1P1bknWbdrHTsP161n0Kzug7Y5HDdPHD1PjTYPHnLn160Tv-b5yPBPyNWrjKhnj0snHmzujb0mLPV5RcLfWnLf1NDfWb1rHfvnW00mynqnfKsUWYs0Z7VIjYs0Z7VT1Ys0ZGY5H00UyPxuMFEUHYsg1Kxn7tsg1nsnH7xn0Kbmy4dmhNxTAk9Uh-bT1Ysg1Kxn7tsg1Kxn0Ksmgwxuhk9u1Ys0AwWpyfqn0K-IA-b5iYk0A71TAPW5H00IgKGUhPW5H00Tydh5HDv0AuWIgfqn0KhXh6qn0Khmgfqn0KlTAkdT1Ys0A7buhk9u1Yk0Akhm1Ys0APzm1Yvnj04rf%26word%3Dlagou%26ck%3D6226.2.86.270.152.240.191.200%26shh%3Dwww.baidu.com%26sht%3Dbaiduhome_pg%26us%3D1.0.1.0.1.300.0%26bc%3D110101; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpc_baidufs_pc%26m_kw%3Dbaidufs_cpc_wh_067de6_5cc815_lagou; JSESSIONID=ABAAABAAAIAACBIF7E4EC9EE654899205B33EBF5E83F661; index_location_city=%E5%85%A8%E5%9B%BD; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1551347468; LGRID=20190228175102-5be066de-3b3e-11e9-a951-525400f775ce"
    tran = Process(cookie)
    print(tran.pro())



