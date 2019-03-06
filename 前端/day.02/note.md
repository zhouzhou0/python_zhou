#### 无意义的块级元素 div

```angular2html
<div> 元素没有特定的含义。除此之外，由于它属于块级元素，浏览器会在其前后显示换行。
一般与 CSS 一同使用
<div> 元素的另一个常见的用途是文档布局。它取代了使用表格定义布局的老式方法。
```

### 二、HTML常用的行级标签（行内元素）
不独占一行
### 有语义的行内元素

#### HTML链接 a标签

```angular2html
<a href="链接地址">链接文本</a>
```

target属性，定义被链接的文档在何处显示  _blank 新窗口打开

#### HTML图像

```angular2html
<img src="图片地址" alt="">
```

#### 文本标签
- b标签 i标签 strong标签 em标签

### 无语义的行内元素

- span标签 配合css使用

### 三、常用的实体字符

```angular2html
&gt;&lt;&copy;
```
### 四、表单标签
表单是一个包含表单元素的区域。通过form来定义表单区域
> 通过type属性定义不同类型的表单控件
- text 普通文本输入框
- password 密码输入框
- radio    单选按钮
- checked  多选按钮
- select   下拉框
- file     文件上传选框
- textarea 文本域
- submit   提交按钮
- reset    重置按钮
- hidden   隐藏域，要和表单单一其提交的信息

常用属性：
```angular2html
name 属性：表单项名，用于存储内容值
value属性：输入的值
disabled属性：禁用属性
readonly属性：禁用属性
checked属性：选择框指定默认选项
placeholder：提示
```
**注意：**
```angular2html
form 有两个必须存在的属性 action提交地址 metchod提交方式
post:通过request body传参，参数不可见，参数没有大小限制
get:通url进行传参，参数可见，不安全，大小有限制，

如果表单中含有文件上传 
    method提交方式必须为post 
    form中必须有enctype属性
    enctype="multipart/form-data"