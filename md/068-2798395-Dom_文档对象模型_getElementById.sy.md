---
show: step
version: 1.0
enable_checker: true
---

# 图片元素

## 回忆

- 上次找到了表单form中的button元素
	- button元素的onclick可以触发js代码
		- alert 对话框
		- console.log 命令行
		- document.write 直接写文档
		- 都成功了
- 但是这个document.write直接把文档清空了
- 我想在指定的位置显示输出可以吗？

### 复现

```
<button type=button onclick="document.write('yes')">
 Show hint
</button>
```

- 执行效果

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240815-1723679609263)

- 这document到底什么意思呢？

### 观察

- 在控制台中输入

```
document
```

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240815-1723679727044)

- document是一个对象
	- 小三角可以打开
	- 里面有很多成员

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240815-1723679751430)

- 和window.alert中的window
	- 是什么关系呢？

### window和 document

- window是
	- 窗口
- document是文档
	- 是窗口中的文档
	- 是window中的对象

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240815-1723686993709)

- document文档中可以找到
	- 元素对象吗？

### 找到函数

```
document.getElement
```

- id可以得到唯一的元素
	- 其他的都得到的是元素组

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240815-1723679944998)

- 目前所有元素都没有id
	- 给body一个id试试

### 修改

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240815-1723680357674)

- 然后再次运行

### 运行结果

- 得到了这个button元素

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240815-1723682809336)

- 找到button元素的
	- 内部文本
	- innerText

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240815-1723682815051)

- 尝试设置
	- b1元素的内部文本
	- innerText

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240815-1723682824450)

- 既然如此
	- 我要建立一个段落
	- paragraph
- 通过点击
	- 修改段落的文本

### 代码

```html
    <button id="b1" type=button onclick="document.getElementById('p1').innerText = 'clicked!'">
         press me
    </button>
    <p id="p1">i am paragraph text!</p>
```

- 点击前

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240815-1723683983001)

- 点击后
	- 确实成功了

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240815-1723684169843)

- 可以从文本框里面得到文本吗？

### 文本框

```html
    <input id="i1">
    <button id="b1" type=button onclick="document.getElementById('p1').innerText = document.getElementById('i1')">
         press me
    </button>
    <p id="p1">i am paragraph text!</p>
```

- 运行结果

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240815-1723684414891)

- 怎么得到文本框的值呢？

### 游乐场观察

- 文本框元素的值
	- 就是他的value属性值

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240815-1723684548002)

- 怎么整合到代码里？

```html
    <input id="i1">
    <button id="b1" type=button onclick="document.getElementById('p1').innerText = document.getElementById('i1')">
         press me
    </button>
    <p id="p1">i am paragraph text!</p>
```

### 整合代码

```html
    <input id="i1">
    <button id="b1" type=button onclick="document.getElementById('p1').innerText = document.getElementById('i1').value">
         press me
    </button>
    <p id="p1">i am paragraph text!</p>
```

- 点击之后
	- 就能得到相应的值了

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240815-1723684666784)

- 如果想要根据这个文本框的值
	- 来做分支判断
	- 应该如何呢？

### 总结 🤔
- 这次研究了document对象
- document是
	- 文档对象
	- 是窗口(window)中的文档对象

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240815-1723687189184)

- 在文档(document)中
	- 通过getElementById可以得到具体的元素
	- 然后得到元素的值
	- 也可以对元素属性赋值
- 可以根据这套DOM结构
	- Document Object Model 来做点什么吗？🤔
- 下次再说！👋