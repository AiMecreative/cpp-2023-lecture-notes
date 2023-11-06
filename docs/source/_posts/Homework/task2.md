---
title: Homework | 第二次作业解答
date: 2023-10-18 11:13:52
category: Homework
---

**【作业情况】**：对变量何时是`int`和`double`有点模糊，例如第一题的涉及到的是`double`的运算；求解一元二次方程后输出结果的处理不好（例如如何打印一个复数）；第三题中输出逆序数没有处理末尾带0的情况（额外要求，例如100100应该逆序为1001，不是001001）；第四题完成较好。
<!--more-->

## 使用`if-else`和`switch-case`计算缴纳费用


**使用`if-else`语句**

```cpp
#include <iostream>

int main() {
  double income{};
  double ratio{};
  std::cout << "input your income: " << std::endl;
  std::cin >> income;
  if (income < 0) {
    std::cout << "income out of range: " << income << " < 0" << std::endl;
  } else if (income < 1000) {
    ratio = 0.02;
  } else if (income < 2000) {
    ratio = 0.03;
  } else if (income < 5000) {
    ratio = 0.04;
  } else if (income < 10000) {
    ratio = 0.05;
  } else {
    ratio = 0.06;
  }
  std::cout << "total fee: " << ratio * income << std::endl;
  return 0;
}
```

**使用`switch-case`语句**

```cpp
#include <iostream>

int main() {
  int income;
  std::cout << "Input your income: ";
  std::cin >> income;
  if (income < 0) {
    std::cout << "You cannot have negative income." << std::endl;
    exit(-1);
  }
  double ratio;

  switch (income / 1000) {
  case 0:
    ratio = .02;
    break;
  case 1:
    ratio = .03;
    break;
  case 2:
  case 3:
  case 4:
    ratio = .04;
    break;
  case 5:
  case 6:
  case 7:
  case 8:
  case 9:
    ratio = .05;
    break;
  default:
    ratio = .06;
  }

  std::cout << "Fund: " << ratio * income << std::endl;
  return 0;
}
```

## 求解一元二次方程

```cpp
#include <cmath>
#include <iostream>

int main() {
  double a, b, c;
  double real_x1, real_x2;
  double img_x1, img_x2;
  std::cout << "input coefficients(a,b,c): ";
  std::cin >> a >> b >> c;
  double delta = b * b - 4 * a * c;
  if (delta >= 0) {
    real_x1 = (-b + sqrt(delta)) / (2 * a);
    img_x1 = 0;
    real_x2 = (-b - sqrt(delta)) / (2 * a);
    img_x2 = 0;
  } else {
    real_x1 = -b / (2 * a);
    img_x1 = sqrt(-delta) / (2 * a);
    real_x2 = -b / (2 * a);
    img_x2 = -sqrt(-delta) / (2 * a);
  }
  std::cout << "x1 = ";
  if (real_x1 != 0)
    std::cout << real_x1;
  if (img_x1 != 0)
    std::cout << (img_x1 < 0? "" : "+") << img_x1 << "i";
  std::cout << std::endl;

  std::cout << "x2 = ";
  if (real_x2 != 0)
    std::cout << real_x2;
  if (img_x2 != 0)
    std::cout << (img_x2 < 0? "" : "+") << img_x2 << "i";
  std::cout << std::endl;
  return 0;
}
```

## 求逆序数

```cpp
#include <iostream>

int main() {
  int num{};
  int bit_num{};
  int bit_sum{};
  std::cout << "input the num: ";
  std::cin >> num;
  // delete zeros in the tail
  while (num % 10 == 0) {
    num /= 10;
    bit_num += 1;
  }
  int t0{num};
  int t1{num};
  std::cout << "the inversion is: ";
  // inversion
  while (t0 > 0) {
    t1 = t0 % 10;
    t0 = t0 / 10;
    bit_num += 1;
    bit_sum += t1;
    std::cout << t1;
  }
  std::cout << std::endl;
  std::cout << "the bit num is: " << bit_num << std::endl;
  std::cout << "the bit sum is: " << bit_sum << std::endl;
  return 0;
}
```

## 求最大公因数和最小公倍数

```cpp
#include <iostream>

int main() {
  int x, y;
  std::cout << "Input two numbers for gcd and lcm:";
  std::cin >> x >> y;
  if (x == 0 || y == 0) {
    std::cout << "gcd: 0" << std::endl;
    if (x == 0 && y == 0) {
      std::cout << "lcm: 0" << std::endl;
    } else {
      std::cout << "lcm: infinity" << std::endl;
    }
  } else {
    if (x < 0) {
      x = -x;
    }
    if (y < 0) {
      y = -y;
    }

    int gcd = std::min(x, y);
    int lcm = std::max(x, y);
    // just ignore the requirement to use for-loop and break:
    while (x % gcd != 0 || y % gcd != 0) {
      gcd -= 1;
    }

    while (lcm % x != 0 || lcm % y != 0) {
      lcm += 1;
    }

    std::cout << "gcd: " << gcd << std::endl;
    std::cout << "lcm: " << lcm << std::endl;
  }
  return 0;
}
```