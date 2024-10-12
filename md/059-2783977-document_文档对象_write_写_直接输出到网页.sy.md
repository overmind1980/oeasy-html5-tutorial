---
show: step
version: 1.0
enable_checker: true
---

# 图片元素

## 回忆

- 上次研究了 js在控制台输出的方法
	- 总共有五种输出方式
	- 代表了五种类型的信息

```
<script>
	console.log('console.log()');
	console.info('console.info()');
	console.debug('console.debug()');
	console.warn('console.warn()');
	console.error('console.error()');
</script>
```

- 除了控制台之外
	- 能否将信息直接输出到网页呢？🤔

### 搜索

- 直接搜索

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240809-1723169614143)

- window.alert是直接弹窗
- console.log是书写日志
- 可以试试
	- document.write

### 直接尝试

- 在控制台输入

```
document.write("oeasy")
```

- 在页面上可以直接看到效果

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240809-1723169796003)

- 这可以啊！

### 尝试改造 

- 试试修改这个代码

```
for(i=0;i<=3;i++){
	alert("i===="+i);
}
```

- 动起手来

### 代码

```
<script>
for(i=0;i<=3;i++){
	document.write("i===="+i);
}
</script>
```

- 输出没有问题
	- 但是没有换行

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240809-1723170830648)

- 怎么换行来着？

### 换行

- <br>可以添加换行
	- 将br添加到输出信息中

```
<script>
for(i=0;i<=3;i++){
	document.write("<br>i===="+i);
}
</script>
```

- 输出成功

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240809-1723170979648)

- 可以改出一个九九乘法表吗？

### 调试过程

- 如果程序出了问题
	- 就要到控制台找到问题位置

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240809-1723171430555)

- 上面的问题位于
	- 12行40个字符
	- vim中<kbd>1</kbd><kbd>2</kbd><kbd>G</kbd>
		- 可以迅速切换到第12行


### 九九乘法

```
<!DOCTYPE html>
<html lang=en>
    <head>
        <meta charset="UTF-8">
        <style>
        </style>
        <script>
            for(i=0;i<=9;i++){
                for(j=0;j<=9;j++){
                    document.write(i+"*"+j+"="+i*j + " ");
                }
                document.write("<br>");
            }
        </script>
        <title>Document</title>
    </head>
    <body>
    </body>
</html>
```

- 但是对不齐

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240809-1723171264118)

- 想要把乘法表变得整齐
	- 应该如何呢？

### 总结 

- 这次了解了直接在网页中输出
- 目前三种输出方式
	- window.alert
	- console.log
	- document.write
- 制作九九乘法表的时候
	- 出现问题
	- 不能对齐

![图片描述](https://doc.shiyanlou.com/courses/uid1190679-20240809-1723171264118)

- 应该如何修改呢？🤔
- 下次再说！👋