"""
Given the following array of values, print out all the elements in reverse order, with each element on a new line.
For example, given the list
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
Your output should be
0
1
2
3
4
5
6
7
8
9
10
You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.
"""

# input: array of values
# output: reversed array, printed one element per line


def reverse_print(array):
    # reverse the array
    array.reverse()
    # loop through the array
    for item in array:
        # print each item
        print(item)


array_a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
reverse_print(array_a)

new_list = array_a[::-1]
print(new_list)
