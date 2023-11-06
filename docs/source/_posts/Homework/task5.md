---
title: Homework | 第五次作业解答
date: 2023-11-06 17:07:23
category: Homework
---

**【作业情况】：正在批改**

<!--more-->

## question 0

> 第二章书后习题 2.18  ，找出100以内的质数，使用课堂讲解的办法两重循环

```cpp
#include <cmath>
#include <iostream>

using namespace std;

int main() {
  int max_limit = 100;
  for (int prime_num = 2; prime_num < max_limit + 1; prime_num += 1) {
    bool is_prime = true;
    for (int fact = 1; fact < sqrt(prime_num) + 1; fact += 1) {
      if (prime_num % fact == 0 && fact != 1 && fact != prime_num) {
        is_prime = false;
        break;
      }
    }
    if (is_prime) cout << prime_num << endl;
  }
  return 0;
}
```

## question 1

> 练习函数， 解决函数中调用其他函数的问题。利用级数展开式计算

```cpp
#include <iostream>

using namespace std;

double g(int m, double x) {
  int coe{};
  for (int i{1}; i <= m; i += 1) {
    coe += i;
  }
  return coe * x;
}

double f(int n, double x) {
  double value{1};
  for (int i = 1; i <= n; i += 1) {
    value += 1 / g(2 * i + 1, x);
  }
  return value;
}

int main() {
  double x{};
  int n{};
  cout << "input x (-1<x<=1): ";
  cin >> x;
  cout << "\ninput n (integer): ";
  cin >> n;
  cout << "f(" << x << ")="  << f(n, x) << ", (n=" << n << ")" << endl;
  return 0;
}
```

## question 2

>  哥德巴赫猜想，验证4-50之间的偶数可以分解为两个质数的和。要求：定义判断一个整数是否为质数的函数，利用这个函数实现对一个偶数的分解和质数之和输出。歌德巴赫猜想验证也用穷举法，在所有组合中找两个数均为素数者

```cpp
#include <cmath>
#include <iostream>

using namespace std;

bool is_prime(int integer) {
  bool judgement{true};
  for (int fact{1}; fact < sqrt(integer) + 1; fact += 1) {
    if (integer % fact == 0 && fact != 1 && fact != integer) {
      judgement = false;
    }
  }
  return judgement;
}

int main() {
  int min_limit{4};
  int max_limit{50};
  for (int odd = min_limit; odd <= max_limit; odd += 2) {
    for (int item{2}; item < odd / 2 + 1; item += 1) {
      if (is_prime(item) && is_prime(odd - item)) {
        cout << odd << "=" << item << "+" << odd - item << endl;
      }
    }
  }
  return 0;
}
```

## question 3

> 设计有两个参数的函数factors(num,k)，返回一个整数，这个整数是num中包含因子k的数（重复几次），8包含2因子3次，如果没有该因子，则返回0个

```cpp
#include <iostream>

using namespace std;

int factors(int num, int k) {
  int count{};
  while (num % k == 0) {
    num /= k;
    count += 1;
  }
  return count;
}

int main() {
  int num{};
  int k{};
  cout << "input num and k (divided by space): ";
  cin >> num >> k;
  cout << "factors: " << factors(num, k) << endl;
  return 0;
}
```

## question 4

> 设计一个函数，计算ln(1+x)

```cpp
#include <cmath>
#include <iostream>
using namespace std;

// input 1 + x
double ln(double x, double limit = 1e-5) {
  x -= 1;
  double former_item = 0;
  double current_item = x;
  double value = x;
  int sign = 1;
  int deno = 1;
  double nume = x;
  while (fabs(current_item - former_item) >= limit) {
    sign *= -1;
    nume *= x;
    deno += 1;
    former_item = current_item;
    current_item = sign * nume / deno;
    value += current_item;
  }
  return value;
}

int main() {
  double x{};
  cout << "input init x: ";
  cin >> x;
  cout << "round value of ln(1+" << x << ") is " << ln(1 + x) << endl;
  return 0;
}
```