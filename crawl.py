import requests
from lxml import etree
import pickle
response = requests.get("https://github.com/overmind1980/oeasy-html5-tutorial/tree/master/html")
with open("test.html","wb") as f:
    f.write(response.content)
et_html = etree.HTML(response.content)
et_anchors = et_html.xpath("/html/body/div[4]/div/main/turbo-frame/div/div/div/div[3]/include-fragment/div[2]/div/div/div[2]/span/a")
l = []
if len(et_anchors) != 0:
    for element in et_anchors:
        et_url = element.xpath("@href")
        name = element.text
        url = et_url[0]
        page = [name,url]
        l.append(page)
with open("pages","wb") as f:
    pickle.dump(l,f)
