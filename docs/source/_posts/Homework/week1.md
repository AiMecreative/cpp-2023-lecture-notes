---
title: Homework | 第一次作业解答
date: 2024-03-11 17:19:45
category: Homework
---

春季学期第一周作业答案，反馈已经发送。本次作业需要主要关注类及其构造函数、成员函数的定义和使用，其中第二题的矩形初始化需要注意题意为初始化对角线顶点坐标

<!--more-->

# question 0

```cpp
/**
 * 题目1：试建立一个类 Student 用于描述学生信息，具体要求如下：
 *         私有数据成员
 *                 int id: 学生学号。  char name[20]。姓名
 *                 char yuwen: 语文成绩（五级分制：A、B、C、D和E，其它无效）。
 *                 double shuxue: 数学成绩（百分制）。
 *         公有成员函数
 * 1)	缺省构造函数（无参数的构造函数）：初始化数据成员为0或空值。
 * 2)	带参构造函数：用参数初始化数据成员。
 * 3)	void Print( ): 输出本对象的学号、语文成绩和数学成绩。
 * 4)	修改函数void set(int ID, char nm[], char score, int ma
 * )：从键盘输入新的学号、语文成绩和数学成绩，修改相应数据成员的值。
 * 主函数可以这样测试定义类
 * int main(void)
 * {
 *      Student stu1(61101, “wang M”,'E',86),  stu2(61102, “Li M”,'D',82), stu3;
 *      stu3.set(61103, “zhang M”,‘A’, 90);
 *      stu1.Print();
 *      stu2.Print();
 *      stu3.Print();
 *      return 0;
 * }
 */

#include <cassert>
#include <cstring>
#include <iostream>
#include <string.h>

using namespace std;

// 使用全局常量定义名字的长度
const size_t name_length = 20;

// 助教编码风格，类名大驼峰命名
class Student {
  // 定义私有成员变量
  // 助教编码风格是在私有成员前加下划线
private:
  int _id;
  char _name[20];
  char _chiese; // A,B,C,D,E
  double _math; // 0-100

public:
  // 默认构造（或称为无参构造）
  // 另一种写法是
  // Student() = default;
  Student() {
    // 事实上使用负数初始化更好，可以分辨数据的合理性
    // 例如一名同学的数学成绩是0分，或者学号是0，用负数初始化后可以区分该同学的数据是否已经赋值
    _id = -1;
    for (unsigned _ = 0; _ < name_length; _ += 1) {
      _name[_] = '\0';
    }
    _chiese = '\0';
    _math = -1;
  }

  Student(int id, const char *name, char chiese, double math) {
    // 由于是数据与学生相关，要在函数体内进行数据合法性验证
    // 使用assert断言
    assert(id >= 0 && strlen(name) <= name_length && 'A' <= chiese &&
           chiese <= 'E' && 0 <= math && math <= 100);
    _id = id;
    strcpy_s(_name, name);
    _chiese = chiese;
    _math = math;
  }

  void set(int id, const char *name, char chiese, double math) {
    // 注意检查数据的合理性
    // 使用assert断言
    assert(id >= 0 && strlen(name) <= name_length && 'A' <= chiese &&
           chiese <= 'E' && 0 <= math && math <= 100);
    _id = id;
    strcpy_s(_name, name);
    _chiese = chiese;
    _math = math;
  }

  // 助教编码风格，公有成员函数名小驼峰命名
  void print() {
    cout << "========Student========" << endl;
    cout << "student id: " << _id << endl;
    cout << "student Chinese score: " << _chiese << endl;
    cout << "student Math score: " << _math << endl;
    cout << "=======================" << endl;
  }
};

int main() {
  Student stu1(61101, "wang M", 'E', 86);
  Student stu2(61102, "Li M", 'D', 82);
  Student stu3;
  stu3.set(61103, "zhang M", 'A', 90);

  stu1.print();
  stu2.print();
  stu3.print();

  return 0;
}

// 事实上在实际项目中，学号或者编号之类的存储不用int
```

# question 1

```cpp
/**
 * 题目2. 课本 P151  题4.4  建立一个矩形类Rectangle
参考的主函数测试为：
包含测试两种构造函数，输出显示成员函数，计算面积和周长的成员函数；
int main()
{
        Rectangle rect;
        rect.Show();
        rect.set(100,400,300,200);
        rect.Show();
        Rectangle rect1(0,200,200,0);
        rect1.Show();
        cout<<"面积"<<rect.Area()<<'\t'<<"周长"<<rect.Perimeter()<<endl;
        return 0;
}
class Rectangle
{
        int x1,y1,x2,y2;
public:
        Rectangle(int a,int b,int c,int d)
        {
                x1 = a; y1 = b; x2 = c; y2 = d;
        }
        Rectangle()
        {
                x1 = 0; y1 = 0; x2 = 0; y2 = 0;
        }
             ……..

 */

#include <cassert>
#include <cmath>
#include <corecrt_math.h>
#include <iostream>

using namespace std;

// 值得注意的是，该矩形是轴平行矩形
class Rectangle {

private:
  // 定义矩形的对角线坐标
  double _x1;
  double _y1;
  double _x2;
  double _y2;

  double _width;
  double _height;

public:
  // 由于都是数据，可以直接用初始化列表
  Rectangle() : _x1(0.), _y1(0.), _x2(0.), _y2(0.), _width(0.), _height(0.) {}
  Rectangle(double x1, double y1, double x2, double y2) {
    // 对参数进行检查，可以使用assert，具体用法可以自行查找
    // 翻译就是：断言宽高都大于0，否则抛出异常
    assert(x1 != x2 && y1 != y2);
    _x1 = x1;
    _y1 = y1;
    _x2 = x2;
    _y2 = y2;
    _width = fabs(_x1 - _x2);
    _height = fabs(_y1 - _y2);
  }

  // 下面函数的const可以省略
  double perimeter() const { return 2. * (_width + _height); }
  double area() const { return _width * _height; }
  void set(double x1, double y1, double x2, double y2) {
    assert(x1 != x2 && y1 != y2);
    _x1 = x1;
    _y1 = y1;
    _x2 = x2;
    _y2 = y2;
    _width = fabs(_x1 - _x2);
    _height = fabs(_y1 - _y2);
  }
  void show() {
    cout << "rectangle corners: ";
    cout << "Point(" << _x1 << ", " << _y1 << "), ";
    cout << "Point(" << _x2 << ", " << _y2 << ")" << endl;
  }
};

int main() {
  Rectangle rect1;
  rect1.show();
  rect1.set(100, 400, 300, 200);
  rect1.show();

  Rectangle rect2(0, 200, 200, 0);
  rect2.show();
  cout << "area of rect2: " << rect2.area() << endl;
  cout << "perimeter of rect2: " << rect2.perimeter() << endl;

  return 0;
}
```

# question 2

```cpp

/**
 * 题目3  补充完整建立一个分数类。
(1)增加复制构造函数，完成对象的复制，并在主程序中测试;
(2) 实现加法add功能，减法subtract 功能，并测试；
(3) 增加判断和另外一个分数是否相等 IsEqual的功能，并测试；
class fraction
{	int above;  //分子
        int below;  //分母
        void reduction();  //约分
               fraction makecommond(fraction b);  //通分
public:
        fraction(int =0,int =1);    //构造函数
        //加法
               // 减法
        void display();//显示
        void input();//输入

   // 按照要求添加函数
};
int main()
{
     fraction a(1,2), b(5,15), c;
     a.display();
     b.display();

     c=a.add(b);
     c.display();

     c=b.substract(a);
     c.display();

     if(a.IsEqual(b))
             cout<<“相等”;
      else
             cout<<“不等”;
     return 0;
}
 */

#include <algorithm>
#include <iostream>
using namespace std;

class Fraction {
private:
  int _above;
  int _below;

  // 最大公约数
  int _gcd(int a, int b) {
    for (int g = min(a, b); g > 0; g -= 1) {
      if (a % g == 0 && b % g == 0) {
        return g;
      }
    }
    return -1;
  }

  // 最小公倍数
  int _lcm(int a, int b) {
    for (int l = max(a, b); l <= a * b; l += 1) {
      if (l % a == 0 && l % b == 0) {
        return l;
      }
    }
    return -1;
  }

public:
  // 默认构造
  Fraction() : _above(0), _below(0) {}
  // 有参构造
  Fraction(int above, int below) : _above(above), _below(below) {}
  // 拷贝构造
  Fraction(Fraction &other) : _above(other._above), _below(other._below) {}

  // !注意这里把约分和通分作为公有函数接口，更加合理

  // 约分
  void reduction();

  // 通分
  // !注意这里与题目要求不一致但更加合理
  // !通分是本对象与另一个分数通分，但不改变另一个分数的分子分母，只改变自身，因此也没有必要有返回值
  void common(const Fraction &other);

  Fraction add(Fraction &other);
  Fraction minus(Fraction &other);

  bool isEqual(Fraction &other);

  void input();
  void display();
};

void Fraction::reduction() {
  int gcd = this->_gcd(_above, _below);
  _above /= gcd;
  _below /= gcd;
}

void Fraction::common(const Fraction &other) {
  int lcm = this->_lcm(_below, other._below);
  int factor = lcm / _below;
  _below *= factor;
  _above *= factor;
}

Fraction Fraction::add(Fraction &other) {
  this->common(other);
  other.common(*this);

  Fraction add_result(this->_above + other._above, this->_below);
  add_result.reduction();
  return add_result;
}

Fraction Fraction::minus(Fraction &other) {
  this->common(other);
  other.common(*this);

  Fraction minus_result(this->_above - other._above, this->_below);
  minus_result.reduction();
  return minus_result;
}

bool Fraction::isEqual(Fraction &other) {
  this->reduction();
  other.reduction();
  return this->_above == other._above && this->_below == other._below;
}

void Fraction::input() {
  cout << "input fraction in order(above, below):";
  cin >> _above;
  cout << " / ";
  cin >> _below;
  reduction();
}

// 这里没有对输出进行格式化，会出现符号问题
void Fraction::display() {
  reduction();
  cout << "fraction: " << _above << " / " << _below << endl;
}

int main() {
  Fraction a(1, 2);
  Fraction b(5, 15);

  a.display();
  b.display();

  Fraction c;
  c = a.add(b);
  c.display();

  if (a.isEqual(b)) cout << "fraction `a` equals to `b`" << endl;
  else cout << "fraction `a` not equals `b`" << endl;

  return 0;
}
```