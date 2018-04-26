#!/usr/bin/env python
from operator import add


def superStack(stacks):
    newStack = list()
    for stack in stacks:
        stackSplit = stack.split(' ')
        if stackSplit[0] == 'push':
            newStack.append(int(stackSplit[1]))
        elif stackSplit[0] == 'pop':
            newStack.pop(-1)
        elif stackSplit[0] == 'inc':
            incrementCount = int(stackSplit[1])
            increment = int(stackSplit[2])
            incList = list()
            for i in range(incrementCount):
                incList.append(increment)
            len_diff = len(newStack) - len(incList)
            for i in range(len_diff):
                incList.append(0)
            newStack = map(add, newStack, incList)

    return newStack


def main():
    # array input of metals length
    stacks_array = list()
    stacks_count = int(input())

    for i in range(int(stacks_count)):
        n = raw_input()
        stacks_array.append(n)
        # print out the result
    print superStack(stacks_array)


if __name__ == '__main__':
    main()