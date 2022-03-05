import requests
import time


def test_time(html_address):
    start_time = time.clock_gettime(time.CLOCK_BOOTTIME)
    res = requests.get(html_address)
    end_time = time.clock_gettime(time.CLOCK_BOOTTIME)
    delta_time = int((end_time - start_time) * 1000)  # in milliseconds
    print(html_address, res)
    print(f"\t\tResponse time: {delta_time} milliseconds")


test_time('https://google.com')
test_time('https://www.ynet.co.il')
test_time('https://imdb.com')
test_time('https://stackoverflow.com')
test_time('https://youtube.com')
