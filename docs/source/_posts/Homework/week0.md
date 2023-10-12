---
title: Homework | 第一次作业解答
date: 2023-10-09 14:41:44
category: homework
---


**【作业情况】** 1.1题中误判`main`和`sin`；1.2题对（5）（6）题的逻辑短路（惰性求值）不理解；1.3对于误判字符串数组和数组名；1.4不能规范书写C++代码；1.6题主要是后两个变量的值错误率高...其实可以写一小段代码验证，关于结果的解释可以上网搜

<!--more-->

## 判断下列标识符是否合法

> 什么是[标识符](https://learn.microsoft.com/zh-cn/cpp/cpp/identifiers-cpp?view=msvc-170)（[Identifier](https://en.cppreference.com/w/cpp/language/identifiers)）
> 什么是[保留字](https://en.cppreference.com/w/cpp/keyword)（[Keywords](https://learn.microsoft.com/zh-cn/cpp/cpp/keywords-cpp?view=msvc-170)）

1. `sin`：合法，C++标准库的函数名
2. `book`: 合法
3. `5arry`：不合法，不能用数字作为开头
4. `_name`：合法
5. `Example2.1`：不合法，`.`是C++的运算符
6. `main`：合法，只是C++中的一个特殊函数名称
7. `$1`：一般而言视作不合法，但是在Microsoft C++编译器（MSVC）中视为合法，具体见[Microsoft C++标识符](https://learn.microsoft.com/zh-cn/cpp/cpp/identifiers-cpp?view=msvc-170)
8. `class_cpp`：合法
9. `a3`：合法
10. `x*y`：不合法，`*`是运算符，表示的是表达式
11. `my name`：不合法，中间含有空格

> **关于为什么`main`和`sin`是合法的标识符**
> 
> 可以用以下代码来验证：
> 
> ```cpp
> #include <iostream>
> using namespace std;
> 
> int main() {
>     auto main = 1;
>     auto sin = 0.8;
>     cout << "idetifier 'main' = " << main << endl;
>     cout << "idetifier 'sin' = " << sin << endl;
>     return 0;
> }
> ```
> 
> 得到的输出是`1`和`0.8`（其中`auto`的自动类型推断告诉我们`main`是一个类型为`int`的变量，`sin`是一个类型为`float`的变量）

## 求表达式的值以及运算后表达式所涉及的各变量的值

```
case 1:
  x + (int)y % a: float = 4.5
  x: float = 2.5
  y: float = 8.2
  a: int = 3
case 2:
  (x = z * b++, b = b * x, b++): int = 42
  x: float = 7
  z: float = 1.4
  b: int = 43
case 3:
  (ch4 = ch3 - ch2 + ch1): char = \
  ch4: char = \
  ch3: char = 0
  ch2: char = 5
  ch1: char = a
case 4:
  int(y / z) + (int)y / (int)z: int = 13
case 5:
  !(a > b) && c && (x *= y) && b++: bool = 0
  x: float = 2.5
  b: int = 5
case 6:
  ch3 || (b += a * c) || c++: bool = 1
  b: int = 5
  c: int = 0
case 7:
  z = (a << 2) / (b >> 1): float = 6
```

> **case 1**
> 主要注意【强制转换】和【算数运算符】的优先级，查优先级表可以知道【强制转换】的优先级更高，从左到右运算后得到表达式的值是4.5，整个表达式不存在赋值操作，因此没有变量的值被改变

> **case 2**
> 这里给了3个【赋值】表达式。第一个表达式注意【后缀自增】运算的优先级更高

> **case 3**
> 字符的运算。相当于对应ASCII码的运算，而不是字符的拼接和剪切。计算得到的`ch4 = 92`或者`ch4 = '\\'`。注意第一个`\`是转义。注意区分'\'和'/'是不一样的符号

> **case 4**
> 基本没问题，注意是整除

> **case 5**
> 逻辑短路。
> 从左到右先计算`a>b`为`false`，取非后为`true`，不能决定最后表达式的值
> 接着计算`c`的值为`0`
> 由于是连续的`&&`与运算，`c`的值已经决定了整个表达式的值（你说为什么C++这么聪明，聪明的是某些编译器啦~课程指路：[编译原理](https://www.bilibili.com/video/BV1cW411B7DW/?spm_id_from=333.337.search-card.all.click)）

> **case 6**
> 和上一题一样

> **case 7**
> 注意`a,b`的值不会改变

## 判断哪些是常量，哪些是变量

- `"China"`: 常量
- `const int n=10;`：常量
- `int m=5;`：变量
- `'a'`：常量
- `char ch='a';`：变量
- `int array[5]={1,2,3,4,5};`：指针类型，`array`是常量，`array[0]...array[4]`是变量
- `char s[ ]="Hello";`：常量

> 关于`const`的[用法](https://learn.microsoft.com/zh-cn/cpp/cpp/const-cpp?view=msvc-170)
> 关于指针的内容可以先跳过

## 将下列表达式或叙述用C++描述

`3.14 / 2 + sqrt(pow(asin(x), 2) + pow(c, 2))`
`(x + y) / ((x - y) * pow(a, y))`
`(x * x + y * y > pow(min(a, b), 2) && (x * x + y * y < pow(max(a, b), 2)`
`(a != b) && (b != c)` 或者 `(a != b) && (b != c) && (a != c)`
`(k <= 20) && (ch != '\0')`

> 基本没问题，第三问没有说明`a,b`的大小关系，上述为较为标准写法（别钻牛角尖了，合理答案都是对的）

## 求程序运行后各变量的值

```
a=3  b=2  x=1.8  y=7  ch1='a'   ch2=' '  ch3='b'
```
注意`' ' != '\0'`

> `cin.get()`的用法，它与`<<`等运算符的区别（建议用[这篇文章](../Notes/about-course.md)的方法去搜索）