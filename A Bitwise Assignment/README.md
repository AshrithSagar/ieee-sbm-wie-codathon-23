# A Bitwise Assignment

> https://www.hackerrank.com/contests/ieee-sbm-wie-codathon-23/challenges/a-bitwise-assignment

---

A teacher gave an assignment to her students. If given a positive integer m, they should find the minimum positive integer n, which will satisfy the following two conditions:
- m and n > 0
- m xor n > 0
and-bitwise AND operation, xor-bitwise XOR operation.

Please help her students find out the answer!

Input Format
The first line of input contains a single integer a (1≤a≤103) — the number of input test cases.
For each test case, the only line of input contains one integer m (1≤m≤230).

Constraints
1≤a≤103
1≤m≤230

Output Format
For each test case, print a single integer — the minimum number of n.

Sample Input 0
`
5
1
2
15
122
256
`

Sample Output 0
`
3
3
1
2
257
`

Explanation 0

Note

Test case 1:

1 and 3 = 1 > 0, 1 xor 3 = 2 > 0.

Test case 2:

2 and 3 = 2 > 0, 2 xor 3 = 1 > 0.
