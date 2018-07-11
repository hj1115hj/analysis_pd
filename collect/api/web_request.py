import sys
from urllib.request import Request, urlopen  #모듈 가져오기
from datetime import *
import json



def print_error(error):
    print('%s %s' % (error, datetime.now()), file=sys.stderr)

def html_request(
    url = '',
    encoding ='utf-8',
    success= None,
    error = lambda e: print('%s %s' % (e,datetime.now()), file=sys.stderr)

):
    try:
        request = Request(url)
        resp = urlopen(request)  # 응답 받기
        html = resp.read().decode(encoding)  # 응답 읽기 (바디 내용)  - 바이트로 통신    인코딩 했으면 디코딩도 해야함

        print('%s :success for request[%s]' %(datetime.now(), url) )
        print(html)  # 네이버 바디(코드)를 가져옴


        if callable(success) is False: #호출가능한지 확인
            return html

        success(html)

    except Exception as e:
        if callable(error) is True:
            error(e)


def json_request(
    url = '',
    encoding ='utf-8',
    success= None,
    error = lambda e: print('%s %s' % (e,datetime.now()), file=sys.stderr)

):
    try:
        request = Request(url)
        resp = urlopen(request)  # 응답 받기
        html = resp.read().decode(encoding)  # 응답 읽기 (바디 내용)  - 바이트로 통신    인코딩 했으면 디코딩도 해야함
        json_result = json.loads(html)


        print('%s : success for request[%s]' % (datetime.now(), url))
        if callable(success) is False: #호출가능한지 확인
            return json_result

        return success(json_result)

    except Exception as e:
        if callable(error) is True:
            error(e)


