---
title: Homework | 第十一次作业解答
date: 2024-01-08 20:48:38
category: Homework
---

解答

<!--more-->

## 第一题

```cpp
/**
 * 1. 定义选择排序、冒泡排序还有插入排序的函数，输入一组整数，完成排序。
 */

#include <iostream>
#include <stdint.h>
#include <stdlib.h>
#include <type_traits>

using namespace std;

const int arr_size = 10;

void printArray(int *arr, int size) {
  for (int i = 0; i < size; i += 1) {
    cout << arr[i] << " ";
  }
  cout << endl;
}

void initArray(int *arr, int size) {
  for (int i = 0; i < size; i += 1) {
    arr[i] = rand() % 10;
  }
}

/**
 * 选择排序的思路：
 * 将排序**每一步**的数组视为“已经排好序”的部分和“还没排好序”的部分
 * 在还没排好序的部分里面选择最小的元素，放入排好序的部分的末尾
 * 该函数假设
 * [0, ordered_tail) 的部分已经排好序了，
 * [ordered_tail, size) 的部分还没排好序
 */
void selectSort(int *arr, int size) {
  // 还没被排序的开始下标
  int ordered_tail = 0;
  for (int i = 0; i < size; i += 1) {
    // 由于是最小值，可以使用c++内置的宏定义的int类型最大值初始化
    int unorder_min = INT_MAX;
    int min_index = -1;
    // 排序的每一步，从未排序的部分选择最值（这里选择最小值）
    for (int j = ordered_tail; j < size; j += 1) {
      if (arr[j] < unorder_min) {
        unorder_min = arr[j];
        min_index = j;
      }
    }
    // 此时找到了最小值，将其和ordered_tail位置上的元素交换
    swap(arr[ordered_tail], arr[min_index]);
    // 更新排好序的长度
    ordered_tail += 1;
  }
}

/**
 * 冒泡排序的思路：
 * 将较小的元素逐一往前移动
 * 数组前面的unorderer_tail个元素都已经排好序
 * 排序的每一步中，
 */
void bubbleSort(int *arr, int size) {
  int unordered_tail = size;
  for (int i = 0; i < unordered_tail; i += 1) {
    for (int j = unordered_tail - 1; j > i; j -= 1) {
      if (arr[j] < arr[j - 1]) {
        swap(arr[j], arr[j - 1]);
      }
    }
  }
}

/**
 * 插入排序的思路：
 * 还是和之前类似，一个数组可以分成排好序的和未排好序的
 * 对于排序算法的每一步
 * 从未排序的部分选择一个数**插入**到排好序的相应位置上（注意没有限制是不是选取最值）
 */
void insertSort(int *arr, int size) {
  // 第一个数本身就是有序的，所以从第二个开始数组无序
  int ordered_tail = 1;
  for (int i = 1; i < size; i += 1) {
    // 选择无序部分的第一个插入到有序的部分
    int insert_loc = -1;
    int insert_val = arr[ordered_tail];
    for (int j = 0; j < ordered_tail; j += 1) {
      // 找插入的位置，找第一个大于它的数
      if (insert_val < arr[j]) {
        insert_loc = j;
        break;
      }
    }
    // 没有小于任何一个值，也就是需要插到末尾
    // 也就是不需要插
    if (insert_loc != -1) {
      // 插入元素
      for (int j = ordered_tail; j > insert_loc; j -= 1) {
        arr[j] = arr[j - 1];
      }
      arr[insert_loc] = insert_val;
    }
    ordered_tail += 1;
  }
}

int main() {
  int arr[arr_size] = {0};
  initArray(arr, arr_size);
  printArray(arr, arr_size);
  //   selectSort(arr, arr_size);
  //   bubbleSort(arr, arr_size);
  insertSort(arr, arr_size);
  printArray(arr, arr_size);
  return 0;
}

```

## 第二题

```cpp
/**
2. 按照课堂讲解学生的结构体，包含学号、 姓名，年龄，和
语文、数学及英文成绩，建立一个长度为5的学生数组，初始化student数组的5个数据：
（1）写出按照学号做升序排序函数；
（2）写出二分折半查找算法函数，输入一位同学信息（student
的结构体变量），输出这位同学在数组的位置或者不存在这位同学。
 */

#include <iostream>
#include <sstream>
#include <stdlib.h>
#include <string>

using namespace std;

const int student_count = 5;
const int student_max_name_length = 10;

struct Student {
  int id;
  int age;
  double chinese_score;
  double math_score;
  double english_score;
  string name;

  Student() {}

  Student(int id, int age, double chinese_score, double math_score,
          double english_score, string name) {
    this->id = id;
    this->age = age;
    this->chinese_score = chinese_score;
    this->math_score = math_score;
    this->english_score = english_score;
    this->name = name;
  }

  Student(int id) {
    this->id = id;
    this->age = 17 + rand() % 5;
    this->chinese_score = rand() % 100;
    this->math_score = rand() % 100;
    this->english_score = rand() % 100;
    // this->name = 'a' + rand() % 26;
    for (int n = 0; n < student_max_name_length; n += 1) {
      this->name += 'a' + rand() % 26;
    }
  }

  void printInfo() {
    cout << "\n==== "
         << "Student Info"
         << " ====" << endl;
    cout << "id = " << this->id << endl;
    cout << "name = " << this->name << endl;
    cout << "age = " << age << endl;
    cout << "Chinese score = " << this->chinese_score << endl;
    cout << "Math score = " << this->math_score << endl;
    cout << "English score = " << this->english_score << endl;
  }
};

/**
 * 选择排序，直接使用上一题的函数即可
 */
void selectSort(Student *arr, int size) {
  int ordered_tail = 0;
  for (int i = 0; i < size; i += 1) {
    int unorder_min = INT_MAX;
    int min_index = -1;
    for (int j = ordered_tail; j < size; j += 1) {
      if (arr[j].id < unorder_min) {
        unorder_min = arr[j].id;
        min_index = j;
      }
    }
    swap(arr[ordered_tail], arr[min_index]);
    ordered_tail += 1;
  }
}

/**
 * 二分查找
 */
int find(Student *arr, int size, Student other) {
  int head = 0;
  int tail = size - 1;
  int mid = head + (tail - head) / 2;
  while (head < tail) {
    if (arr[mid].id < other.id) head = mid;
    if (arr[mid].id > other.id) tail = mid;
    if (arr[mid].id == other.id) return mid;
    mid = head + (tail - head) / 2;
  }
  return size;
}

int main() {
  // 下面这句话相当于
  // Student group[student_count];
  auto *group = new Student[student_count];
  cout << "input the id of " << student_count << " students: ";
  for (unsigned i = 0; i < student_count; i += 1) {
    unsigned id = 0;
    cin >> id;
    group[i] = Student(id);
  }
  cout << "the group info is: " << endl;
  for (unsigned i = 0; i < student_count; i += 1) group[i].printInfo();

  cout << "the sorted group info is: " << endl;
  selectSort(group, student_count);
  for (unsigned i = 0; i < student_count; i += 1) group[i].printInfo();

  cout << "input the student id to look up: ";
  int id = 0;
  cin >> id;
  auto other = Student(id);
  int loc = find(group, student_count, other);
  if (loc >= student_count) cout << "find nothing" << endl;
  else cout << "find the student in " << loc + 1 << " position" << endl;
  return 0;
}
```

## 第三题

```cpp
#include <cstring>
#include <iostream>

using namespace std;

int isPalindrome(char *str) {
  auto len = strlen(str);
  for (int i = 0; i < (len - 1) / 2; i += 1) {
    if (str[i] != str[len - 1 - i]) return false;
  }
  return true;
}

int main() {
  char str[] = {};
  cin >> str;
  auto res = isPalindrome(str);
  cout << res << endl;
  return 0;
}
```

## 第四题

```cpp
#include <cstddef>
#include <cstring>
#include <iostream>

using namespace std;

const unsigned buffer_size = 1024;

int wordCounter(char *str) {
  auto len = strlen(str);
  int count = 0;
  for (size_t i = 0; i < len - 1; i += 1) {
    if ((str[i] == ' ' || str[i] == '\t') && i != len - 2) count += 1;
  }
  return count + 1;
}

int main() {
  char str[buffer_size] = {};
  cin.getline(str, buffer_size);
  int count = wordCounter(str);
  cout << count << endl;
  return 0;
}
```