#!/usr/bin/env python
# coding=utf-8
# 需要带一个uid参数在后面

import datetime
import requests
import sys

uid = sys.argv[1]
# uid = 22245854
# SESSDATA: e40cc2ff%2C1660895519%2C37141%2A21
# SESSDATA: a23e924a%2C1676453812%2C6098c%2A81 2022-8-20

# SESSDATA 有一个月有效期，记得更新
header = {
        'cookie':'SESSDATA=a23e924a%2C1676453812%2C6098c%2A81',
        'Host': 'api.bilibili.com',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Mobile Safari/537.36',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
}
# 关注数
url = 'https://api.bilibili.com/x/relation/stat?vmid=%s'%uid # 22245854 贰鼠 672328094 嘉然
resp = requests.get(url, headers=header)
json_data = resp.json()
follower = json_data['data']['follower']

# 视频播放数、专栏阅读数、总获赞数
likes_url = 'https://api.bilibili.com/x/space/upstat?mid=%s'%uid
likes_resp = requests.get(likes_url, headers=header)
likes_json_data = likes_resp.json()
# print(likes_json_data)
video_view = likes_json_data['data']['archive']['view']
article_view = likes_json_data['data']['article']['view']
likes = likes_json_data['data']['likes']

date = datetime.datetime.now().strftime('%Y-%m-%d')
line = '%s,%s,%s,%s,%s' % (date, follower, likes, video_view, article_view)
print(line)

