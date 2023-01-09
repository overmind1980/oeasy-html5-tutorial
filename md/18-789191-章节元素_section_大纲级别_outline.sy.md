---
show: step
version: 1.0
enable_checker: true
---

# h1 - h6 标题元素

## 回忆

- 上次我们了解了标题元素
- 标题一共分为六级
	- 标题一 headings 1
	- 标题二 headings 2
	- 标题三 headings 3
	- 标题四 headings 4
	- 标题五 headings 5
	- 标题六 headings 6
- 有必要分这么多吗？🤔

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670485849589)

- 大纲级别又该怎么理解？

### 等价

- 下面这两个是等价的

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670485952734)

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670485966596)

- 这里面有个没有学过的section元素
- 什么是section呢？

### 查询元素

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670487126436)

- 章节元素(section)代表着文档或者应用的章节
- 一般来说
	- 一个章节就是主题相似的内容
	- 一个章节一般有个章节的标题
- section这个词来自于什么呢？

### section

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670487947035)

- 从整体上切下来的一部分
	- 章节、部门、部分

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670488016115)

- 来自于*sek-
	- 锯子斧头都是用来切的
- 具体怎么切呢？

### 看例子

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670485966596)

- 给 h2 等标题 各领了一个章节
- 这怎么理解呢？

### 标题

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670488474949)

- 每个标题都是一个头目
- 这个头目管的范围不同
- 要把归属理清楚

### 归属关系

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670488731165)

- 一师师长长隶属于一军军长这很明确
- 这个士兵的隶书关系不是很明确

- 这个士兵究竟是
	- 隶属于一军军长
	- 还是隶属于一师师长

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670488778161)

- 怎么让他明确呢？

### 放到section中

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670488965147)

- 士兵隶属于一师师长

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670489012718)

- 士兵隶属于一军军长
- 这就明确了

### 再看代码

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670485952734)

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670485966596)

- 这里面都是头儿
- 但是有层级
	- 军师旅团 营连排班
	- 把各自管辖范围划分清楚了

### 军团编制

- 军团编制其实是调兵谴将

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670490918394)

- 书写文档是遣词造句
- 并且形成了一个文档大纲(outline)
	- 什么是文档大纲呢?

### 大纲

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670505643337)

- 纲就是提网的总绳
	- 所以说纲举目张

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670505884494)

- 纲领是关键是最重要的
	- 所以说提纲挈领

### 文档大纲

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670504952111)

- 将例程中的代码复制进剪贴板
- 然后放进一个检查大纲的网站
	- https://gsnedders.html5.org/outliner/

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670505032614)

### 检查大纲

- 上下两段大纲相同

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670505164943)

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670505174618)

- 其实两段代码本质相同
	- section就是给不同的标题
	- 划定范围

### 大纲

- 标题一层层的
	- 最终会形成一棵树
		- 有次序的大纲树
![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670506120989)

- 如果文档有若干标题
	- 至少有一个得是h1
- 标题下的子标题
	- 标题级别 +1

### 具体例子

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670506706468)

- h4 被升级为 h1

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670506716816)

- 和下图相同

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670506777226)

### 子标题升级

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670506865747)

- h3 会自动升级吗？

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670506881618)

- h3确实会自动升级为h2

### 总结🤔

- 这一次我们研究的是section章节
- 一个完整的网页可以分成
	- 章、节、小节、小小节...
	- 每个部件是一个section
	- 每个section可以有自己的标题
	- 这些标题构成一棵大纲树

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670507219234)

- 标题还有什么好玩的吗?🤔
- 下次再说！👋
