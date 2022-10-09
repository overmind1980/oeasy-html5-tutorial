import requests
from lxml import etree
url = "https://github.com/overmind1980/oeasy-html5-tutorial/blob/master/md/01-563148-%E4%BF%AE%E6%94%B9%E7%9A%84%E4%B9%90%E8%B6%A3.sy.md"
response = requests.get(url)
et_html = etree.HTML(response.content)
with open("detail_page","wb") as f:
    f.write(response.content)
et_imgs = et_html.xpath("/html/body/div[4]/div/main/turbo-frame/div/div/div/readme-toc/div/div[2]/article/p/a/img")
for img in et_imgs:
    img_url = img.xpath("@data-canonical-src")[0]
    pos = img_url.rindex("/")
    print(pos,type(pos))
    length = len(img_url)
    print(length,type(length))
    file_name = img_url[pos+1:length]
    print(file_name)
    img_response = requests.get(img_url)
    img_content = img_response.content
    with open("img/"+file_name,"wb") as f:
        f.write(img_content)
    print(img_url)
