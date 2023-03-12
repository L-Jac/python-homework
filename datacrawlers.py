import json
import time
import random
import requests
import pickle


def randDelay(a, b):
    """设置随机延迟"""
    time.sleep(random.uniform(a, b))


def get_videoData(aid, videoDict):
    """
    根据AID获取视频数据
    :param aid: 视频aid
    :param videoDict: 存储视频信息字典
    :return: None
    """
    url = f"http://api.bilibili.com/archive_stat/stat?aid={aid}&type=jsonp"
    page = requests.get(url, headers=headers)
    js = json.loads(page.text)
    keysname = ['view', 'danmaku', 'reply', 'favorite', 'coin', 'share', 'like']
    for key in keysname:
        # 将数据添加到字典中
        videoDict[key] = js["data"][key]


def get_videoTag(aid):
    """
    获取视频Tag
    :param aid: 视频aid
    :return: 存储tag的列表
    """
    url = f"http://api.bilibili.com/x/tag/archive/tags?aid={aid}"
    page = requests.get(url, headers=headers)
    js = json.loads(page.text)
    tag_names = list()
    for i in js["data"]:
        tag_name = i["tag_name"]
        tag_names.append(tag_name)
    return tag_names


def get_videoMsg(uid, name, all_data):
    """
    获取up投稿视频（前一百个）
    :param uid: up主id
    :param name: 昵称
    :param all_data:存储最终结果的列表
    :return: None
    """
    zoneApi = f"http://api.bilibili.com/x/space/arc/search?mid={uid}&ps=100"
    html = requests.get(zoneApi, headers=headers)
    js = json.loads(html.text)
    # print(html, end='')  # 状态码测试

    for videoMsg in js['data']['list']['vlist']:
        # 创建存储数据的列表
        videoDict = {"uid": uid, "name": name}
        # 要筛选的数据字段
        keysName = ['title', 'aid', 'video_review', 'typeid']
        # 单独获取时间戳
        createTime = videoMsg['created']
        ret = time.localtime(createTime)
        videoDict['time'] = time.strftime("%Y-%m-%d %H:%M:%S", ret)
        # 存储数据到字典
        for key in keysName:
            videoDict[key] = videoMsg[key]
        # 字典添加到列表中
        all_data.append(videoDict)


headers = {
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
}


# 获取百大up主名单
url = "https://www.bilibili.com/activity/web/view/data/814?csrf=352cdb849904ef11e483b5afd7f7be24"
html = requests.get(url, headers=headers)
js = json.loads(html.text)
upMsg = []
for up in js['data']['list']:
    data = up["data"]
    keysName = ["name", "uid"]
    person = dict()
    for key in keysName:
        person[key] = data[key]
    upMsg.append(person)


# 存储所有数据的列表
all_data = []
# 遍历每个人的名称，id。爬取所有视频名称与Aid
for up in upMsg:
    name = up["name"]
    uid = up["uid"]
    get_videoMsg(uid, name, all_data)
    randDelay(2, 4)

# 遍历中的aid，获取所有视频的详细信息
for dta in all_data:
    aid = dta["aid"]
    # 获取视频标签
    dta['tag'] = get_videoTag(aid)
    randDelay(2, 4)
    # 获取视频数据
    get_videoData(aid, dta)
    randDelay(2, 4)

print(all_data)