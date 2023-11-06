---
title: Homework | 第三次作业解答
date: 2023-10-29 15:33:40
category: Homework
---


**【作业情况】：** 第一题没有对输入数据进行限制（额外要求，因为是实际应用的程序，因此希望对错误输入有相应的处理）；第二题有同学只使用了一重循环，应该是两重；第三题的问题在于平均值错误，主要是要把平均数定义为`double`，并且两数相除时也要求结果为`double`；第四题除了题目理解问题以外基本没问题；第五题很多同学最后结果没有乘4，要关注这个问题求的是$\pi$，不是$arctan(1)$

<!--more-->

## question 0

> 2.3   设计程序将输入的v。
> 提示：10分一档用10进行整除获得，转换用开关语句实行。

```cpp
#include <cmath>
#include <iostream>

int main() {
  double score{};
  int result{};
  std::cin >> score;
  // get the round int number
  int round_score = round(score);

  // use if-else
  if (round_score < 0 || round_score > 100) {
    std::cout << "please input valid score (0 <= score <= 100)" << std::endl;
  } else {
    if (round_score < 60) {
      result = 1;
    } else if (round_score < 70) {
      result = 2;
    } else if (round_score < 80) {
      result = 3;
    } else if (round_score < 90) {
      result = 4;
    } else if (round_score <= 100) {
      result = 5;
    }
    std::cout << "the result converted scored is: " << result << std::endl;
  }

  // use switch-case
  result = 0;
  if (round_score < 0 || round_score > 100) {
    std::cout << "please input valid score (0 <= score <= 100)" << std::endl;
  } else {
    switch (round_score / 10) {
    default:
      break;
    case 0:
    case 1:
    case 2:
    case 3:
    case 4:
    case 5:
      result = 1;
      break;
    case 6:
      result = 2;
      break;
    case 7:
      result = 3;
      break;
    case 8:
      result = 4;
      break;
    case 9:
    case 10:
      result = 5;
      break;
    }
    std::cout << "the result converted scored is: " << result << std::endl;
  }

  // a simpler method
  result = 0;
  if (round_score < 0 || round_score > 100) {
    std::cout << "please input valid score (0 <= score <= 100)" << std::endl;
  } else {
    round_score = std::max(round_score - 50, 0);
    result = std::min(round_score / 10 + 1, 5);
    std::cout << "the result converted scored is: " << result << std::endl;
  }

  return 0;
}
```

## question 1

> 2.7 输入n，求1!+2!+3!+…+n!
> 提示： 循环中要增加累加的变量

```cpp
#include <iostream>

int main() {
  int n{};
  int fact = 1;
  int sum = 0;
  std::cin >> n;
  for (int i = 1; i <= n; i += 1) {
    for (int j = 1; j <= i; j += 1) {
      fact *= j;
    }
    // output the process
    std::cout << i << " " << fact << " " << sum << std::endl;
    // accemulation sum
    sum += fact;
    // reset fact
    fact = 1;
  }
  std::cout << sum << std::endl;
  return 0;
}
```

## question 2

> 2.9 从键盘输入一组非0整数，以输入0标志结束，求这组整数的平均值，并统计其中正数和负数的个数。
> 提示： 分别建立求和，统计输入整数数量，整数和负数的个数的变量， 按照课堂讲解输入数据的方法

```cpp
#include <iostream>

int main() {
  int num{};
  int sum{};
  int positive_count{};
  int negtive_count{};
  while (std::cin >> num) {
    if (num == 0) {
      break;
    }
    positive_count = (num > 0) ? (positive_count + 1) : positive_count;
    negtive_count = (num < 0) ? (negtive_count + 1) : negtive_count;
    sum += num;
  }
  std::cout << "positive count: " << positive_count << std::endl;
  std::cout << "negtive count: " << negtive_count << std::endl;
  std::cout << "average: " << (double)sum / (positive_count + negtive_count)
            << std::endl;
  return 0;
}
```

## question 3

> 2.10 编程找出1-500之中满足除以3余2，除以5余3，除以7余2的整数。
> 提示:  使用穷举的方法，按照条件输出满足条件的数字。

```cpp
#include <iostream>

int main() {
  int min_limit = 1;
  int max_limit = 500;
  for (int num = min_limit; num < max_limit + 1; num += 1) {
    int r0 = num % 3;
    int r1 = num % 5;
    int r2 = num % 7;
    if (r0 == 2 && r1 == 3 && r2 == 2) {
      std::cout << num << " ";
    }
  }
  std::cout << std::endl;
  return 0;
}
```

## question 4

> 2.13 利用反正切展开计算Pi的近似值   令x=1，可计算出pi/4的近似值

```cpp
#include <cmath>
#include <corecrt_math.h>
#include <iostream>

int main() {
  double x = 1;
  double former = 0;
  double current = x;
  double limit = 1e-5;
  double sign_fact = 1;
  double x_fact = x;
  double deno = 1;
  while (fabs(current - former) > limit) {
    former = current;
    x_fact *= x * x;
    sign_fact *= -1;
    deno += 2;
    current += sign_fact * x_fact / deno;
  }
  std::cout << "pi = " << current * 4 << std::endl;
  return 0;
}
```