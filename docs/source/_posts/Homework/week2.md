---
title: Homework | 第二次作业解答
date: 2024-03-18 16:36:00
category: Homework
---

春季学期第二次作业解答

<!--more-->

# question 0

![question0](t0.png)

```cpp
#include <iostream>

using namespace std;

class Book {
private:
  // 可以定义一个常量，表示最大的库存
  const int MAX_CAP = 10;
  int _no;
  int _cap;
  double _price;
  int _lend;

public:
  // 这里默认构造函数采用的是初始化形参列表，比较简洁
  Book(int no, int cap, double price)
      : _no(no), _cap(cap), _price(price), _lend(0) {}

  // 这些公有函数实现步骤较多，为了不破坏类的可读性，可以放在类外实现
  int input(int num);
  void lendOut(int num);
  void giveBack(int num);

  // 对于一些简单的成员函数直接在类内实现
  int getCap() { return _cap; }
  double getPrice() { return _price; }
  int getLend() { return _lend; }

  void display() {
    cout << "no = " << _no;
    cout << " cap = " << _cap;
    cout << " price = " << _price;
    cout << " lend = " << _lend;
    cout << endl;
  }
};

// 成员函数的实现
int Book::input(int num) {
  if (num + _cap > MAX_CAP) {
    cout << "最多放入 " << MAX_CAP - _cap << " 本" << endl;
    return _cap - MAX_CAP;
  }
  cout << "添加成功" << endl;
  return num;
}

void Book::lendOut(int num) {
  if (num > _cap) {
    cout << "最多能借出" << _cap << " 本" << endl;
    return;
  }
  _lend += num;
  _cap -= num;
  cout << "借出成功" << endl;
  return;
}

void Book::giveBack(int num) {
  int back_num = input(num);
  if (back_num < 0) {
    cout << "最多归还 " << -back_num << " 本" << endl;
    return;
  }
  cout << "归还成功" << endl;
  return;
}

int main() {
  // 基本和题目提供的主函数一致，修改了部分变量名，更加赏心悦目
  Book book_a(101, 2, 35.8), book_b(102, 5, 66.2);
  int stat_a = book_a.input(3);
  int stat_b = book_b.input(8);
  if (stat_a < 0) {
    book_a.input(-stat_a);
  }
  if (stat_b < 0) {
    book_b.input(-stat_b);
  }
  book_a.display();
  book_b.display();

  if (book_a.getPrice() > book_b.getPrice()) {
    book_a.lendOut(3);
    book_b.lendOut(8);
  } else {
    book_a.lendOut(8);
    book_b.lendOut(3);
  }
  book_a.display();
  book_b.display();

  book_a.giveBack(1);
  book_b.giveBack(1);

  book_a.display();
  book_b.display();

  return 0;
}
```

# quesion 1

![question1](t1.png)

```cpp
#include <cassert>
#include <cmath>
#include <iostream>

using namespace std;

class Triangle {
private:
  // 题目中某些逆天变量，一般而言是存储顶点坐标而不是边长
  // 为了保持一致，这里定义边长
  // 由于三边类型一致，直接用数组
  double _edge[3];

public:
  // 默认构造函数
  Triangle(double *edge) {
    // 验证是否能构成三角形
    assert(edge[0] + edge[1] > edge[2] && edge[0] + edge[2] > edge[1] &&
           edge[1] + edge[2] > edge[0]);
    for (unsigned e = 0; e < 3; e += 1) {
      _edge[e] = edge[e];
    }
  }
  // 重载构造函数
  Triangle(double edge_1, double edge_2, double edge_3) {
    assert(edge_1 + edge_2 > edge_3 && edge_1 + edge_3 > edge_2 &&
           edge_2 + edge_3 > edge_1);
    _edge[0] = edge_1;
    _edge[1] = edge_2;
    _edge[2] = edge_3;
  }
  // 复制（拷贝）构造函数
  Triangle(const Triangle &other) {
    for (unsigned e = 0; e < 3; e += 1) {
      _edge[e] = other._edge[e];
    }
  }
  // 析构函数，注意管理内存，由于成员数组也不是new出来的
  // 析构可以为空
  ~Triangle() {}

  // 根据三边计算三角形面积，直接用海伦公式
  double getArea() const {
    double p = 0.5 * (_edge[0] + _edge[1] + _edge[2]);
    double area_2 = p * (p - _edge[0]) * (p - _edge[1]) * (p - _edge[2]);
    return sqrt(area_2);
  }

  double operator+(const Triangle &other);
  double operator-(const Triangle &other);
};

double Triangle::operator+(const Triangle &other) {
  return getArea() + other.getArea();
}

double Triangle::operator-(const Triangle &other) {
  return getArea() - other.getArea();
}

int main() {
  double edge_a[3] = {4.3, 5.8, 3.4};
  Triangle tri_a(edge_a);
  Triangle tri_b(2.2, 1.4, 3.1);
  Triangle tri_c(tri_a);

  // 测试重载符号
  cout << "tri_a - tri_b = " << tri_a.getArea() << " - " << tri_b.getArea()
       << " = " << tri_a - tri_b << endl;
  cout << "tri_b + tri_c = " << tri_b.getArea() << " + " << tri_c.getArea()
       << " = " << tri_b + tri_c << endl;
  return 0;
}
```

# question 2

![question2](t2.png)

```cpp
#include <iostream>
#include <ostream>

using namespace std;

// 注意每天时间的最大值
const int HOURS = 24;
const int MINUTES = 60;
const int SECONDS = 60;

class MyTime {
private:
  int _hour;
  int _minute;
  int _second;

public:
  MyTime() : _hour(0), _minute(0), _second(0) {}
  MyTime(int hour, int minute, int second)
      : _hour(hour), _minute(minute), _second(second) {}

  // 用于实现诸如 --time 的操作
  // 前缀是先改变对象，再返回改变的对象
  MyTime operator--();
  // 用于实现 time-- 的操作
  // 后缀是改变对象，但返回改变前的对象
  MyTime operator--(int);

  // 重载流运算符，用于输出
  friend ostream &operator<<(ostream &output, const MyTime &t) {
    cout << t._hour << " : " << t._minute << " : " << t._second;
    return output;
  }
};

MyTime MyTime::operator--() {
  _second--;
  if (_second < 0) {
    _minute--;
    _second += SECONDS;
    if (_minute < 0) {
      _hour--;
      _minute += MINUTES;
      if (_hour < 0) {
        _hour += HOURS;
      }
    }
  }
  return MyTime(_hour, _minute, _second);
}

MyTime MyTime::operator--(int) {
  MyTime old_t(_hour, _minute, _second);
  _second--;
  if (_second < 0) {
    _minute--;
    _second += SECONDS;
    if (_minute < 0) {
      _hour--;
      _minute += MINUTES;
      if (_hour < 0) {
        _hour += HOURS;
      }
    }
  }
  return old_t;
}

int main() {
  MyTime t1(0, 0, 0);
  MyTime t2(3, 16, 0);
  cout << "t1: " << t1 << endl;
  cout << "t2: " << t2 << endl;

  cout << "test t1--: ";
  cout << t1-- << endl;
  cout << t1 << endl;
  cout << "test --t2: ";
  cout << --t2 << endl;
  cout << t2 << endl;

  return 0;
}
```