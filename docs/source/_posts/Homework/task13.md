---
title: Homework | 第十三次作业解答
date: 2024-01-08 21:05:56
category: Homework
---

第十三次作业解答

<!--more-->

## 第一题

```cpp

#include <cstddef>
#include <cstdlib>
#include <iostream>
// 不用管
#include <type_traits>

using namespace std;

// 不用管
template <typename V>
void print(V *arr, size_t arr_size) {
  for (size_t i = 0; i < arr_size; i += 1) cout << arr[i] << " ";
  cout << endl;
}

// 不用管
template <typename V>
void randInit(V *arr, size_t arr_size) {
  auto is_double = is_same<double, V>::value;
  if (is_double)
    for (auto i = 0; i < arr_size; i += 1)
      arr[i] = 10. * (double)rand() / RAND_MAX;
  for (auto i = 0; i < arr_size; i += 1) arr[i] = rand() % 10;
}

int *addVectors(int *A, size_t a_size, int *B, size_t b_size) {
  // 检查数组大小是否相同
  if (a_size != b_size) return nullptr;
  int *res = new int[a_size];
  for (size_t i = 0; i < a_size; i += 1) res[i] = A[i] + B[i];
  return res;
}

double findMagnitude(double *arr, size_t arr_size) {
  double magnitude = 0.;
  for (size_t i = 0; i < arr_size; i += 1) {
    magnitude += arr[i] * arr[i];
  }
  return sqrt(magnitude);
}

void normalizeVector(double *arr, size_t arr_size) {
  double magnitude = findMagnitude(arr, arr_size);
  for (size_t i = 0; i < arr_size; i += 1) {
    arr[i] /= magnitude;
  }
}

int main() {
  cout << "input 3 vactors' size: ";
  int a_size = 0;
  int b_size = 0;
  int c_size = 0;
  cin >> a_size >> b_size >> c_size;
  int *a_arr = new int[a_size];
  int *b_arr = new int[b_size];
  double *c_arr = new double[c_size];
  randInit(a_arr, a_size);
  randInit(b_arr, b_size);
  randInit(c_arr, c_size);

  cout << "random initialized arrays: " << endl;
  print(a_arr, a_size);
  print(b_arr, b_size);
  print(c_arr, c_size);

  cout << "test addVectors" << endl;
  int *added = addVectors(a_arr, a_size, b_arr, b_size);
  if (added != nullptr)
    print(added, a_size);
  else
    cout << "error in addVectors" << endl;

  cout << "test findMagnitude" << endl;
  double magnitude = findMagnitude(c_arr, c_size);
  cout << "magnitude of c_arr: " << magnitude << endl;

  cout << "test normalizedVector" << endl;
  normalizeVector(c_arr, c_size);
  print(c_arr, c_size);

  return 0;
}
```

## 第二题

```cpp
#include <cstddef>
#include <cstdlib>
#include <iostream>

using namespace std;

const size_t vector_dim = 3;

template <typename T>
void print3D(T *vec) {
  cout << "(";
  for (size_t i = 0; i < vector_dim; i += 1) cout << vec[i] << " ";
  cout << ")" << endl;
}

template <typename T>
void randInit(T *vec) {
  for (size_t i = 0; i < vector_dim; i += 1) vec[i] = rand() % 10;
}

int findDotProduct(int *vec_a, int *vec_b) {
  return vec_a[0] * vec_b[0] + vec_a[1] * vec_b[1] + vec_a[2] * vec_b[2];
}

int *findCrossProduct(int *vec_a, int *vec_b) {
  int *crossed = new int[vector_dim];
  crossed[0] = vec_a[1] * vec_b[2] - vec_a[2] * vec_b[1];
  crossed[1] = vec_a[2] * vec_b[0] - vec_a[0] * vec_b[2];
  crossed[2] = vec_a[0] * vec_b[1] - vec_a[1] * vec_b[0];
  return crossed;
}

bool isOrthogonal(int *vec_a, int *vec_b) {
  return findDotProduct(vec_a, vec_b) == 0;
}

int main() {
  int *vec_a = new int[vector_dim];
  int *vec_b = new int[vector_dim];
  randInit(vec_a);
  randInit(vec_b);

  cout << "defined vectors: " << endl << endl;
  print3D(vec_a);
  print3D(vec_b);

  cout << "test cross product: " << endl;
  print3D(findCrossProduct(vec_a, vec_b));
  cout << endl;

  cout << "test isOrthogonal: " << endl;
  cout << isOrthogonal(vec_a, vec_b) << endl;

  return 0;
}
```

## 第三题

```cpp
#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

bool relativePrime(int a, int b) {
  int cd = min(a, b);
  for (; cd > 1; cd -= 1) {
    if (a % cd == 0 && b % cd == 0) {
      return false;
    }
  }
  return true;
}

int findPrimePair(int* arr, int arr_size) {
  int count = 0;
  for (int i = 0; i < arr_size; i += 1) {
    for (int j = i + 1; j < arr_size; j += 1) {
      if (relativePrime(arr[i], arr[j])) {
        count += 1;
      }
    }
  }
  return count;
}

int main() {
  int arr_size = 0;
  cin >> arr_size;
  int* arr = new int[arr_size];
  for (int i = 0; i < arr_size; i += 1) {
    cin >> arr[i];
  }
  int count = findPrimePair(arr, arr_size);
  cout << (count == 0 ? "No" : to_string(count)) << " pair of prime numbers";
  return 0;
}
```

## 第四题

```cpp
#include <climits>
#include <cstdlib>
#include <iostream>

using namespace std;
const int f = 4;
const int w = 20;
const int s = 2;
/*卷积函数 cvn 声明:
fs: 原始特征信号在内存空间中存放的首地址
flt: 卷积核存放的首地址
fm_w: 原始特征信号长度
fm_f: 卷积核长度
fm_s: 卷积步长
max_index: 卷积后特征信号的最大值下标
*/
int* cnv(int* fs, int* flt, int fm_w, int fm_f, int fm_s, int& max_index);
int main() {
  // 添加代码 1：。。。。。
  int filter[f] = {-1, 2, 0, 1};
  int featuresig[w] = {0};
  for (int i = 0; i < w; i += 1) {
    featuresig[i] = rand() % 10 - 5;
    cout << featuresig[i] << " ";
  }
  cout << endl;
  // 添加代码 2: 。。。。
  int index = 0;
  int* cvs_fs = cnv(featuresig, filter, w, f, s, index);
  // 输出卷积后的特征值
  int new_fs_size = (w - f) / s + 1;
  for (int i = 0; i < new_fs_size; i += 1) {
    cout << cvs_fs[i] << " ";
  }
  cout << endl;
  // 输出最大卷积特征值下标
  cout << index << endl;
  // （2 分）添加代码 3: 完成必要的善后工作
  return 0;
}

int* cnv(int* fs, int* flt, int fm_w, int fm_f, int fm_s, int& max_index) {
  int new_fs_size = (fm_w - fm_f) / fm_s + 1;
  int* new_fs = new int[new_fs_size];
  int index = -1;
  for (int i = 0; i < fm_w; i += fm_s) {
    index += 1;
    new_fs[index] = 0;
    for (int j = i; j < i + fm_f; j += 1) {
      new_fs[index] += fs[j] * flt[j - i];
    }
  }
  int max_v = INT_MIN;
  for (int i = 0; i < new_fs_size; i += 1) {
    if (max_v < new_fs[i]) {
      max_index = i;
      max_v = new_fs[i];
    }
  }
  return new_fs;  // 返回存放特征值动态数组的首地址
}
```