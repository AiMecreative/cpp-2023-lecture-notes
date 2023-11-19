---
title: Homework | 第六次作业解答
date: 2023-11-19 14:55:31
category: Homework
---

**【作业情况】：正在批改**

<!--more-->

## question 0

```cpp
/**
 * 课本 3.4  题
 * 设计两个函数，分别求两个数的最大公约数和最小公倍数，主函数测试，可使用穷举
 */

#include <algorithm>
#include <iostream>

using namespace std;

// 最小公倍数
int getLcm(int a, int b) {
  int res = std::max(a, b);
  while (true) {
    if ((res % a == 0) && (res % b) == 0)
      break;
    res += 1;
  }
  return res;
}

// 最大公约数
int getGcd(int a, int b) {
  int res = std::max(a, b);
  while (true) {
    if ((a % res == 0) && (b % res) == 0)
      break;
    res -= 1;
  }
  return res;
}

int main() {
  int a{0}, b{0};
  cout << "input 2 numbers and calculate there gcd and lcm: ";
  cin >> a >> b;
  cout << "gcd(" << a << ", " << b << ") = " << getGcd(a, b) << endl;
  cout << "lcm(" << a << ", " << b << ") = " << getLcm(a, b) << endl;
  return 0;
}
```

## question 1

```cpp
#include <iostream>

using namespace std;

double legendre(int n, double x) {
    if (n == 0) return 1;
    if (n == 1) return x;
    return ((2 * n - 1) * x * legendre(n-1, x) - (n - 1) * legendre(n - 2, x)) / n;
}

int main() {
    cout << legendre(4, 1.5);
    return 0;
}
```

## question 2

```cpp
/**
 * 要求：设计一个函数 int check(int m)并且测试；
 * （1）函数功能是传递参数，提取一个整数中的最高位的数字和最低位数字，检查二者是否相同，若是则返回
 * 1，否则返回 0。
 * （2）主函数要求依次输入5个数，
 * 然后调用上述设计的函数，输出一共有多少个整数是高位与低位相同。
 */

#include <iostream>

using namespace std;

int check(int m) {
  int tail = m % 10;
  // 当m被10整除后结果不为0（也就是m至少是两位数时），不断整除10并赋值给自己
  while (m / 10) m /= 10;
  int head = m;
  return tail == head;
}

int main() {
  int const input_count = 5;
  int value = 0;
  for (auto _ = 0; _ < input_count; _ += 1) {
    cin >> value;
    cout << "check result: " << check(value) << endl;
  }
  return 0;
}
```

## question 3

```cpp
#include <cmath>
#include <corecrt_math.h>
#include <ios>
#include <iostream>
#include <iomanip>

using namespace std;

int gcd(int a, int b) {
    for (int i = min(a, b); i > 0; i -= 1) {
        // cout << i << endl;
        if (a % i == 0 && b % i == 0) return i;
    }
    return -1;
}

int main() {
    double num{};
    cin >> num;
    int bit_num{};
    int integer_num{};
    int deli{1};
    while (fabs(num - integer_num) >= 1e-6) {
        num *= 10;
        integer_num = (int)round(num);
        bit_num += 1;
        deli *= 10;
        cout << fixed << setprecision(6) << num << " " << integer_num << " " << deli << " " << bit_num << endl;
    }
    // cout << "this" << endl;
    int frac_gcd = gcd(integer_num, deli);
    cout << frac_gcd << endl;
    cout << (integer_num / frac_gcd) << '/' << (deli / frac_gcd) << endl;
    return 0;
}
```