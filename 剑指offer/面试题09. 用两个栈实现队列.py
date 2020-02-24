# -*- coding:utf-8 -*-

"""
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

示例 1：
输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]

示例 2：
输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
提示：

1 <= values <= 10000
最多会对 appendTail、deleteHead 进行 10000 次调用

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class CQueue:

    def __init__(self):
        self.stk1 = []  # 栈 1 用来追加元素
        self.stk2 = []  # 栈 2 用来弹出元素

    def appendTail(self, value: int) -> None:
        """
        元素入队列
        先将栈 2 的元素都倒到栈 1 里面, 再将要入队列的元素追加到栈 1
        :param value:
        :return:
        """
        while (self.stk2):
            self.stk1.append(self.stk2.pop())
        self.stk1.append(value)

    def deleteHead(self) -> int:
        """
        队列弹出元素
        先将栈 1 的元素倒入到栈 2, 再将元素弹出
        :return:
        """
        while (self.stk1):
            self.stk2.append(self.stk1.pop())
        return self.stk2.pop() if self.stk2 else -1


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
