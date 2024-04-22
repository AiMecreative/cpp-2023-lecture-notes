---
title: Homework | 第六次作业解答
date: 2024-04-22 16:02:45
category: Homework
---

第六次作业解答

<!--more-->

# question 0

使用指针数组机制， int **p 建立动态二维数组，输入二维数组的维数 m=3, n=5, 
设计输出这个二维整数数组函数output，以及返回值这二维数组最大元素的值的函数findmax。注意函数的形式参数定义。

- 主要考察二维指针的使用

```cpp
#include <iostream>
#include <stdint.h>
#include <stdlib.h>

using namespace std;

int **init2d(int **p, int row_size, int col_size) {
  if (p != nullptr) {
    delete[] p;
    p = nullptr;
  }
  if (p == nullptr) {
    p = new int *[row_size];
    for (int r = 0; r < row_size; r += 1) {
      p[r] = new int[col_size];
    }
  }
  for (int r = 0; r < row_size; r += 1) {
    for (int c = 0; c < col_size; c += 1) {
      p[r][c] = rand() % 10;
    }
  }
  return p;
}

void output2d(int **p, const int row_size, const int col_size) {
  if (p == nullptr) {
    cout << "empty pointer";
    return;
  }
  for (int r = 0; r < row_size; r += 1) {
    for (int c = 0; c < col_size; c += 1) {
      cout << p[r][c] << " ";
    }
    cout << endl;
  }
}

int findMax(int **p, const int row_size, const int col_size) {
  // 初始化最大值为int类型的最小值
  int max = INT32_MIN;
  for (int r = 0; r < row_size; r += 1) {
    for (int c = 0; c < col_size; c += 1) {
      if (p[r][c] > max) {
        max = p[r][c];
      }
    }
  }
  return max;
}

int main() {
  int **p = nullptr;
  int row_size = 3;
  int col_size = 5;
  p = init2d(p, row_size, col_size);
  output2d(p, row_size, col_size);
  int max = findMax(p, row_size, col_size);
  cout << "max value: " << max << endl;
  return 0;
}
```

输出结果为

```txt
1 7 4 0 9 
4 8 8 2 4
5 5 1 7 1
max value: 9
```

# question 1

实现MyString类，仿照C++内置的字符串类

- 注意，由于要求是仿照，所以尽量别用字符串内置函数，例如 `strlen, strcpy_s` 之类的

```cpp
#include <cassert>
#include <iostream>

using namespace std;

class MyString {
private:
  char *_str;
  int _length;

public:
  MyString() : _str(nullptr), _length(0) {}
  // 由于是要我们自己仿照字符串类，那最好就不要用c++字符串内置函数
  MyString(const char *str) {
    // 先计算str的长度
    int length = 0;
    int i = 0;
    while (str[i] != '\0') {
      length += 1;
      i += 1;
    }
    // 再初始化自己
    _length = length;
    _str = new char[length + 1];
    for (i = 0; i < _length; i += 1) {
      _str[i] = str[i];
    }
    _str[length] = '\0';
  }
  // 重复c字符times次
  MyString(int times, char c) {
    _length = times;
    _str = new char[_length + 1];
    for (int i = 0; i < times; i += 1) {
      _str[i] = c;
    }
    _str[_length] = '\0';
  }
  // 由于是要我们自己仿照字符串类，那最好就不要用c++字符串内置函数
  MyString(const MyString &other) : _length(other._length) {
    _str = new char[_length + 1];
    for (int i = 0; i < _length; i += 1) {
      _str[i] = other._str[i];
    }
    _str[_length] = '\0';
  }
  ~MyString() {
    if (_str != nullptr) {
      delete[] _str;
      _str = nullptr;
    }
    _length = 0;
  }

  void assign(const char *str) {
    // 先计算str的长度
    int length = 0;
    int i = 0;
    while (str[i] != '\0') {
      length += 1;
      i += 1;
    }
    // 再初始化自己
    _length = length;
    // 但要记住要先delete原先的值（拷贝构造不需要delete）
    if (_str != nullptr) {
      delete[] _str;
      _str = nullptr;
    }
    _str = new char[length + 1];
    for (i = 0; i < _length; i += 1) {
      _str[i] = str[i];
    }
    _str[length] = '\0';
  }

  int length() const { return _length; }

  char at(const int index) const {
    assert(0 <= index && index < _length);
    return _str[index];
  }

  void clear() {
    if (_str != nullptr) {
      delete[] _str;
      _str = nullptr;
    }
    _length = 0;
  }

  void show() const {
    for (int i = 0; i < _length; i += 1) {
      cout << _str[i];
    }
    cout << endl;
  }

  MyString operator=(const MyString &other) {
    assign(other._str);
    return *this;
  }

  MyString operator+=(const MyString &other) {
    int len = _length + other._length;
    char *temp = nullptr;
    if (_str != nullptr) {
      temp = new char[_length + 1];
      for (int i = 0; i < _length; i += 1) {
        temp[i] = _str[i];
      }
      temp[_length] = '\0';
      delete[] _str;
      _str = nullptr;
    }
    _str = new char[len + 1];
    if (temp != nullptr) {
      for (int i = 0; i < _length; i += 1) {
        _str[i] = temp[i];
      }
    }
    if (other._str != nullptr) {
      for (int i = 0; i < other._length; i += 1) {
        _str[_length + i] = other._str[i];
      }
    }
    _str[len] = '\0';
    _length = len;
    return *this;
  }

  char operator[](const int index) const { return at(index); }
  char &operator[](const int index) {
    assert(0 <= index && index < _length);
    return _str[index];
  }
};

int main() {
  MyString str1;
  MyString str2(5, 'c');
  MyString str3("China");

  str1.show();
  str2.show();
  str3.show();

  cout << "str3 length: " << str3.length() << endl;

  str2.assign("C++ programming");
  str2.show();

  char c1 = str3.at(2);
  str2[2] = c1;
  str2.show();

  str1.assign("SEU");
  str1.show();

  MyString str4 = str1;
  str4 += str1;
  str4.show();

  MyString str5;
  str5 = str4;
  str5.show();
  return 0;
}
```

输出结果为

```txt

ccccc
China
str3 length: 5
C++ programming
C+i programming
SEU
SEUSEU
SEUSEU
```
