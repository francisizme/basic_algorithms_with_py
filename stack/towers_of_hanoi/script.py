#!/usr/bin/env python3
from stack.script import Stack

print("\nLet's play Towers of Hanoi!!")
# init towers
stacks = []
left_stack = Stack(name='Left')
middle_stack = Stack(name='Middle')
right_stack = Stack(name='Right')

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

# setup game
num_disk = int(input("\nHow many disks do you want to play with?\n"))
# will fun with at least 3
while num_disk < 3:
    num_disk = int(input("Enter a number greater than or equal to 3\n"))
for i in range(num_disk, 0, -1):
    left_stack.push(i)
num_optimal_moves = 2 ** num_disk - 1
print(f"\nThe fastest you can solve this game is in {num_optimal_moves} moves")


# get user input
def get_input():
    choices = [stack.get_name()[0] for stack in stacks]
    while True:
        len_stacks = len(stacks)
        for stack_index in range(len_stacks):
            name = stacks[stack_index].get_name()
            letter = choices[stack_index]
            print(f"Enter {letter} for {name}.")
        user_input = input('')
        if user_input in choices:
            for stack_index in range(len_stacks):
                if user_input == choices[i]:
                    return stacks[i]


# play game
num_user_moves = 0
while right_stack.get_size() != num_disk:
    print("\n\n\n...Current Stacks...")
    for stack in stacks:
        stack.print_items()
    while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()
        if from_stack.is_empty():
            print("\n\nInvalid Move. Try Again")
        elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        else:
            print("\n\nInvalid Move. Try Again")
print(f"\n\nYou completed the game in {num_user_moves} moves, and the optimal number of moves is {num_optimal_moves}")
