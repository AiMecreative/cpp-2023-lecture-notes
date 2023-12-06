---
title: Homework | 第9次作业解答
date: 2023-12-06 15:29:00
category: Homework
---

**【批改情况会私法给同学】**

<!--more-->

## question 0

```cpp
/**
 * 数组基本应用：建立长度为10的数组，屏幕输入10个整数，输出其中最大的奇数与最大的偶数，注意需要考虑输入的数列中有没有奇数或者偶数的情况。
 * 注意在数列中有可能没有奇数或者偶数问题可以由统计个数来确定。
 */

#include <iostream>
#include <sstream>

using namespace std;

const int ary_size = 10;

// 判断是否是奇数
bool isOdd(int value) { return value % 2 == 1; }

// 判断是否是偶数
bool isEven(int value) { return value % 2 == 0; }

int main() {
  int ary[ary_size] = {0};
  // 输入的数可能有负数，不好确定最大值的初始值
  // 因此选择使用 INT_MIN
  int max_odd = INT_MIN;
  int max_even = INT_MIN;
  // 记录奇数和偶数的个数
  int odd_count = 0;
  int even_count = 0;
  cout << "input 10 integers: ";
  for (int i = 0; i < ary_size; i += 1) {
    cin >> ary[i];
    // 如果是偶数，且大于当前的最大值，则刷新最大值，记录为新的最大值
    if (isEven(ary[i]) && max_even < ary[i]) {
      max_even = ary[i];
      even_count += 1;
    }
    // 如果是奇数，同理
    if (isOdd(ary[i]) && max_odd < ary[i]) {
      max_odd = ary[i];
      odd_count += 1;
    }
  }
  // 可以使用 stringstream 来格式化输出
  stringstream even_result, odd_result;
  even_count > 0
      ? (even_result << "the max even number is: " << max_even << "\n")
      : (even_result << "no even number in array\n");
  odd_count > 0
      ? (even_result << "the max odd number is: " << max_odd << "\n")
      : (even_result << "no odd number in array\n");
  cout << even_result.str() << odd_result.str() << endl;
  return 0;
}

```

## question 1

```cpp
/**
 * 2. 数组下标使用及数组为形参的函数定义
〔题目〕本程序用于查找一组数中呈现峰值的数及其个数。所谓呈现峰值的数，是指满足下列条件的数组元素a[i]：
a[i-1]<a[i] 且 a[i]>a[i+1] 尖峰 或者  a[i-1]>a[i] 且
a[i]<a[i+1]，低谷。其中：1<=i<=n-1 例如，数组： a[0]  a[1]  a[2]  a[3]  a[4]
a[5]  a[6]  a[7]  a[8] 12   13    21     34    32    41     24    12    11
中a[3]既大于a[2]又大于a[4]，a[4]既小于a[3]又小于a[5]。故a[3]、a[4]、a[5]即为正、负峰值(不含第0个和最后一个)
运行时可输入如下数据调式程序：
   12 13 21 34 32 41 24 12 11       //2个峰值，34和41，一个低谷32
   11 12 13 14 15 16 17 18 19       //0个峰值
要求：
（1）在主函数中，定义数组a大小为15，数字数据由文件file1.txt中读入后由屏幕输出，找出结果，并存入数组b中，并输出查找的结果（包括文件输出和屏幕输出）输出的文件为file2.txt。
（2）【运行结果】
9个测试数据如下：
a[i]= 12  13  21  34  32  41  24  12  11
计算结果：
b[i]= 34  41 有2个峰值， 32 低谷
（3）查找峰值+低谷的个数由函数完成，函数返回值为峰值+低谷的个数；
 */

#include <fstream>
#include <iostream>
#include <string>

using namespace std;

const int ary_size = 15;
const string cpp_path = "";  // 或者替换成你自己cpp的绝对路径，主要针对cmake用户
const string data_file = "file1.txt";
const string output_file = "file2.txt";

// 找峰值的函数，数组传参也可以使用 int[] ary，
// res表示结果，结果的数组大小不可能大于ary
int peak(int *ary, int *res, int ary_size) {
  // 只有 size 大于或等于 3 才可能出现峰值
  if (ary_size < 3) {
    return 0;
  }
  int peak_count = 0;
  // 峰值不可能出现在两端，所以注意遍历的上下限
  for (int i = 1; i < ary_size - 1; i += 1) {
    if (ary[i - 1] < ary[i] && ary[i + 1] < ary[i]) {
      res[peak_count] = ary[i];
      peak_count += 1;
    }
    if (ary[i] < ary[i - 1] && ary[i] < ary[i + 1]) {
      res[peak_count] = ary[i];
      peak_count += 1;
    }
  }
  return peak_count;
}

int main() {
  // 定义 a数组和 b数组
  int a[ary_size] = {0};
  int b[ary_size] = {0};
  // 定义文件路径并打开文件
  ifstream ifile;
  ofstream ofile;
  ifile.open(cpp_path + data_file);
  ofile.open(cpp_path + output_file);
  // 读入数据
  for (int i = 0; i < ary_size; i += 1) {
    ifile >> a[i];
  }
  // 找峰值
  int peak_count = peak(a, b, ary_size);
  // 输出文件和console内容
  for (int i = 0; i < peak_count; i += 1) {
    ofile << b[i] << " ";
    cout << b[i] << " ";
  }
  cout << endl;
  return 0;
}

```


## question 2

```cpp
/**
 * 3. 使用一维数组作为函数参数解决问题：
建立一个长度为10的数组，从键盘由大到小输入9个有序的整数，形成一个有序的数列依次存放到数组中；然后再输入一个数，把这个数放到数组的正确位置，使得数组依然有序（不能使用排序方法重新排序）。
例如 ，数组为data[10]， 预先输入， 1, 3 , 4, 6, 8, 12, 14, 16, 20;
然后再从键盘接收一个数，例如为 5，最后的数组结果为，1, 3 , 4, 5, 6, 8, 12, 14,
16, 20。
提示，算法采用数组的搬移，
第一步：创建数组，读入9个有序的数字；
第二步：再读入一个数，然后在数组上遍历，找到新数应该处于的位置i，即当在数组中发现第一个大于新数的位置，就在它的前面停止下来；
第三步：从i+1到9，数组依次向后搬移，注意搬移要从后面开始，即从第9个开始向后依次到第i+1个；
第四步：把输入的数字放到位置i上；
void appenddata(int data[], int n, int data)
 */

#include <iostream>

using namespace std;

const int ary_size = 10;

void appenddata(int *ary, int ary_size, int data) {
  // 插入数据的位置
  int insert_loc = ary_size - 1;
  for (int i = 0; i < ary_size; i += 1) {
    if (ary[i] < data) {
      insert_loc = i;
      break;
    }
  }
  // 从insert_loc开始到ary_size结束，开始搬移数据
  // 注意要从末尾开始搬移，即用前一个数据覆盖后一个数据
  for (int i = ary_size - 1; i >= insert_loc; i -= 1) {
    ary[i] = ary[i - 1];
  }
  // 插入数据
  ary[insert_loc] = data;
}

int main() {
  int ary[ary_size] = {0};
  int data = 0;
  for (int i = 0; i < ary_size - 1; i += 1) {
    cin >> ary[i];
  }
  cout << "append data: ";
  cin >> data;
  appenddata(ary, ary_size, data);
  for (int i = 0; i < ary_size; i += 1) {
    cout << ary[i] << " ";
  }
  cout << endl;
  return 0;
}
```

## question 3

```cpp
/**
 * 4. 建立函数，功能是删除数组中指定的数字， 例如数组定义数组a[10]，输入8个数字
1,2,3,3,5,5,6,3 之后， 删除数字3， 之后 数组为 1,2,5,5,6。
删除数字之后要更新数组有效长度。
函数定义：
int erasedata( int data[], int n, int data)
data为操作的数组， n为数组原来有效长度，data为删除的数据，
返回值为数组新的长度。
 */

#include <iostream>

using namespace std;

const int ary_size = 10;

int eraseData(int *ary, int valid_size, int data) {
  int new_size = valid_size;
  int erase_loc = valid_size;
  // 首先需要查找是否存在这个data，
  // 这里直接用最简单的遍历查找（一般而言是使用二分查找）
  for (int i = 0; i < valid_size; i += 1) {
    if (ary[i] == data) {
      erase_loc = i;
      break;
    }
  }
  // 如果erase_loc大于或等于原来的有效长度，则说明不存在这个元素，所以不需要更新
  if (erase_loc >= valid_size) return new_size;
  // 否则更新数组，直接用erase_loc后面的元素依次覆盖前面的元素
  for (int i = erase_loc; i < valid_size - 1; i += 1) ary[i] = ary[i + 1];
  new_size -= 1;
  return new_size;
}

int main() {
  int ary[ary_size] = {0};
  int valid_size = 0;
  cout << "define the valid size:";
  cin >> valid_size;
  cout << "input the data:";
  for (int i = 0; i < valid_size; i += 1) cin >> ary[i];
  int data = 0;
  cout << "erase data is:";
  cin >> data;
  valid_size = eraseData(ary, valid_size, data);
  cout << "the valid size is:" << valid_size << endl << "the updated array is:";
  for (int i = 0; i < valid_size; i += 1) cout << ary[i] << " ";
  cout << endl;
  return 0;
}
```