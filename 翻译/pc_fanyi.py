# 解析传进来的url地址，并输出相应信息
import urllib.request
import urllib.parse
# json模块序列化讲字典转换为字符串
import json
import sys

def transatle(content):
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    head = {}
    head["User_Agent"] = "eWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    data = {}
    data["i"] = content
    data["from"] = "AUTO"
    data["to"] = "AUTO"
    data["smartresvlt"] = "dict"
    data["client"] = "fanyideskweb"
    data["salt"] = "16821711844874"
    data["sign"] = "8886728a34723159df64faf11466b5ba"
    data["lts"] = "1682171184487"
    data["by"] = "5687269bfcf3c2e21217e8ca4cbd18bd"
    data["doctype"] = "json"
    data["version"] = "2.1"
    data["keyfrom"] = "fanyi.web"
    data["action"] = "FY_BY_CLICKBUTTION"
    data = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(url, data, head)
    respond = urllib.request.urlopen(req)
    html = respond.read().decode("utf-8")
    targe = json.loads(html)
    dic_result = targe["translateResult"][0][0]["tgt"]
    return dic_result
