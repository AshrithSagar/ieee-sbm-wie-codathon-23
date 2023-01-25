# Loids Watch

> https://www.hackerrank.com/contests/ieee-sbm-wie-codathon-23/challenges/loids-time

---

A long time ago, in a galaxy far, far away, Loid had a 24-hour clock. The clock had been given to him by the Grand Oracle, and it showed time in the format "HH:MM". He loved the clock so much that he looked at it every x minutes, and the clock is currently showing time s.

Beginning from time s, if Loid looks at the clock every x minutes, how many different palindromes will Loid see, the first time being at time s?

A palindrome is a sequence that reads the same from backward and forward. For example 12:21 is a palinfrome but 20:57 is not.

Input Format
The first line of the input should have an integer a, where (1≤a≤100) - the number of test cases. The test cases have to be provided with the following descriptions.

Each test case should be given in its own line of input, and should contain a string s of length 5 with the format "HH:MM", where 00 ≤ HH ≤ 23 and 00 ≤ MM ≤ 59, and another integer b, where (1≤b≤1440) — the number of minutes Loid takes to look again at the clock.

Constraints
00 ≤ HH ≤ 23
00 ≤ MM ≤ 59.

Output Format
The program should output a single integer for each test case, which would be the number of different palindromes seen by Loid if he looks at the clock every x minutes, starting from time s.

Sample Input 0
`
10
05:17 516
03:42 1088
10:47 1114
21:01 954
09:54 999
00:47 846
13:15 511
15:51 712
07:04 332
04:42 17
`

Sample Output 0
`
1
2
6
1
1
0
16
2
5
16
`