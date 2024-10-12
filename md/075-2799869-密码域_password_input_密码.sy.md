---
show: step
version: 1.0
enable_checker: true
---

# 图片元素

## 回忆

- 上次了解了亚马逊
	- 世界上最大的电子书店
	- 从图书目录开始
	- 在没有实体店和仓库的情况下
	- 做成了世界上最大的网上书店

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240823-1724420988868)

- 登陆电视商务网站
	- 肯定需要密码
- 密码是如何录入系统的呢？🤔

### 最初结构

- https://www.w3.org/MarkUp/html-spec/html-spec_8.html#SEC8.2.4

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240825-1724572158218)

- 将name这个input的type设置为password

### 目前代码

```
<FORM METHOD="POST" ACTION="http://oeasy.org/fun">
<P>Your name: <INPUT NAME="name" TYPE="password">
<P><INPUT TYPE=SUBMIT> <INPUT TYPE=RESET>
</FORM>
```

- 运行效果
	- 文本框中输入的按键
	- 都看不到具体的字符
	- 起到了保密的作用

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240825-1724573394823)

- 提交效果
	- 提交的时候
	- 能够把输入的字符正确提交到服务器

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240825-1724573410894)

- 密码这块又有什么常用的吗？

### 对密码进行判断

``` html
<form id="myForm">
    密码: <input type="password" id="password">
    <input type="button" value="提交" onclick="check()">
  </form>

  <p id="errorMessage"></p>

  <script>
    function check(){
      var password = document.getElementById("password").value;
      var hasUpperCase = false;
      var hasLowerCase = false;
      var hasNumber = false;

      for (var i = 0; i < password.length; i++) {
        var char = password.charAt(i);
        if (/[A-Z]/.test(char)) {
          hasUpperCase = true;
        } else if (/[a-z]/.test(char)) {
          hasLowerCase = true;
        } else if (/[0-9]/.test(char)) {
          hasNumber = true;
        }
      }

      if (!hasUpperCase ||!hasLowerCase ||!hasNumber) {
        document.getElementById("errorMessage").innerHTML = "密码必须包含大写字母、小写字母和数字";
      }
    }
  </script>
```

- 这样要求
	- 密码必须包含大写字母、小写字母和数字

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240825-1724593344421)

- 刷新网页
	- 符合要求之后
	- 也不提交？

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240825-1724593396858)

- 这怎么办？

### 提交表单

- 两处修改
	- 设置form 表单元素的属性
		- method 提交方法
		- action 提交地址
	- check检查函数的结尾
		- 通过id得到表单form
		- 然后将表单提交

```
<form id="myForm" method="get" action="http://oeasy.org/o">
    密码: <input type="password" id="password">
    <input type="button" value="提交" onclick="check()">
</form>

<p id="errorMessage"></p>

<script>
function check(){
  var password = document.getElementById("password").value;
  var hasUpperCase = false;
  var hasLowerCase = false;
  var hasNumber = false;

  for (var i = 0; i < password.length; i++) {
    var char = password.charAt(i);
    if (/[A-Z]/.test(char)) {
      hasUpperCase = true;
    } else if (/[a-z]/.test(char)) {
      hasLowerCase = true;
    } else if (/[0-9]/.test(char)) {
      hasNumber = true;
    }
  }

  if (!hasUpperCase ||!hasLowerCase ||!hasNumber) {
    document.getElementById("errorMessage").innerHTML = "密码必须包含大写字母、小写字母和数字";
  }
  else{
	var form = document.getElementById("myForm");
	form.submit();
  }
}
</script>
```

- 表单可以提交
	- 但是不能传递参数

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240825-1724594815030)

- 这是为什么呢？

### 观察

- 注意能够传递参数的属性是name

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240827-1724763700952)

- 如果我们把id变成name就可以吗？

### 试试看

- 点击提交按钮

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240827-1724764046153)

- 无效😳

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240827-1724764076027)

- 第10行有错
	- 因为找不到id为password的元素了

### 修改

- 密码域需要两个属性

|属性名称|作用|
|---|---|
|name|传递表单数据|
|id|js得到元素进行操作|

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240827-1724764237371)

- 改成这样
	- js可以找到吗？

### 再试

- 再点击提交

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240827-1724764300946)

- 这次可以看到
	- 参数传递已成功
	- get参数在url上有显示
- 除了
	- 大写
	- 小写
	- 数字
	- 还想要特殊字符

### 最终代码

```
<form id="myForm" method="get" action="http://oeasy.org/o">
    密码: <input type="password" name="password" id="password">
    <input type="button" value="提交" onclick="check()">
</form>

<p id="errorMessage"></p>

<script>
function check(){
  var password = document.getElementById("password").value;
  var hasUpperCase = false;
  var hasLowerCase = false;
  var hasNumber = false;
  var hasSpecialChar = false;

  for (var i = 0; i < password.length; i++) {
    var char = password.charAt(i);
    if (/[A-Z]/.test(char)) {
      hasUpperCase = true;
    } 
    else if (/[a-z]/.test(char)) {
      hasLowerCase = true;
    } 
    else if (/[0-9]/.test(char)) {
      hasNumber = true;
    }
    else if (/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(char)) {
      hasSpecialChar = true;
    }
  }

  if(!hasSpecialChar||!hasUpperCase ||!hasLowerCase ||!hasNumber) {
    document.getElementById("errorMessage").innerHTML = "密码必须包含大写字母、小写字母、数字、符号";
  }
  else{
	var form = document.getElementById("myForm");
	form.submit();
  }
}
</script>
```

### 总结 🤔

- 这次研究了密码域(password)
	- 密码域在填写的时候不回显
- 两个属性 各有各的用处

|属性名称|作用|
|---|---|
|name|传递表单数据|
|id|js得到元素进行操作|

- 还有什么好用的表单控件吗？🤔
- 下次再说！👋

