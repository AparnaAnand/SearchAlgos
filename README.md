# SearchAlgos
Implements BFS, DFS and UCS search algorithms

Input should be in the following format:

<#cases> total number of test cases in file
<task> algorithm that you are supposed to use for this case 'BFS','DFS' or 'UCS'
<source> name of the source node
<destinations> names of the destination nodes (space separated)
<middle nodes> names of the middle nodes (space separated)
<#pipes> represents the number of pipes
<graph> represents start-end nodes, length, #off-times and off-time range of pipes (space separated)
<start-time> the time when water will start flowing through the pipes

eg:
1
BFS
A
B C D
E F G H I
5
A B 12 0
A E 3 3 2-4 1-5 9-10 1-15
E H 2 1 1-2
H D 5 2 5-6 2-3
I C 6 1 10-14
3

Output will be in the following format:

<destination pipe> <time>

eg:
B 4

NOTE: BFS and DFS don't consider lengths and off-times. Length is taken to be 1 by default.
