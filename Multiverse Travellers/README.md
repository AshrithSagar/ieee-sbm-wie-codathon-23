# Multiverse Travellers

> https://www.hackerrank.com/contests/ieee-sbm-wie-codathon-23/challenges/multiverse-travellers

---

Ben and Scarlet are multiverse travellers. While travelling across a m x m dimension universe they need to get to the portal situated at (ax, by).

While they are standing at (cx, dy). But there is a demon guarding the portal at (ex,fx) . Ben and Scarlet have to go from (ax,by) to (cx,dy) without getting caught by the demon.

They get caught by the demon if they are on the same row, column or diagonal as him. They can take only one step along any of the 8 directions adjacent to them (north, south, east, west, north-east, north-west, south-east, south-west).

Find if they can fulfill their mission or not.

Input Format
First line contains the dimensions of the universe , a single integer m
Second line contains two integers location of demon (ex,fy)
Third line contains Ben and Scarlet's location (cx,dy)
Fourth line contains location of portal (ax,by)

It is guaranteed that Ben and Scarlet are currently not in the demon's radar.
Also the demon is not in the same place as Scarlet and Ben.
Furthermore the portal is not in the same place as the demon or Scarlet and Ben and the portal is also not in the demon's radar.

Constraints
3<=m<=1000
1<= ex,fy<=m
1<= cx,dy<=m
1<= cx,by<=m

Output Format
YES, when the mission will be a success if they reach the portal without getting caught by the demon.
NO, when the mission will be unsuccessful if they get caught.

Sample Input 0
`
5
4 4
1 3
3 1
`

Sample Output 0
`YES`

Sample Input 1
`
10
4 4
2 3
1 6
`

Sample Output 1
`NO`
