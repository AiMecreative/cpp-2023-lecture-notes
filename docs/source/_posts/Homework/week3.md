---
title: Homework | 第三次作业解答
date: 2024-03-18 16:36:09
category: Homework
---

春季学期第二次作业解答

<!--more-->

# question 0

![question0](t0.png)

```cpp
#include <cmath>
#include <corecrt_math.h>
#include <iostream>

using namespace std;

class Point {
private:
  int _x;
  int _y;

public:
  Point() : _x(0), _y(0) {}
  Point(int x, int y) : _x(x), _y(y) {}

  void setXy(int x, int y) {
    _x = x;
    _y = y;
  }

  int getX() const { return _x; }
  int getY() const { return _y; }
};

class Rectangle {
private:
  Point _point1; // 左上
  Point _point2; // 左下
  Point _point3; // 右下
  Point _point4; // 右上

public:
  Rectangle() {}
  // 注意题目中说“对象之间可以赋值”，但在规范的编程中需要重载等号
  // 因此这里使用`setXy(int, int)`
  Rectangle(Point point1, Point point3) {
    _point1.setXy(point1.getX(), point1.getY());
    _point2.setXy(point1.getX(), point3.getY());
    _point3.setXy(point3.getX(), point3.getY());
    _point4.setXy(point3.getX(), point1.getY());
  }
  Rectangle(int x1, int y1, int x3, int y3) {
    _point1.setXy(x1, y1);
    _point2.setXy(x1, y3);
    _point3.setXy(x3, y3);
    _point4.setXy(x3, y1);
  }

  int getArea() {
    int h = abs(_point1.getY() - _point2.getY());
    int w = abs(_point2.getX() - _point3.getX());
    return h * w;
  }

  void printPoints() {
    cout << "( " << _point1.getX() << ", " << _point1.getY() << "), "
         << "( " << _point4.getX() << ", " << _point4.getY() << ")\n";
    cout << "( " << _point2.getX() << ", " << _point2.getY() << "), "
         << "( " << _point3.getX() << ", " << _point3.getY() << ")\n";
  }
};

int main() {
  Point p1(-15, 56);
  Point p2(89, -10);

  Rectangle rec1(p1, p2);
  Rectangle rec2(1, 5, 5, 1);

  cout << "矩形1的四个顶点坐标：";
  rec1.printPoints();
  cout << "矩形1的面积：" << rec1.getArea() << endl;

  cout << "矩形2的四个顶点坐标：";
  rec2.printPoints();
  cout << "矩形2的面积：" << rec2.getArea() << endl;

  return 0;
}
```

# question 1

![question1](t1.png)

```cpp
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

  //---------------week3 question1 added---------------//
  // 拷贝构造
  Fraction(Fraction &other) : _above(other._above), _below(other._below) {}
  // 析构函数
  ~Fraction() {}
  Fraction operator+(const Fraction &other);
  Fraction operator-(const Fraction &other);
  Fraction operator=(const Fraction &other);
  bool operator==(Fraction &other);
  //---------------------------------------------------//
  // !注意这里把约分和通分作为公有函数接口，更加合理

  // 约分
  void reduction();

  // 通分
  // !注意这里与题目要求不一致但更加合理
  // !通分是本对象与另一个分数通分，但不改变另一个分数的分子分母
  // !只改变自身，因此也没有必要有返回值
  void common(const Fraction &other);

  Fraction add(Fraction &other);
  Fraction minus(Fraction &other);

  bool isEqual(Fraction &other);

  void input();
  void display();

  //---------------week3 question1 added---------------//
  friend Fraction operator*(const Fraction &current, const Fraction &other);
  friend Fraction operator/(const Fraction &current, const Fraction &other);
  //---------------------------------------------------//
};

//---------------week3 question1 added---------------//
Fraction Fraction::operator=(const Fraction &other) {
  _above = other._above;
  _below = other._below;
  return *this;
}

Fraction Fraction::operator+(const Fraction &other) {
  Fraction res(_above + other._above, _below + other._below);
  res.reduction();
  return res;
}

Fraction Fraction::operator-(const Fraction &other) {
  Fraction res(_above - other._above, _below - other._below);
  res.reduction();
  return res;
}

bool Fraction::operator==(Fraction &other) {
  this->reduction();
  other.reduction();
  return _above == other._above && _below == other._below;
}

Fraction operator*(const Fraction &current, const Fraction &other) {
  Fraction res(current._above * other._above, current._below * other._below);
  res.reduction();
  return res;
}

Fraction operator/(const Fraction &current, const Fraction &other) {
  Fraction res(current._above * other._below, current._below * other._above);
  res.reduction();
  return res;
}
//---------------------------------------------------//

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

// 这里没有对输出进行格式化，会出现正负的符号问题
void Fraction::display() {
  reduction();
  cout << "fraction: " << _above << " / " << _below << endl;
}

int main() {
  Fraction a(1, 2);
  Fraction b(5, 15);
  Fraction c = a;

  a.display();
  b.display();
  c.display();

  c = a + b;
  c.display();

  Fraction f(10, 30);
  if (f == b)
    cout << "fraction `f` equals to `b`" << endl;
  else
    cout << "fraction `f` not equals `b`" << endl;

  return 0;
}
```

