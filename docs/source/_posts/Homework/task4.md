---
title: Homework | 第四次作业解答
date: 2023-11-06 17:07:12
category: Homework
---

**【作业情况】：正在批改**

<!--more-->

## question 0

> 猴子吃桃问题：猴子摘下若干个桃子，第一天吃了桃子的一半多一个，以后每天吃了前一天剩下的一半多一个，到第十天吃以前发现只剩下一个桃子，问猴子共摘了几个桃子。

```cpp
#include <iostream>

using namespace std;

int main() {
  int peach_sum{};
  int peach_remains = peach_sum;
  int total_day = 9;
  int exact_divide = true;
  while (true) {
    for (int day{}; day < total_day; day += 1) {
      peach_remains = peach_remains - (peach_remains / 2 + 1);
      // check for exactly division (except for the last day)
      if (peach_remains % 2 != 0 && day < total_day - 1) {
        exact_divide = false;
      }
    }
    // meet 2 requirements, the last day has only one peach and every step the
    // remains count can be exactly divided by 2
    if (peach_remains == 1 && exact_divide) {
      break;
    }
    // reset these variables
    peach_sum += 1;
    peach_remains = peach_sum;
    exact_divide = true;
  }
  cout << peach_sum << endl;
  return 0;
}
```

## question 1

> 将100元换成用10元、5元和1元的组合，共有多少种组合方法。  请把组合方法写入文件

**记得修改文件路径**

```cpp
#include <cstring>
#include <fstream>
#include <iostream>

using namespace std;

int main() {
  // relevent to cpp_dir/build
  string out_file_path{"path/to/your/file"};
  ofstream out_file{out_file_path, ios::out};
  const int total_mouny = 100;
  const int ten_tick = 10;
  const int five_tick = 5;
  const int one_tick = 1;
  out_file << "10 yuan 5 yuan 1 yuan\n";
  for (int ten_count{}; ten_count < total_mouny / ten_tick + 1;
       ten_count += 1) {
    int remains = total_mouny - ten_count * ten_tick;
    for (int five_count{}; five_count < remains / five_tick + 1;
         five_count += 1) {
      remains -= five_count * five_tick;
      if (remains < 0) {
        break;
      }
      out_file << "\t" << ten_count << "\t" << five_count << "\t" << remains << endl;
    }
  }
  out_file.close();
  return 0;
}
```

## question 2

> 一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如，6的因子为1、2、3，而6=1+2+3，28=1+2+4+7+14因此6，28是“完数”。编程序找出1000之内的所有的完数并输出到屏幕和文件data.txt

**记得修改文件路径**

```cpp
#include <cmath>
#include <fstream>
#include <iostream>

using namespace std;

int main() {
  string out_file_path{"path/to/your/file"};
  ofstream out_file{out_file_path, ios::out};
  const int max_limit = 1000;
  for (int num = 1; num < max_limit + 1; num += 1) {
    int fact_sum{};
    for (int f_num = 1; f_num < num; f_num += 1) {
      if (num % f_num != 0) continue;
      fact_sum += f_num;
    }
    if (fact_sum != num) continue;
    cout << num << endl;
    out_file << num << endl;
  }
  out_file.close();
  return 0;
}
```

## question 3

> 从文件data.txt读入数据，求平均值，并统计其中正数和负数的个数

**记得修改文件路径**

```cpp
#include <cstring>
#include <fstream>
#include <iostream>

using namespace std;

int main() {
  string in_file_path{"path/to/your/file"};
  ifstream in_file{in_file_path, ios::in};
  double value{};
  double avg{};
  int pos_count{};
  int neg_count{};
  while (in_file >> value) {
    if (value == 0) break;
    if (value < 0) neg_count += 1;
    if (value > 0) pos_count += 1;
    avg += value;
  }
  in_file.close();
  avg /= pos_count + neg_count;
  cout << "positive number: " << pos_count << endl;
  cout << "negtive number: " << neg_count << endl;
  cout << "average number: " << avg << endl;
  return 0;
}
```

## question 4

> iteration x_{n+1}=\frac{x_n^2 - 10(x_n sin(x_n) + cos(x_n))}{2 x_n - 10sin(x_n)} 
> solve the equation: x^2 + 10 cos(x) = 0

```cpp
#include <cmath>
#include <corecrt_math.h>
#include <iostream>


using namespace std;

double iterate(double x) {
  double numerator = x * x - 10 * (x * sin(x) + cos(x));
  double denominator = 2 * x - 10 * sin(x);
  return numerator / denominator;
}

int main() {
  double init_x{};
  double limit = 1e-5;
  cout << "input the init x (!= 0): ";
  cin >> init_x;
  if (fabs(init_x) < limit)
    return 1;
  double former_x = init_x;
  double current_x = iterate(init_x);
  while (fabs(current_x - former_x) >= limit) {
    double x_n = current_x;
    former_x = current_x;
    current_x = iterate(x_n);
  }
  cout << "solution is: " << current_x << " the error is: " << fabs(current_x - former_x) << endl;
  return 0;
}
```

注意问题的**多解性**
- 可以多尝试几个初值，会发现答案不止一个
- 可以使用绘图软件绘制函数，发现与 $y=0$ 的交点不止一个

其中绘图如下：

![function](Figure_1.png)

使用的是python绘图，代码如下：

```python
import matplotlib.pyplot as plt
import numpy as np

x = [_ for _ in np.linspace(-10, 10, 100)]
y = [_x * _x + 10 * np.cos(_x) for _x in x]
y_copy = [np.fabs(_x * _x + 10 * np.cos(_x)) for _x in x]
x_points = np.argsort(y_copy)[:4]
print(x_points)

plt.plot(x, y)
plt.plot(x, [0 for _ in x], 'k', label="$y=x^2+10cos(x)$")
for x_p in x_points:
    plt.plot(x[x_p], 0, 'ro')
    print((x[x_p], 0.0))
plt.legend()
plt.grid()
plt.show()
```