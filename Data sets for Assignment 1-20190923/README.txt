These data files contain Kessel Run problem instance descriptions.  

a_easy.txt
b_moderate.txt
c_hard.txt
d_veryhard.txt
e_puremadness.txt

The file names are indicative of the average difficulty of problems in the files themselves.  Here, the measure of difficulty is the expected depth of the optimal solution, but as the problems are randomly generated (by randomly choosing rotations for a given starting position), some problem instances may be less difficult than the average for the data set.

There are 20 problem instances for most of the files, and 21 instances for data set d_veryhard.txt.

The data files consist of one problem per line. Each line will have the following format: 􏰀 􏰁
i m n a0 a1 a2 a3 ... b0 b1 b2 b3 ...

The first number is the problem index, so you can more easily compare results. The next two values on the line indicate the number of rows (m) and the number of columns (n), followed by exactly the right number of integers for two arrays. The arrays are linearized in row-major order, meaning that the first n integers are the first row, the second n integers are the second row, etc.  All of the data on the line will be separated by spaces, and there may be an extra space between the two arrays, just for human readability. 

