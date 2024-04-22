---
title: Homework | 第八次作业解答
date: 2024-04-22 15:01:10
category: Homework
---

第八周作业解答

<!--more-->

# question 0

!! **本题重载了输出流运算符，可以直接使用cout进行输出**

编程建立一个图书类的对象数组，并检查该数组是否根据图书的借阅量排序。
（1）图书类的定义包括，图书名称，作者，图书简介以及借阅量；
（2）通过构造函数完成string以及char *对象成员的初始化；设计复制构造函数支持深复制；
（3）按照排序算法的支持要求设计对应的运算符重载函数。本题内容包在下面的代码，按照要求完善出来。

```cpp
#include <cstring>
#include <iostream>
#include <ostream>
#include <string.h>
#include <string>

using namespace std;

class Book {
private:
  const int INIT_DESCRIPTION_SIZE = 20;
  string _bookname;
  string _author;
  char *_description;
  int _lending_times;

public:
  Book() : _bookname(), _author(), _lending_times(0) {
    _description = new char[INIT_DESCRIPTION_SIZE + 1];
    _description[0] = '\0';
  }
  Book(const string &bookname, const string &author, const char *description,
       const int lending_times)
      : _bookname(bookname), _author(author), _lending_times(lending_times) {
    int des_size = strlen(description) + 1;
    _description = new char[des_size];
    strcpy_s(_description, des_size, description);
  }
  Book(const Book &other)
      : _bookname(other._bookname), _author(other._author),
        _lending_times(other._lending_times) {
    int des_size = strlen(other._description) + 1;
    _description = new char[des_size];
    strcpy_s(_description, des_size, other._description);
  }
  ~Book() {
    delete[] _description;
    _description = nullptr;
  }

  void setInfo(const string &bookname, const string &author,
               const char *description, const int lending_times) {
    _bookname = bookname;
    _author = author;
    _lending_times = lending_times;

    int des_size = strlen(description) + 1;
    if (_description != nullptr) {
      delete[] _description;
    }
    _description = new char[des_size];
    strcpy_s(_description, des_size, description);
  }

  void getInfo(string &bookname, string &author, char *description,
               int &lending_times) {
    bookname = _bookname;
    author = _author;
    _lending_times = lending_times;

    int des_size = strlen(_description) + 1;
    if (description != nullptr) {
      delete[] description;
    }
    description = new char[des_size];
    strcpy_s(description, des_size, _description);
  }

  // 重载了int的强制转换，方便后续用于比较大小
  operator int() { return _lending_times; }

  // 重载了流运算符，方便后续直接使用cout进行输出，代替了原题目中的print函数
  friend ostream &operator<<(ostream &out, const Book &book) {
    out << "|--------------- Book ---------------|\n";
    out << "| book name: " << book._bookname << endl;
    out << "| author name: " << book._author << endl;
    out << "| description: ";
    for (int i = 0; i < strlen(book._description); i += 1) {
      out << book._description[i];
    }
    out << endl;
    out << "| lending times: " << book._lending_times << endl;
    out << "|-----------------------------------|\n";

    return out;
  }
};

template <typename T> bool isDescendingSorted(T *ary, int size) {
  bool res = true;
  for (int i = 1; i < size; i += 1) {
    int p1 = (int)(ary[i - 1]);
    int p2 = (int)(ary[i]);
    if (p1 < p2) {
      res = false;
    }
  }
  return res;
}

int main() {
  Book book_ary[5] = {
      Book("一句顶一万句", "刘震云", "底层百姓人物的故事", 200),
      Book("蛙", "莫言", "乡村女医生的人生经历", 180),
      Book("推拿", "毕飞宇", "推拿中盲人的情感、尊严和梦想", 170),
      Book("你在高原", "张炜", "地址队员的故事", 160),
      Book("天行者", "刘醒龙", "乡村民办教师的故事", 150),
  };
  for (int i = 0; i < 5; i += 1) {
    cout << book_ary[i] << endl;
  }

  cout << (isDescendingSorted(book_ary, 5) ? "sorted!" : "unsorted!") << endl;

  Book book1;
  book1.setInfo("人世间", "梁晓声", "中国社会的巨大变迁和百姓生活", 150);
  cout << book1 << endl;

  Book book2 = book1;
  cout << book2 << endl;

  return 0;
}
```

# question 1

链表的操作规整成为函数完成。

包括：

- 打印链表
- 在前插入结点、在后插入结点
- 查询结点
- 删除结点
- 清空链表
- 计算链表长度

```cpp
#include <iostream>
#include <stdlib.h>

using namespace std;

struct Node {
  int value;
  Node *next;
};

void printList(const Node *head) {
  cout << "[HEAD] -> ";
  Node *p = head->next;
  while (p != nullptr) {
    cout << "[" << p->value << "]"
         << " -> ";
    p = p->next;
  }
  cout << "[TAIL]" << endl;
}

void insertFront(Node *node, Node *head, Node *&tail) {
  node->next = head->next;
  if (tail == head) {
    tail = node;
  }
  head->next = node;
}

// 这里把head也作为参数传进来是为了和上述函数统一接口参数
// 如果以后需要调用插入结点的函数，可以直接修改函数名
// 方便以后可以使用函数指针
void insertRear(Node *node, Node *head, Node *&tail) {
  tail->next = node;
  tail = node;
}

Node *find(int value, const Node *head) {
  Node *p = head->next;
  while (p != nullptr) {
    if (p->value == value) {
      return p;
    }
    p = p->next;
  }
  return p;
}

int length(const Node *head) {
  Node *p = head->next;
  int len = 0;
  while (p != nullptr) {
    len += 1;
    p = p->next;
  }
  return len;
}

void makeEmpty(Node *head, Node *&tail) {
  Node *p = head;
  while (p->next != nullptr) {
    Node *q = p->next;
    p->next = q->next;
    delete q;
    q = nullptr;
  }
  tail = head;
}

void deleteNode(int value, Node *head, Node *&tail) {
  Node *p = head;
  while (p->next != nullptr) {
    if (p->next->value == value) {
      Node *q = p->next;
      p->next = q->next;
      delete q;
      q = nullptr;
    }
    p = p->next;
  }
  cout << "no node should be deleted" << endl;
}

int main() {
  // initialize
  Node *head = new Node;
  head->value = 0;
  head->next = nullptr;
  Node *tail = head;

  // insert 3 nodes in the front
  for (int i = 0; i < 3; i += 1) {
    Node *node = new Node;
    node->value = rand() % 10;
    node->next = nullptr;
    insertFront(node, head, tail);
    cout << "insert node [" << node->value << "] in the front:" << endl;
    printList(head);
  }

  // insert 3 nodes in the tail
  for (int i = 0; i < 3; i += 1) {
    Node *node = new Node;
    node->value = rand() % 10;
    node->next = nullptr;
    insertRear(node, head, tail);
    cout << "insert node [" << node->value << "] in the tail:" << endl;
    printList(head);
  }

  int target = rand() % 10;
  cout << "wish to find [" << target << "] in the list: ";
  Node *find_res = find(target, head);
  cout << (find_res != nullptr ? "success!" : "fail!") << endl;

  int delete_value = rand() % 10;
  cout << "wish to delete [" << delete_value
       << "] in the list, deleted result: " << endl;
  deleteNode(delete_value, head, tail);
  printList(head);

  cout << "make empty:" << endl;
  makeEmpty(head, tail);
  printList(head);
  return 0;
}
```