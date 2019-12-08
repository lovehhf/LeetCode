# -*- coding:utf-8 -*-

"""
有 n 位用户参加活动，他们的 ID 从 0 到 n - 1，每位用户都 恰好 属于某一用户组。给你一个长度为 n 的数组 groupSizes，其中包含每位用户所处的用户组的大小，请你返回用户分组情况（存在的用户组以及每个组中用户的 ID）。

你可以任何顺序返回解决方案，ID 的顺序也不受限制。此外，题目给出的数据保证至少存在一种解决方案。

 

示例 1：

输入：groupSizes = [3,3,3,3,3,1,3]
输出：[[5],[0,1,2],[3,4,6]]
解释：
其他可能的解决方案有 [[2,1,6],[5],[0,4,3]] 和 [[5],[0,6,2],[4,3,1]]。
示例 2：

输入：groupSizes = [2,1,3,3,3,2]
输出：[[1],[0,5],[2,3,4]]
 

提示：

groupSizes.length == n
1 <= n <= 500
1 <= groupSizes[i] <= n

CPP:
class Solution {
public:
    vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
        unordered_map <int, vector<int>> dict; // 键： 某个组的人数, 值: 用户索引数组
        vector<vector<int>> res;

        for(int i = 0; i < groupSizes.size(); i ++)
        {
            int k = groupSizes[i];
            dict[k].push_back(i);
            // 只要某个组人数满了就推到res中, 并清空这个数组重新装用户
            if(dict[k].size() >= k)
            {
                res.push_back(dict[k]);
                dict.erase(k);
            }
        }
        return res;
    }
};
"""

from typing import List

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        n = len(groupSizes)
        # 带上索引按小组人数排序
        group = sorted([(i, groupSizes[i]) for i in range(n)], key = lambda x:x[1])
        res = []
        i = 0
        while (i < n):
            t = group[i][1]
            res.append([group[i][0] for i in range(i, i + t)])
            i += t
        return res

s = Solution()
print(s.groupThePeople([3,3,3,3,3,1,3]))