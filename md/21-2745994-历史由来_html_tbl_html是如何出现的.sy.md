---
show: step
version: 1.0
enable_checker: true
---

# h1 - h6 标题元素

## 回忆

- 上次看了各种优秀作品
- 这些标签都是怎么来的呢?

### 溯源

- 我们现在的html版本是
	- html5

- 如果搜索html1
	- 会如何呢?

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240702-1719923522310)

- 得到了一个
	- txt
	- 纯文本文档

### 尝试下载


- 下载并观察
	- 这是一篇关于html1的草案
	- ietf的草案

```
wget https://www.w3.org/MarkUp/draft-ietf-iiir-html-01.txt
wc draft-ietf-iiir-html-01.txt
```

- ietf
	- 国际互联网工程任务组
	- The Internet Engineering Task Force

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240702-1719923635942)

- 如果下不了
	- 可能是因为缺乏外网权限
	- 可以直接打开
	- https://www.w3.org/MarkUp/draft-ietf-iiir-html-01.txt

### 草案文本

- 使用的字符集是latin-1
	- 说明网页最早起源于西欧

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240702-1719925448734)

- 15页描述了
	- 6种 标题元素(headings)
	- h1-h6

### 具体定义

- 16页给出了具体定义
	- 以及 具体的字体变化

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240702-1719925596712)

- h1元素
	- 需要大写H1
	- 加粗、加大、剧中
	- 前后空1-2行
	- 如果在纸张上
		- 就另起一页
- 整个草案的输出目标媒介
	- 是A4纸张

### p元素登场

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240702-1719925847095)

- 渲染建议
	- 段落之间
	- 纵向间距半行

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240702-1719925861135)

### title元素

- title元素
	-  应该出现在文档的head中

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240702-1719925939263)

### em元素

- 当时给出的渲染效果建议
	- 斜体字

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240702-1719926035979)

- 显然浏览器遵从了这个建议

### 落款

- 最后是作者署名
- 两位作者提出了草案
	- Tim  Berners-Lee(瑞士)
	- Daniel Connolly(美国)

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240702-1719926256154)

- 这俩是谁啊?

### Daniel Connolly

- 1990年毕业之后
	- 对于语义网络很感兴趣
	- 加入了ietf Internet Engineering Task Force 
	- internet工程任务组 

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240702-1719927313707)

### 进入w3名人堂

- https://www.w3.org/People/Connolly/

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240702-1719926973205)

- 通过刚出现的电子邮件进行交流

### Tim Berners—Lee

- 在欧洲的原子能中心工作

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240702-1719927522003)

- 这两个人怎么会有交集呢?

### 邮件列表

- Tim 发起了 一个邮件列表
	- 主题就是www
	- world wide web
	- 万维网

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240703-1720011394475)

- 这相关域名
	- 就是www开头


### www

- 用一种网页的方式服务访问者

- Tim并着手制作
	- 能够解析html的浏览器
- Dan 在里面响应了他
	- 并提供支持

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240702-1719927723032)

- 这里面还提到了标签的起源

### 最早的标签
- http://info.cern.ch/hypertext/WWW/MarkUp/Tags.html
	- 这里面提到了
	- 开始和结束标签

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240702-1719928076976)

- 还有p和headings

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240702-1719928120138)

### 总结 
- 这次研究了html的由来
	- 有了网络之后
	- 出现了电子邮件
	- 和邮件列表
- 欧洲和美洲的两个年轻人
	- talk出一种超文本标记语言
	- 通过邮件列表交流 实现浏览器的方式

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240702-1719928244613)

- 列表这中文字结构也有对应的标签吗?🤔
- 下次再说！👋
