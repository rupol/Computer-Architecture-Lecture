4 # STORE PRINT_1
20 # location of PRINT_1
0 # into reg 0
4 # STORE PRINT_2 
15 # location of PRINT_2
1 # into reg 1
4 # STORE PRINT_3
12 # location of PRINT_3
2 # into reg 2
9 # CALL print_one
0 # stored in reg 0
2 # HALT
3 # PRINT_NUM - print_three coroutine
3 # the number to print
10 # RET
3 # PRINT_NUM - print_two coroutine
2 # the number to print
9 # CALL PRINT_THREE
2 # stored in reg 2
10 # RET
3 # PRINT_NUM - print_one coroutine
1 # the number to print
9 # CALL PRINT_TWO
1 # stored in reg 1
10 # RET
