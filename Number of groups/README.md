# Number of groups

> https://www.hackerrank.com/contests/ieee-sbm-wie-codathon-23/challenges/number-of-groups-1-1

---

Given 3 integers a,b and c where a,b,c are all positive (>0), find the number of groupings (a,b) such that

`(a * lcm (x,y)) - (b * hcf(x,y)) = c`
where lcm(x,y) is the least common multiple of x and y and hcf(x,y) is the highest common factor of x and y.

Input Format
First line has one integer t indicating the number of testcases (1≤t≤104).
Next t lines contain 3 integers each - a,b,c (1≤a,b and c≤107)

Constraints
Integer t, 1≤t≤104
Integer a, 1≤a≤107
Integer b, 1≤b107
Integer c, 1≤c107

Output Format
Print the number of groupings (x,y) which satisfy the given equation for each of the test cases.

Sample Input 0
`
2
5 58 9
3 63 5
`

Sample Output 0
`
0
0
`

Sample Input 1
`
4
1 1 3
4 2 6
3 3 7
2 7 25
`

Sample Output 1
`
4
3
0
8
`
