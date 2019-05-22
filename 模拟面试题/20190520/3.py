# -*- coding:utf-8 -*-

__author__ = 'huanghf'

"""
假设我们以下述方式将我们的文件系统抽象成一个字符串:

字符串 "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" 表示:

dir
    subdir1
    subdir2
        file.ext
目录 dir 包含一个空的子目录 subdir1 和一个包含一个文件 file.ext 的子目录 subdir2 。

字符串 "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" 表示:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
            
目录 dir 包含两个子目录 subdir1 和 subdir2。 
subdir1 包含一个文件 file1.ext 和一个空的二级子目录 subsubdir1。subdir2 包含一个二级子目录 subsubdir2 ，其中包含一个文件 file2.ext。
我们致力于寻找我们文件系统中文件的最长 (按字符的数量统计) 绝对路径。
例如，在上述的第二个例子中，最长路径为 "dir/subdir2/subsubdir2/file2.ext"，其长度为 32 (不包含双引号)。

给定一个以上述格式表示文件系统的字符串，返回文件系统中文件的最长绝对路径的长度。 如果系统中没有文件，返回 0。

说明:

文件名至少存在一个 . 和一个扩展名。
目录或者子目录的名字不能包含 .。
要求时间复杂度为 O(n) ，其中 n 是输入字符串的大小。

请注意，如果存在路径 aaaaaaaaaaaaaaaaaaaaa/sth.png 的话，那么  a/aa/aaa/file1.txt 就不是一个最长的路径。

"dir\n        file.txt" -> 12
"dirrrrrrrrrr\n        file.txt" -> 16
不是四个空格可以代替\t 而是         file.txt作为了新的根目录
"""


class Solution(object):
    def lengthLongestPath(self, s):
        """

        d:记录遍历时最新的path长度
        :type input: str
        :rtype: int
        """
        if not '.' in s:
            return 0
        d = {0: 0}
        max_depth = 0
        for line in s.split("\n"):
            name = line.lstrip("\t")
            depth = len(line) - len(name)
            if "." in name:
                print(len(name),depth)
                max_depth = max(max_depth, len(name) + d[depth])
            else:
                d[depth + 1] = len(name) + d[depth] + 1
        print(d)
        return max_depth

    def lengthLongestPath2(self, s):
        """
        测试样例太贱了。。。。
        :type input: str
        :rtype: int
        """
        if not '.' in s:
            return 0
        ls = s.split('\n')
        q = []
        m = 0
        for i in range(len(ls)):
            t = ls[i]
            c = 0
            j = 0
            # print(t[j:j+1]=='\t')
            while t[j:j + 1] == '\t':
                c += 1
                j += 1
            t = t[j:]
            m = max(m,c)
            q.append((c, t))
        res = ''
        max_length = 0
        paths = [[] for _ in range(m+1)]
        while q:
            level,filename = q.pop(0)
            if not '.' in filename:
                paths[level].append(filename+'/')
            if '.' in filename:
                # print(paths)
                if level!=0:
                    path = ''.join(paths[x][-1] for x in range(level))+filename
                else:
                    path = filename
                if len(path)>max_length:
                    res = path
                    max_length = len(path)
        print(res)
        return len(res)

sol = Solution()
s = "dir\n\t        file.txt\n\tfile2.txt"
print(sol.lengthLongestPath(s))
print(sol.lengthLongestPath2(s))
