---
show: step
version: 1.0
enable_checker: true
---

# 图片元素

## 回忆

- 上次研究了单选(radio)按钮
	- 也是 常用的 表单(form)项(item)
	- 可以用这些构成比较复杂的测试
	- 并且通过js来计算得分

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240819-1724053570619)

- 可以有彼此不互斥的成组表单项吗？🤔

### checkbox

- 这次的表单项是
	- 复选框
	- type="checkbox"

```
<FORM METHOD="POST" ACTION="http://oeasy.org/sample">
<UL>
<LI>Kent <INPUT NAME="city" TYPE=checkbox VALUE="kent">
<LI>Miami <INPUT NAME="city" TYPE=checkbox VALUE="miami">
</UL>
<P><INPUT TYPE=SUBMIT> <INPUT TYPE=RESET>
</FORM>
```

- 首先看看
	- 提交到服务器的效果

### 提交

- name为city的复选框(checkbox)组
	- 传递过去两个值

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240819-1724056334441)

- 如果把POST方法变成GET呢？

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240819-1724056514834)

### GET

- GET传递没有封装
	- 直接就在url里面

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240819-1724056583577)

- city这个变量
	- 有两个值
	- 同时选中

|类型|type|
|---|---|
|单选按钮|radio|
|复选按钮|checkbox|

- 可以设置复选按钮的默认状态吗？

### 查找文档

- 在whatwg中找到input元素
	- https://html.spec.whatwg.org/multipage/input.html#the-input-element

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240819-1724071063471)

### 构造代码

- 注意油条默认的状态是已选择

```
<FORM METHOD="POST" ACTION="http://oeasy.org/sample">
<UL>
<LI><INPUT NAME="dinner" TYPE=checkbox VALUE="fried" checked>油条
<LI> <INPUT NAME="dinner" TYPE=checkbox VALUE="soy">豆浆
</UL>
<P><INPUT TYPE=SUBMIT> <INPUT TYPE=RESET>
</FORM>
```

- 效果

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240819-1724071690622)

- 可以来一个全选按钮吗？

### 全选按钮

```
<FORM METHOD="POST" ACTION="http://oeasy.org/sample">
<UL>
<LI><INPUT NAME="all" TYPE=checkbox VALUE="select_all" onclick="alert('select all');">全选
<LI><INPUT NAME="dinner" TYPE=checkbox VALUE="fried" checked>油条
<LI><INPUT NAME="dinner" TYPE=checkbox VALUE="soy">豆浆
</UL>
<P><INPUT TYPE=SUBMIT> <INPUT TYPE=RESET>
</FORM>
```

- 尝试运行

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240819-1724072247541)

- 准备构建代码

### js全选

```
<FORM METHOD="POST" ACTION="http://oeasy.org/sample">
<UL>
<LI><INPUT NAME="all" TYPE=checkbox VALUE="select_all" onclick="select_all();">全选
<LI><INPUT NAME="dinner" TYPE=checkbox VALUE="fried" checked>油条
<LI><INPUT NAME="dinner" TYPE=checkbox VALUE="soy">豆浆
</UL>
<P><INPUT TYPE=SUBMIT> <INPUT TYPE=RESET>
</FORM>
<script>
    function select_all(){
        checkbox_list = document.getElementsByName("dinner");
        for(i=0;i<checkbox_list.length;i++){
            checkbox = checkbox_list[i];
            checkbox.checked = true;
        }
    }
</script>
```

- 效果

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240819-1724072757190)

- 这让你想到了什么？

### 清空购物车

- 将购物车全选然后结账...

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240819-1724072901589)

- 这是梦里的感觉

### 总结 🤔

- 这次我们研究的是
	- 多选按钮
	- checkbox 
	- 一组可以选择多个
- 经常用在购物车领域
- 话说互联网购物是如何兴起的呢？

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240820-1724125358031)

- 下次再说！👋

