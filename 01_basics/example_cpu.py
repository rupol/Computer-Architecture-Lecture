import sys

#  operation (OP) codes
#  things our computer can do
#  our computer is 8 bit, so we can only write 256 OP codes
PRINT_HELLO_WORLD = 1  # 0b00000001
HALT = 2  # 0b00000010
PRINT_NUM = 3   # 0b00000011
SAVE_REG = 4   # 0b00000100
PRINT_REG = 5   # 0b00000101
ADD = 6    # 0b00000110

memory = [
    # hard code a program
    SAVE_REG,
    420,  # value 420
    1,  # register 1
    SAVE_REG,
    246,  # value 246
    2,  # register 2
    ADD,
    1,
    2,
    PRINT_REG,
    1,
    HALT,
]

registers = [0] * 8

running = True

pc = 0

while running:
    # read line by line from memory
    instruction = memory[pc]

    if instruction == PRINT_HELLO_WORLD:
        # print Hello World
        # move the PC up 1 to the next instruction
        print('Hello World')
        pc += 1

    elif instruction == PRINT_NUM:
        # print the number in the next memory slot
        num = memory[pc + 1]
        print(num)
        pc += 2  # skip over the next line (this is just our num)

    elif instruction == SAVE_REG:
        # save some value to some register
        # first number after instruction will be the value to store
        # second number after instruction will be register
        num = memory[pc + 1]
        reg_location = memory[pc + 2]
        registers[reg_location] = num
        pc += 3

    elif instruction == PRINT_REG:
        #  number after instruction will be register to print
        reg_location = memory[pc + 1]
        print(registers[reg_location])
        pc += 2

    elif instruction == ADD:
        # takes two registers, adds their values, and stores the result in the first register given
        #  get register 1
        reg_1 = memory[pc + 1]
        #  get register 2
        reg_2 = memory[pc + 2]
        #  add the values
        #  store in register 1
        registers[reg_1] += registers[reg_2]
        pc += 3

    elif instruction == HALT:
        running = False
        pc += 1
        # could have also returned

    else:
        print(f'Unknown instruction {instruction}')
        sys.exit(1)  # says program exited uncleanly (crashed)
