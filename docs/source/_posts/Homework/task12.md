---
title: Homework | 第十二次作业解答
date: 2024-01-08 20:49:46
category: Homework
---

第十二次作业解答

<!--more-->

## 第一题

> `declare.hpp`

```cpp
#pragma once

double f(int, double);
double g(int, double);
```

> `instance.cpp`

```cpp
#include "declare.hpp"

double g(int n, double x) { return (n - 1) * n / 2. * x; }

double f(int n, double x) {
  double value = 1.;
  for (unsigned k = 1; k <= n; k += 1) {
    value += 1. / g(2 * k + 1, x);
  }
  return value;
}
```

> `question0.cpp`

```cpp
#include <iostream>

#include "declare.hpp"

using namespace std;

int main() {
  double x = 0.;
  int n = 1;
  cout << "input the init value of x (-1, 1]: ";
  cin >> x;
  cout << "input the init value of n (integer): ";
  cin >> n;
  double result = f(n, x);
  cout << "f(" << x << ") = " << result << ", (n = " << n << ")\n";
  return 0;
}
```

## 第二题

> `matrix.hpp`

```cpp
#pragma once

// 矩阵结构体的声明
struct Matrix {
  int x_dim;
  int y_dim;
  int** elem;
};

// 关于矩阵结构体运算的函数声明
// 说明: 在下个学期时, 可以作为成员函数直接在struct/class中声明,
//      不用像这样分开声明

// 创建并初始化一个矩阵
Matrix create(int x_dim, int y_dim);

//赋值
void assign(Matrix& m, int x, int y, int value);

// 打印
void print(const Matrix& m);

// 转置
Matrix transpose(const Matrix& matrix);

// 乘法
Matrix multiply(const Matrix& m1, const Matrix& m2);
```

> `matrix.cpp`

```cpp
#include "matrix.hpp"

#include <cassert>
#include <iostream>

Matrix create(int x_dim, int y_dim) {
  Matrix created;
  created.x_dim = x_dim;
  created.y_dim = y_dim;
  created.elem = new int *[created.x_dim];
  for (int xd = 0; xd < x_dim; xd += 1) {
    created.elem[xd] = new int[created.y_dim];
    // 初始化每一个值
    for (int v = 0; v < y_dim; v += 1) {
      created.elem[xd][v] = 0;
    }
  }
  return created;
}

void assign(Matrix &m, int x, int y, int value) { m.elem[x][y] = value; }

void print(const Matrix &m) {
  for (int i = 0; i < m.x_dim; i += 1) {
    for (int j = 0; j < m.y_dim; j += 1) {
      std::cout << m.elem[i][j] << "\t";
    }
    std::cout << std::endl;
  }
  std::cout << std::endl;
}

Matrix transpose(const Matrix &matrix) {
  // 定义好转置后的结果矩阵, 并初始化
  Matrix transposed = create(matrix.y_dim, matrix.x_dim);
  // 进行转置: a[i, j] -> b[j, i]
  for (int i = 0; i < matrix.x_dim; i += 1) {
    for (int j = 0; j < matrix.y_dim; j += 1) {
      transposed.elem[j][i] = matrix.elem[i][j];
    }
  }
  return transposed;
}

Matrix multiply(const Matrix &m1, const Matrix &m2) {
  // 检查维度是否匹配
  assert(m1.y_dim == m2.x_dim);
  // 创建一个用于存储结果的矩阵
  Matrix result = create(m1.x_dim, m2.y_dim);
  // 乘法
  for (int i = 0; i < result.x_dim; i += 1) {
    for (int j = 0; j < result.y_dim; j += 1) {
      for (int k = 0; k < m1.y_dim; k += 1) {
        result.elem[i][j] += m1.elem[i][k] * m2.elem[k][j];
      }
    }
  }
  return result;
}
```

> `question1.cpp`

```cpp
#include <iostream>
#include <random>

#include "matrix.hpp"

using namespace std;

int main() {
  int x_dim1 = 0, x_dim2 = 0;
  int y_dim1 = 0, y_dim2 = 0;
  cout << "input the first matrix's shape (x, y): ";
  cin >> x_dim1 >> y_dim1;
  cout << "input the second matrix's shape (x, y): ";
  cin >> x_dim2 >> y_dim2;

  Matrix m1 = create(x_dim1, y_dim1);
  Matrix m2 = create(x_dim2, y_dim2);

  // 分别为两个矩阵赋值并打印查看结果
  for (int i = 0; i < m1.x_dim; i += 1) {
    for (int j = 0; j < m1.y_dim; j += 1) {
      assign(m1, i, j, rand() % 20 - 10);
    }
  }
  for (int i = 0; i < m2.x_dim; i += 1) {
    for (int j = 0; j < m2.y_dim; j += 1) {
      assign(m2, i, j, rand() % 20 - 10);
    }
  }
  cout << "the init values of 2 matrices are:\n";
  cout << "first matrix:\n";
  print(m1);
  cout << "second matrix:\n";
  print(m2);

  cout << "transpose of the first matrix:\n";
  print(transpose(m1));

  cout << "multiply of 2 matrices:\n";
  print(multiply(m1, m2));
  return 0;
}
```

## 第三题

> `matrix.hpp`

```cpp
#pragma once

// 矩阵结构体的声明
struct Matrix {
  int x_dim;
  int y_dim;
  int** elem;
};

// 关于矩阵结构体运算的函数声明
// 说明: 在下个学期时, 可以作为成员函数直接在struct/class中声明,
//      不用像这样分开声明

// 创建并初始化一个矩阵
Matrix create(int x_dim, int y_dim);

// 赋值
void assign(Matrix& m, int x, int y, int value);

// 随机初始化矩阵
// 参数sym表示是否需要创建对称矩阵
void init(Matrix& m, bool sym);

// 打印
void print(const Matrix& m);

// 转置
Matrix transpose(const Matrix& matrix);

// 乘法
Matrix multiply(const Matrix& m1, const Matrix& m2);

// 判断是否为对称矩阵
bool isSymmetric(const Matrix& m);
```

> `matrix.cpp`

```cpp
#include "matrix.hpp"

#include <cassert>
#include <iostream>

Matrix create(int x_dim, int y_dim) {
  Matrix created;
  created.x_dim = x_dim;
  created.y_dim = y_dim;
  created.elem = new int *[created.x_dim];
  for (int xd = 0; xd < x_dim; xd += 1) {
    created.elem[xd] = new int[created.y_dim];
    // 初始化每一个值
    for (int v = 0; v < y_dim; v += 1) {
      created.elem[xd][v] = 0;
    }
  }
  return created;
}

void assign(Matrix &m, int x, int y, int value) { m.elem[x][y] = value; }

void print(const Matrix &m) {
  for (int i = 0; i < m.x_dim; i += 1) {
    for (int j = 0; j < m.y_dim; j += 1) {
      std::cout << m.elem[i][j] << "\t";
    }
    std::cout << std::endl;
  }
  std::cout << std::endl;
}

void init(Matrix &m, bool sym) {
  for (int i = 0; i < m.x_dim; i += 1) {
    for (int j = 0; j < m.y_dim; j += 1) {
      assign(m, i, j, rand() % 20 - 10);
    }
  }
  if (!sym) return;
  // 对称矩阵必然是方阵
  if (m.x_dim != m.y_dim) return;
  for (int i = 0; i < m.x_dim; i += 1) {
    for (int j = 0; j < i; j += 1) {
      m.elem[i][j] = m.elem[j][i];
    }
  }
}

Matrix transpose(const Matrix &matrix) {
  // 定义好转置后的结果矩阵, 并初始化
  Matrix transposed = create(matrix.y_dim, matrix.x_dim);
  // 进行转置: a[i, j] -> b[j, i]
  for (int i = 0; i < matrix.x_dim; i += 1) {
    for (int j = 0; j < matrix.y_dim; j += 1) {
      transposed.elem[j][i] = matrix.elem[i][j];
    }
  }
  return transposed;
}

Matrix multiply(const Matrix &m1, const Matrix &m2) {
  // 检查维度是否匹配
  assert(m1.y_dim == m2.x_dim);
  // 创建一个用于存储结果的矩阵
  Matrix result = create(m1.x_dim, m2.y_dim);
  // 乘法
  for (int i = 0; i < result.x_dim; i += 1) {
    for (int j = 0; j < result.y_dim; j += 1) {
      for (int k = 0; k < m1.y_dim; k += 1) {
        result.elem[i][j] += m1.elem[i][k] * m2.elem[k][j];
      }
    }
  }
  return result;
}

bool isSymmetric(const Matrix &m) {
  // 对称矩阵必然是方阵
  if (m.x_dim != m.y_dim) return false;
  for (int i = 0; i < m.x_dim; i += 1) {
    for (int j = 0; j < i; j += 1) {
      if (m.elem[i][j] != m.elem[j][i]) {
        return false;
      }
    }
  }
  return true;
}
```

> `question2.cpp`

```cpp
#include <iostream>
#include <random>

#include "matrix.hpp"

using namespace std;

int main() {
  int x_dim1 = 0, x_dim2 = 0;
  int y_dim1 = 0, y_dim2 = 0;
  cout << "input the first matrix's shape (x, y): ";
  cin >> x_dim1 >> y_dim1;
  cout << "input the second matrix's shape (x, y): ";
  cin >> x_dim2 >> y_dim2;

  Matrix m1 = create(x_dim1, y_dim1);
  Matrix m2 = create(x_dim2, y_dim2);

  // 分别为两个矩阵赋值并打印查看结果
  // m1不是对称矩阵
  init(m1, false);
  // m2是对称矩阵
  init(m2, true);
  
  print(m1);
  print(m2);

  cout << "is the first matrix symmetric? " << (isSymmetric(m1)? "Yes" : "No") << endl;
  cout << "is the second matrix symmetric? " << (isSymmetric(m2)? "Yes" : "No") << endl;
  return 0;
}
```

## 第四题

> `student.hpp`

```cpp
#pragma once
#include <string>

struct Student {
  int id;
  int age;
  std::string name;
};

void mySwap(double &, double &);

Student create(int id, int age, std::string name);
void print(const Student &);
void exchange(Student &, Student &);
```

> `student.cpp`

```cpp
#include "student.hpp"

#include <iostream>
#include <ostream>
#include <string>

void mySwap(double &v1, double &v2) {
  double temp = v1;
  v1 = v2;
  v2 = temp;
}

Student create(int id, int age, std::string name) {
  Student stu;
  stu.id = id;
  stu.age = age;
  stu.name = name;
  return stu;
}

void print(const Student &stu) {
  std::cout << "============ student info ============\n";
  std::cout << "name: " << stu.name << std::endl;
  std::cout << "id: " << stu.id << std::endl;
  std::cout << "age: " << stu.age << std::endl;
  std::cout << "======================================\n";
}

void exchange(Student &stu1, Student &stu2) {
  Student temp = stu1;
  stu1 = stu2;
  stu2 = temp;
}
```

> `question3.cpp`

```cpp
#include <iostream>

#include "student.hpp"

using namespace std;

int main() {
  double v1 = 3.4;
  double v2 = 4.3;
  Student stu1 = create(0, 18, "Shiming Yuan");
  Student stu2 = create(1, 20, "Ziliang Ye");

  cout << "double swap: \n";
  cout << "initial values: "
       << "v1 = " << v1 << ", v2 = " << v2 << endl;
  mySwap(v1, v2);
  cout << "swapped values: "
       << "v1 = " << v1 << ", v2 = " << v2 << endl;
  cout << "student swap: \n";
  cout << "initial students' info: \n";
  print(stu1);
  print(stu2);
  exchange(stu1, stu2);
  cout << "exchanged students' info: \n";
  print(stu1);
  print(stu2);
  return 0;
}
```