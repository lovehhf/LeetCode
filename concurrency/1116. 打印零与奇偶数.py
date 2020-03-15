# -*- coding:utf-8 -*-

"""
假设有这么一个类：

class ZeroEvenOdd {
  public ZeroEvenOdd(int n) { ... }      // 构造函数
  public void zero(printNumber) { ... }  // 仅打印出 0
  public void even(printNumber) { ... }  // 仅打印出 偶数
  public void odd(printNumber) { ... }   // 仅打印出 奇数
}
相同的一个 ZeroEvenOdd 类实例将会传递给三个不同的线程：

线程 A 将调用 zero()，它只输出 0 。
线程 B 将调用 even()，它只输出偶数。
线程 C 将调用 odd()，它只输出奇数。
每个线程都有一个 printNumber 方法来输出一个整数。请修改给出的代码以输出整数序列 010203040506... ，其中序列的长度必须为 2n。

示例 1：
输入：n = 2
输出："0102"
说明：三条线程异步执行，其中一个调用 zero()，另一个线程调用 even()，最后一个线程调用odd()。正确的输出为 "0102"。

示例 2：
输入：n = 5
输出："0102030405"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/print-zero-even-odd
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import threading

def printNumber(x):
    print(x, end='')

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.lock_zero = threading.Lock();
        self.lock_even = threading.Lock();
        self.lock_odd = threading.Lock();
        self.lock_odd.acquire()  # 先把奇数和偶数锁起来, 只让0先打印
        self.lock_even.acquire()

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.lock_zero.acquire()  # 取锁成功
            printNumber(0)
            # i 是奇数数给偶数解锁, 是偶数时给奇数解锁
            if (i & 1):
                self.lock_even.release()
            else:
                self.lock_odd.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.lock_even.acquire()
            printNumber(i)
            self.lock_zero.release()  # 不管是奇数还是偶数都给 0 解锁

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.lock_odd.acquire()
            printNumber(i)
            self.lock_zero.release()
