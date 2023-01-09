---
show: step
version: 1.0
enable_checker: true
---

# lang属性

## 回忆

- 上次我们研究了换行元素
	- br 直接换行
	- wbr 有可能换行的位置
- 文本级的元素
	- 基本了解得差不多了
- 可以看看非文本级别的么
- 比如

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221204-1670160673717)

- 这里的p元素已经见过了很多次了
- 到底啥意思呢？🤔
- 去whatwg查文档

### 去whatwg搜索

- 搜索p元素

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221207-1670418203375)

- p元素 
	- 代表着paragragh
	- 什么意思呢？

### 词源

- paragraph 中有两个词源
	- para
	- graph

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221207-1670418322427)

- 我们一个个来看

### para

- para源于pro
- pro 是英文的拉丁词源
	- 意思是向前的
		- project
		- progress
		- produce
	- 也许是投掷的象声词

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221207-1670419062275)

- 这个发音在北欧为
	- for far fro from

### para

- para 为 旁边

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221207-1670418390488)

- 而且还特指平行
	- parallels

### parallels

- 既不像椭圆(ellipse) 
	- 省略(ellipsis)得不到位
- 也不像双曲线(hyperbola)
	- 夸张(hyperbola)得过分
- 只有抛物线(parabola)
	- 才是最合适的圆锥曲线
	- 能描述出这种遥远的相似性

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221207-1670419136628)

- 那是比较理想的
	- 天堂 paradise
	- 梵语般若 paramita
- para 明白了
- 我们再看看graph

### -graph

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221207-1670420054370)

- -graph来自于carve
	- 雕刻
- 雕刻什么
	- 雕刻图画
- 图画固定下来
	- 成为符号
	- 成为文字

### paragraph

- para(平行的) + -graph(文字)
	- 平行的文字
	- 段落

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221207-1670420462385)

- 但是中文为什么叫做段落呢？

### 段落

- 古人用竹简
	- 一篇文章靠皮绳编

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221207-1670421112144)

- 把这一卷书
	- 按照含义分成段落
	- 也便于理解文章整体含义
- 我们去试试

### 尝试使用

- 大江东去，浪淘尽，千古风流人物。故垒西边，人道是，三国周郎赤壁。乱石穿空，惊涛拍岸，卷起千堆雪。江山如画，一时多少豪杰。

- 遥想公瑾当年，小乔初嫁了，雄姿英发。羽扇纶巾，谈笑间，樯橹灰飞烟灭。故国神游，多情应笑我，早生华发。人生如梦，一尊还酹江月。

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221207-1670422078732)

- 效果如何呢？

### 效果

- 效果是换行

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221207-1670422088957)

- 上次好像也是换行
- 怎么换的来着？

### 回忆上次换行

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20220908-1662643888017)

- 好像不是直接换行的

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20220908-1662643929074)

- 怎么换行来着？

### br

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221207-1670418035773)

- br 就是 换行
	- 意思是line break

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221207-1670418055533)

- 有了br元素换行
	- 为什么还要p

### p元素的作用

- para(平行的) + -graph(文字)
	- 平行的文字
	- 体现这两块文字之间平行的关系

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670464887323)

- 这个p元素什么结构呢？

### 分析p元素

- p元素就像其他html元素一样

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221120-1668951031902)

- 元素由
	- 开始标签(opening tag) 
	- 和 结束标签 (closing tag) 
	- 组成

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221120-1668951045960)

- 开始标签和结束标签之间的
	- 是元素的内容(content)
- p元素里面可以嵌套元素吗？

### 嵌套元素

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221207-1670422078732)

- 尝试着在第一段找到一个重点

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670464952345)

### 再嵌套元素

- 尝试在第二段找到一个强调

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670465048466)

- 强调之中还可以有重点吗？

### 深入嵌套

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670465081197)

- 或许还可以更丰富？

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670465122790)

### 反向包围

- 我是否可以先来个strong

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670465204503)

- 然后把两个段落都放进去

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670465149765)

- 貌似是可以的

### 元素类型

- strong 属于短语内容

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670465544783)

- 什么是短语内容呢？

### 短语内容

- 短语内容

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670465749334)


- 短语内容是文档的文本
	- 在段落内级别标记该文本的元素
	- 短语内容形成段落

- 所以
	- 最好是
		- p 包括着 strong
	- 而不是
		- strong 包括着 p

### 总结 

- 这次学习了p元素
	- paragragh
- p元素可以表示段落
- 段落自动会换行
	- 当然如果文章中有个标题就更好了

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221208-1670467600079)

- 网页内容中应该如何设置标题呢？
- 下次再说！👋
