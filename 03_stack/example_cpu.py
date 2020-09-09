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
PUSH = 7
POP = 8

memory = [0] * 256

registers = [0] * 8
SP = 7

running = True

pc = 0

# get file name from command line arguments
if len(sys.argv) != 2:
    print('Usage: example_cpu.py filename')
    sys.exit(1)


def load_memory(filename):
    address = 0
    # open a file and load into memory
    try:
        with open(filename) as f:
            for line in f:
                # split the current line on the # symbol
                split_line = line.split('#')
                # removes whitespace and new lines
                code_value = split_line[0].strip()
                # make sure the value before the # is not empty
                if code_value == '':
                    continue

                num = int(code_value)
                memory[address] = num
                address += 1
    # if file doesn't exist
    except FileNotFoundError:
        print(f'{filename} file not found')
        sys.exit(2)


load_memory(sys.argv[1])
# set the top of the stack correctly
registers[SP] = len(memory)

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
        print(memory[-20:])
        print(registers)

    elif instruction == PUSH:
        given_register = memory[pc + 1]
        value_in_register = registers[given_register]
        # decrement the Stack Pointer
        registers[SP] -= 1
        # write the value of the given register to memory AT the SP location
        memory[registers[SP]] = value_in_register
        pc += 2

    elif instruction == POP:
        given_register = memory[pc + 1]
        # write the value in memory at the top of stack to the given register
        value_from_memory = memory[registers[SP]]
        registers[given_register] = value_from_memory
        # increment the Stack Pointer
        registers[SP] += 1
        pc += 2

    else:
        print(f'Unknown instruction {instruction}')
        sys.exit(1)  # says program exited uncleanly (crashed)
