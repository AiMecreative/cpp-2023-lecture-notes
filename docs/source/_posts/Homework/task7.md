---
title: Homework | 第七次作业解答
date: 2023-11-19 14:55:45
category: Homework
---

**【作业情况】：正在批改**

<!--more-->

## question 0

```cpp
/**
1. 编写程序，完成分数的加法和减法（加减功能不用函数，
用到的最大公约数功能使用函数）； 提示： (1) 输入两个整数作为一个分数，例如：a1,
a2 代表第一个分数的分子和分母；b1, b2 代表 第二个分数的分子和分母，使用c1, c2
作为结果存储； (2) 两个分数的加法，先通分， 第一个分数变成 a1*b2/a2*b2;
第二个分数变成 b1*a2/b2*a2；  然后， c1= a1*b2+a1*b2; c2为通分后分母；
调用求最大公约数的函数；要约分化简c1,c2输出; (3) 输出 分数结果 c1, c2;
例如要求输出： 5/6 + 2/3 = 3/2   5/6- 2/3= 1/6
 */

#include <algorithm>
#include <iostream>

using namespace std;

int getGcd(int a, int b) {
  int res = std::max(a, b);
  while (true) {
    if ((a % res == 0) && (b % res == 0))
      break;
    res -= 1;
  }
  return res;
}

void printFraction(int numerator, int denominator) {
  cout << numerator << "/" << denominator;
}

/**
 * 分数的加法，这里函数没有返回值（当然以后学了一些东西后可以带返回值）
 * 直接将结果打印出来，不返回
 */
void fractionAdd(int num_a, int deno_a, int num_b, int deno_b) {
  int num_res = num_a * deno_b + num_b * deno_a;
  int deno_res = deno_a * deno_b;
  int frac_gcd = getGcd(num_res, deno_res);
  // print the result
  printFraction(num_a, deno_a);
  cout << "+";
  printFraction(num_b, deno_b);
  cout << "=";
  printFraction(num_res / frac_gcd, deno_res / frac_gcd);
  cout << endl;
}

void fractionMinus(int num_a, int deno_a, int num_b, int deno_b) {
  fractionAdd(num_a, deno_a, -num_b, deno_b);
}

int main() {
  int num_a = 0, deno_a = 0;
  int num_b = 0, deno_b = 0;
  cin >> num_a >> deno_a;
  cin >> num_b >> deno_b;
  fractionAdd(num_a, deno_a, num_b, deno_b);
  fractionMinus(num_a, deno_a, num_b, deno_b);
  return 0;
}
```

## question 1

```cpp
/**
 2.
从所给文本文件inf.txt中读取文本信息，对其做加密运算后输出到屏幕。运算规则为：
（1）英文、数字字符以外的字符不作处理；
（2）对英文字符，用英文字母表中该字符后数第19个字母替代它，若到字母表最后一个字母则接着从第一个字母向后数。例如，‘a’变为’t’，’Q’
变为’J’,字符’z’变成’s’；
（3）对数字字符，’0’不处理，其它用该位补数替代。例如：’3’变为’7’，’9’变为’1’。
 */

#include <fstream>
#include <iostream>

using namespace std;

const string PROGRAM_PATH{
    "E:/Documents/Repositories/cpp-2023-lecture-notes/tasks/week9/ref/"};
const string in_file{"inf.txt"};

// 26个英文字母
const unsigned int E = 26;
// 10个数字
const unsigned int N = 9;
// 加密偏移字段
const unsigned int E_OFFSET = 19;
const unsigned int N_OFFSET = 9;
// 各个字符开始位置
const char capitalAlphabetStart = 'A';
const char lowercaseAlphabetStart = 'a';
const char numberStart = '1';

bool isCapitalAlphabet(char c) {
  return (capitalAlphabetStart <= c) && (c <= capitalAlphabetStart + E - 1);
}

bool isLowercaseAlphabet(char c) {
  return (lowercaseAlphabetStart <= c) && (c <= lowercaseAlphabetStart + E - 1);
}

bool isNumber(char c) {
  return (numberStart <= c) && (c <= numberStart + N - 1);
}

char encryptE(char c, char start, char offset, unsigned int field) {
  return (c - start + offset) % field + start;
}

char encryptN(char c, char start, char offset, unsigned int field) {
    return field - (c - start) + start - 1;
}

/**
 * 加密文件的函数
 * 由于只要求输出到console中，因此不用文件写入
 * 直接打印即可
 */
void encrypt(const string &file_path) {
  ifstream ifile{file_path};
  char value = 0;
  while (ifile >> value) {
    if (isCapitalAlphabet(value))
      cout << encryptE(value, capitalAlphabetStart, E_OFFSET, E);
    else if (isLowercaseAlphabet(value))
      cout << encryptE(value, lowercaseAlphabetStart, E_OFFSET, E);
    else if (isNumber(value))
      cout << encryptN(value, numberStart, N_OFFSET, N);
    else cout << value;
  }
}

int main() {
  encrypt(PROGRAM_PATH + in_file);
  return 0;
}
```

## question 2

```cpp
/**
 求100~2000内的所有“回文数”（即正读与反读大小相同的数，如101、111、121、131等等），并将它们存入文本文件huiwen.txt。回文数需设计函数
【提示】：
（1）方法：判断n是否为“回文数”，可先求n的反序数res，看两者是否相等；求反序数可将n按位拆解，再反序拼装为res，如137，拆为1、3、7，再拼成731。
（2）编程：
设计函数，形参为待转化整数，返回值为它的反序数字，思路在使用前面讲解过的方法，利用在循环中拆解的最后位数字，不断乘以10相加获得，
尽量不用power函数。
 */

#include <fstream>
#include <iostream>
#include <string>

using namespace std;

const unsigned int START{100};
const unsigned int END{2000};
const string PROGRAM_PATH{
    "E:/Documents/Repositories/cpp-2023-lecture-notes/tasks/week9/ref/"};
const string OUT_FILE{"huiwen.txt"};

int reverse(int num) {
  int rev = 0;
  while (true) {
    int n = num % 10;
    if (n == 0 && (num / 10 == 0))
      break;
    num /= 10;
    rev *= 10;
    rev += n;
  }
  return rev;
}

int main() {
  ofstream ofile{PROGRAM_PATH + OUT_FILE};
  for (auto num{START}; num <= END; num += 1) {
    if (num == reverse(num)) ofile << num << endl;
  }
  return 0;
}
```

## question 3

```cpp
#include <iostream>

using namespace std;

const double beta{0.0001};
const double gamma{0.01};
const unsigned int initS{500};
const unsigned int initI{500};
const unsigned int initR{0};
const unsigned int rangeDay{100};

double derivativeS(int In, int Sn) { return -beta * In * Sn; }
double derivativeI(int In, int Sn) { return beta * In * Sn - gamma * In; }
double derivativeR(int In) { return gamma * In; }
double S(int Sn, double dSn) { return Sn + dSn; }
double I(int In, double dIn) { return In + dIn; }
double R(int Rn, double dRn) { return Rn + dRn; }

int main() {
  double Sn = S(initS, derivativeS(initI, initS));
  double In = I(initI, derivativeI(initI, initS));
  double Rn = R(initR, derivativeR(initI));
  cout << 1 << ": " << Sn << " " << In << " " << Rn << endl;
  int peek_day = 0;
  bool got = false;
  for (int day = 1; day < rangeDay; day += 1) {
    double Sn1 = S(Sn, derivativeS(In, Sn));
    double In1 = I(In, derivativeI(In, Sn));
    double Rn1 = R(Rn, derivativeR(In));
    cout << day + 1 << ": " << Sn1 << " " << In1 << " " << Rn1 << endl;
    if (In1 < In && !got) {
      peek_day = day;
      got = true;
    }
    Sn = Sn1;
    In = In1;
    Rn = Rn1;
  }
  cout << "the Infected people count decreases after " << peek_day << " days"
       << endl;
  return 0;
}
```