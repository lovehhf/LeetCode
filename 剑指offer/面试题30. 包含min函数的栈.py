# -*- coding:utf-8 -*-

"""
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

示例:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.


提示：
各函数的调用总次数不超过 20000 次
 
注意：本题与主站 155 题相同：https://leetcode-cn.com/problems/min-stack/
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class MinStack:

    def __init__(self):
        """
        栈: 先进后出
        可以定义最小栈 min_stack: 按元素进入的顺序, 只存储单调递减的元素,
        新元素 x > 栈顶元素时不存入最小栈中, 因为 x 肯定是比最小栈中的栈顶元素先出去的, 最小值不可能是x
        initialize your data structure here.
        """
        self.stk = []
        self.min_stk = []  # 最小栈

    def push(self, x: int) -> None:
        self.stk.append(x)
        if not self.min_stk or x <= self.min_stk[-1]:
            self.min_stk.append(x)

    def pop(self) -> None:
        x = self.stk.pop()
        if x == self.min_stk[-1]:
            self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def min(self) -> int:
        return self.min_stk[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
