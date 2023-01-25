# Ron's IQ

> https://www.hackerrank.com/contests/ieee-sbm-wie-codathon-23/challenges/rons-iq

---

Harry is playing a game made up by Ron inorder to check his IQ. The rules are simple, Ron will give a list of numbers to him along with a word and he has to find if he could make that word from the given list. If he is able to make the word then he should say yes otherwise no. Procedure that Harry has to follow:-

While the list is not empty:

He needs to choose any number x from the list a, and any letter of the English alphabet y. Then he will replace all occurrences of number x with the letter y. For example, if Ron made the list as a=[2,3,4,4,1,5], then he could transform it in the following way:

Choose the number 2 and the letter m. After that a=[m,3,4,4,1,5]. Choose the number 3 and the letter u. After that a=[m,u,4,4,1,5]. Choose the number 4 and the letter g. After that a=[m,u,g,g,1,5]. Choose the number 1 and the letter l. After that a=[m,u,g,g,l,5]. Choose the number 5 and the letter e. After that a=[m,u,g,g,l,e]. After the transformation all letters are united into a string, in our example we get the string "muggle".

Having the list a and the string s, help Harry to check his IQ by giving output as YES or NO.

Input Format
The first line contains a single integer t — the number of test cases.
Then the description of the test cases follows.
The first line of each test case contains a single integer n — the length of the array a and the string s.
The second line of each test case contains exactly n integers: a1,a2,…,an — the elements of the array a.
The third line of each test case contains a string s of length n, consisting of lowercase English letters.

Constraints
(1≤t≤103)
(1≤n≤50)
(1≤ai≤50)

Output Format
For each test case, output "YES", if we can get the string s from the array a, and "NO" otherwise. You can output each letter in any case.

Sample Input 0
`
7
1
22
g
2
26 26
gg
2
22 22
ua
2
29 47
xx
2
25 25
zh
3
17 17 17
bbb
3
32 32 32
pph
`

Sample Output 0
`
YES
YES
NO
YES
NO
YES
NO
`
