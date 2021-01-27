#usr/bin/python 3
#-*- encoding:utf-8 -*-
#
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'priceton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

import requests


def getHTMLText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv)
        r.raise_for_status()  # 如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text[:1000]
    except:
        return "产生异常"


if __name__ == "__main__":
    url = "https://www.amazon.com/Jointown-Face-Mask-Pack-50/dp/B086KMYNSS/ref=gbps_img_m-9_475e_5ca69238?smid=ATVPDKIKX0DER&pf_rd_p=5d86def2-ec10-4364-9008-8fbccf30475e&pf_rd_s=merchandised-search-9&pf_rd_t=101&pf_rd_i=15529609011&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=QE5CFPAQJJJ6JDPSSNZ6"
    print(getHTMLText(url))