---
show: step
version: 1.0
enable_checker: true
---

# head元素

## 回忆

- 上次我们学习了body元素
- body元素和html元素一样
	- 也是由开始和结束标签构成的
		- 开始标签 
			- start tag
			- `<body>`
		- 结束标签
			- end tag
			- `</body>`
- 如果html、head、body不存在或不完整
	- 浏览器也会帮我们补全这些框架

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221120-1668935070920)

- 如果我们偏偏搞颠倒会如何呢？🤪
	- head在下
	- body在上

### 构建

- <kbd>ctrl</kbd> + <kbd>c</kbd>
	- 结束上一个火狐进程
	- 回到vim
- 修改文档如下

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221120-1668934931773)

- 保存并用火狐浏览网页

### 再次浏览

- <kbd>f12</kbd> 检查元素

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20220908-1662624148010)

- 已经帮我们进行改成了标准结构
	- html元素依然是根
	- html根下依然是两个元素
		- 先 head
		- 后 body
- 浏览器是如何理解源代码的呢？

### view source

- 鼠标右键
	- 查看源文件

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221206-1670320718534)

- 浏览器可以看到源代码
- 但是标红了head的开始和结束标签
- 把鼠标移动到红线上面

### 浏览器提示

- stray start tag "head"

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221206-1670320783957)

- 什么是stray呢？

### stray

- stray 来自于 古法语
	- 来自古法语 estraier, 漫游，流浪，偏离

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221206-1670320983565)

- 在大街上的流浪汉
	- street people
- 浏览器显然认为head元素
	- 已经离家出走了
- 再去whatwg查看一下文档


### 查询

- 去关于head定义的字典查询
	- https://html.spec.whatwg.org/multipage/semantics.html#the-head-element

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20220908-1662623104626)

- head 号称 html里面 第1个元素
	- 元素之间是有层次关系的一棵树
- 可以看看这个树的结构么？

### 树形结构

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221206-1670315898562)

- 选中html开始标签
	- 观察最后一行
		- 发现页面元素和结束标签都变蓝

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221120-1668935360592)

- html元素下面两个元素
	- 先是head

### head

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20220908-1662624449075)

- 后是body

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221120-1668935401049)

- 这两个元素的次序固定
- 试着搜索文本

### 搜索body

- 搜索body
	- 有2个匹配
	- 2个匹配在同一行
	- 先匹配的是body元素
	- 回车之后
	- 再匹配body文本

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221120-1668935453282)

- 搜索head
	- 可以跳转到head元素的位置

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221120-1668935484677)

- 如果搜索文本`am` 呢？

### 搜索文本

- 搜索文本可以跳转到文本相应的位置

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221120-1668935526560)

- 这个结构我理解了
	- 可以在html源文件体现出这个结构吗？

### 缩进体现结构

- 关闭火狐
	- 回到vim
- 在正常状态下输入
	- <kbd>g</kbd><kbd>g</kbd><kbd>=</kbd><kbd>G</kbd>
	- 进行自动缩进

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221120-1668936137903)

- 自动缩进之后
	- 网页的层次结构非常清晰
	- html是根
		- head和body是子元素
- 不过次序还有点问题

### 调整次序

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221120-1668936274194)

- :5,6m1
	- 把从第5到第6行
	- m(move/移动)到第1行下面

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221120-1668936289620)

- head元素
	- 是html下面的第1个元素
	- 然后才是body
- 我们总结去

### 总结
- 这次我们了解了head元素
- head元素
	- 也是由开始标签和结束标签来组成
		- 开始标签
			- `<head>`
		- 结束标签 
			- `</head>` 
	- 开始和结束两个标签一起封闭起来
	- 构成一个head元素
- 根是`<html>`
	- `<html>`里面两个子元素
	- `<head>`和`<body>`
- `<body>`里面
	- 是网页的具体内容
- `<head>`里面
	- 是什么呢?🤔

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20221206-1670320477048)

- 下次再说！👋


