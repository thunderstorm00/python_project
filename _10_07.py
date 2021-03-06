#使用request，re爬取淘宝网的商品名称和价格
#知识图谱
import requests
import re
def getTxtHtml(url):
    try:
        taobaohtml = requests.get(url)
        taobaohtml.raise_for_status();
        taobaohtml.encoding = taobaohtml.apparent_encoding
        return taobaohtml.text
    except:
        return None;


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


def main():
    goods = '书包'
    depth = 3
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            html = getTxtHtml(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)


main()