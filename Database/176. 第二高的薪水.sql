
/*
编写一个 SQL 查询，获取 Employee 表中第二高的薪水（Salary） 。

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
例如上述 Employee 表，SQL查询应该返回 200 作为第二高的薪水。如果不存在第二高的薪水，那么查询应返回 null。

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+



DISTINCT 去重
ORDER BY Salary:  对 Salary 排序(从小到大)
DESC: 逆序排序 (从大到小)
OFFSET 1: 第 1 条数据之后的数据(从第二条开始)
LIMIT 1: 取第 2条数据
直接使用 SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT 1 OFFSET 1 AS SecondHighestSalary 取不出 NULL
可以使用临时表: select (...) as SecondHighestSalary

或者使用 IFNULL:

SELECT
    IFNULL(
      (SELECT DISTINCT Salary
       FROM Employee
       ORDER BY Salary DESC
        LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary

*/

SELECT (SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT 1 OFFSET 1) AS SecondHighestSalary

