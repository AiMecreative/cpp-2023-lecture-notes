---
title: Homework | 第七次作业解答
date: 2024-04-08 13:21:36
category: Homework
---

<!--more-->

# question 0

使用模板实现矩阵类。需要重载常见的赋值运算符和乘法运算符，存储方式采用二维指针。

```c++
#include <cassert>
#include <iostream>
#include <random>
#include <type_traits>

using namespace std;

template <typename Ty> class CMatrix {
private:
  Ty **_value_ptr;
  int _row;
  int _col;

public:
  CMatrix<Ty>() {
    _value_ptr = nullptr;
    _row = 0;
    _col = 0;
  }

  CMatrix<Ty>(int row, int col) : _row(row), _col(col) {
    _value_ptr = new Ty *[row];
    for (int r = 0; r < row; r += 1) {
      _value_ptr[r] = new Ty[col];
    }
  }

  CMatrix<Ty>(const CMatrix<Ty> &other) : _row(other._row), _col(other._col) {
    _value_ptr = new Ty *[_row];
    for (int r = 0; r < _row; r += 1) {
      _value_ptr[r] = new Ty[_col];
      for (int c = 0; c < _col; c += 1) {
        _value_ptr[r][c] = other._value_ptr[r][c];
      }
    }
  }

  ~CMatrix<Ty>() {
    if (_value_ptr == nullptr) {
      return;
    }
    for (int r = 0; r < _row; r += 1) {
      delete[] _value_ptr[r];
    }
    delete[] _value_ptr;
  }

  Ty *operator[](int index) {
    assert(index < _row);
    assert(_value_ptr != nullptr);
    return _value_ptr[index];
  }

  CMatrix<Ty> operator*(CMatrix<Ty> &other) {
    assert(_col == other._row);
    CMatrix<Ty> res(_row, other._col);
    for (int i = 0; i < res._row; i += 1) {
      for (int j = 0; j < res._col; j += 1) {
        Ty t = Ty();
        for (int n = 0; n < _col; n += 1) {
          t = t + _value_ptr[i][n] * other._value_ptr[n][j];
        }
        res[i][j] = t;
      }
    }
    return res;
  }

  CMatrix<Ty> &operator=(const CMatrix<Ty> &other) {
    if (_value_ptr != nullptr) {
      for (int r = 0; r < _row; r += 1) {
        delete[] _value_ptr[r];
      }
      delete[] _value_ptr;
    }

    _row = other._row;
    _col = other._col;

    _value_ptr = new Ty *[_row];
    for (int r = 0; r < _row; r += 1) {
      _value_ptr[r] = new Ty[_col];
      for (int c = 0; c < _col; c += 1) {
        _value_ptr[r][c] = other._value_ptr[r][c];
      }
    }

    return *this;
  }

  // 矩阵转置
  CMatrix<Ty> T() {
    CMatrix<Ty> t(_col, _row);
    for (int r = 0; r < t._row; r += 1) {
      for (int c = 0; c < t._col; c += 1) {
        t._value_ptr[r][c] = _value_ptr[c][r];
      }
    }
    return t;
  }

  // 随机初始化，设计到 type_traits ，可以忽略
  void rand_init(Ty lower, Ty upper, int seed = 0) {
    default_random_engine e;
    e.seed(seed);
    if constexpr (is_floating_point_v<Ty>) {
      uniform_real_distribution<Ty> u(lower, upper);
      for (int r = 0; r < _row; r += 1) {
        for (int c = 0; c < _col; c += 1) {
          _value_ptr[r][c] = u(e);
        }
      }
      return;
    }
    if constexpr (is_integral_v<Ty>) {
      uniform_int_distribution<Ty> u(lower, upper);
      for (int r = 0; r < _row; r += 1) {
        for (int c = 0; c < _col; c += 1) {
          _value_ptr[r][c] = u(e);
        }
      }
    }
  }

  void print() {
    assert(_value_ptr != nullptr);
    for (int c = 0; c < _col; c += 1) {
      for (int r = 0; r < _row; r += 1) {
        cout << _value_ptr[r][c] << " ";
      }
      cout << endl;
    }
  }
};

using dtype = double;

int main() {
  CMatrix<dtype> m1;
  CMatrix<dtype> m2(3, 3);
  m2.rand_init(2, 8);
  cout << "m2:\n";
  m2.print();

  m1 = m2.T();
  cout << "m1:\n";
  m1.print();

  CMatrix<dtype> m3(m1);
  cout << "m3:\n";
  m3.print();

  m3.rand_init(0, 10);
  cout << "m3:\n";
  m3.print();

  CMatrix<dtype> m4;
  m4 = m2;
  cout << "m4:\n";
  m4.print();

  // 希望大家在自己写的代码中测试一下这两句
  m4 = m3 * m2 * m1;
  m4 = m3 * (m2 * m1);
  cout << "m4:\n";
  m4.print();

  return 0;
}
```


# question 1

实现链表，数据域使用复数。

```c++
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

class Complex {
private:
  int _re;
  int _im;

public:
  Complex() : _re(0), _im(0) {}
  Complex(int re, int im) : _re(re), _im(im) {}
  Complex(const Complex &other) : _re(other._re), _im(other._im) {}

  Complex operator=(const Complex &other) {
    _re = other._re;
    _im = other._im;
    return *this;
  }

  void print(bool require_endl = false) {
    string sign = _im <= 0 ? "" : "+";
    if (_re != 0) {
      cout << _re;
    }
    cout << sign;
    if (_im != 0) {
      cout << _im << "i";
    }
    if (_re == 0 && _im == 0) {
      cout << 0;
    }
    if (require_endl) {
      cout << endl;
    }
  }
};

struct Node {
  Complex value;
  Node *ptr;

  Node() : value(Complex()), ptr(nullptr) {}
};

class List {
private:
  Node *_head;

public:
  // 初始化哨兵结点（什么是哨兵结点？）
  // 可以将前后插入结点的操作统一起来
  List() : _head(nullptr) {
    _head = new Node;
    _head->value = Complex();
    _head->ptr = nullptr;
  }

  void clear() {
    if (_head->ptr == nullptr) {
      return;
    }
    Node *p = _head->ptr;
    while (p != nullptr) {
      Node *q = p->ptr;
      delete[] p;
      p = q;
    }
  }

  // 在前插入结点实现链表
  void forward(const string &fp) {
    ifstream file_in{fp};
    while (!file_in.eof()) {
      int re = 0;
      int im = 0;
      file_in >> re >> im;

      Complex complex(re, im);
      Node *node = new Node;
      node->value = complex;
      node->ptr = _head->ptr;
      _head->ptr = node;
    }
  }

  // 在后插入结点实现链表
  void reverse(const string &fp) {
    ifstream file_in{fp};
    Node *p = _head;
    while (!file_in.eof()) {
      int re = 0;
      int im = 0;
      file_in >> re >> im;

      Complex complex(re, im);
      Node *node = new Node;
      node->value = complex;
      p->ptr = node;
      p = node;
    }
  }

  void print() {
    Node *p = _head->ptr;
    cout << "HEAD -> ";
    while (p != nullptr) {
      cout << "[";
      p->value.print();
      cout << "] -> ";
      p = p->ptr;
    }
    cout << "END" << endl;
  }
  // List operator+()
};

const string fp ="path/to/data";

int main() {
  List li;
  li.forward(fp);
  li.print();
  li.clear();
  li.reverse(fp);
  li.print();
  return 0;
}
```