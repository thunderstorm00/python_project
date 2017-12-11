import requests
def getHttpText(url):
    try:
        r = requests.get(url, timeout = 50)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'find except'

if __name__ == '__main__':
    url = "http://rz.muc.edu.cn:8900"
    print(getHttpText(url))