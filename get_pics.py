import pickle
import requests
from lxml import etree
import os
with open("pages","rb") as f:
    l = pickle.load(f)
print(l)

for page in l:
    folder_name = page[0]
    page_name = page[1]
    print("---page---------", folder_name, page_name, end="\n")
    url = "https://github.com/" + page_name + "/" + folder_name + ".sy.md"
    print("1===========")
    print(url)
    print("2==========")
    response = requests.get(url)
    et_html = etree.HTML(response.content)
    folder_name = folder_name.replace(")","").replace("(","")
    os.system("mkdir content/" + folder_name)
    with open("./content/" + folder_name+".html","wb") as f:
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
        with open("./content/" + folder_name + "/" + file_name + ".jpg","wb") as f:
            f.write(img_content)
        print(img_url)
