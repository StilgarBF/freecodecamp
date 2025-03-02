"""
Tower of Hanoi is a classic puzzle game involving three rods and a number of disks of different sizes.
The objective of the game is to move all the disks from the source rod to the target rod, following these rules:
1. Only one disk can be moved at a time.
2. Each move consists of taking the top disk from one of the rods and placing it on top of another rod.
3. No disk may be placed on top of a smaller disk.

This script solves the Tower of Hanoi problem for a given number of disks and displays the state of the towers after each move.
"""

NUMBER_OF_DISKS = 3
A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

def display_towers(A: list[int], B: list[int], C: list[int]) -> None:
    """
    Display the current state of the towers in the Tower of Hanoi game.

    Args:
        A (list): The list representing the first tower.
        B (list): The list representing the second tower.
        C (list): The list representing the third tower.

    The function prints the towers vertically, with the top of the towers at the top of the output.
    Each tower is represented by a column, and disks are represented by their values.
    If a position in a tower is empty, it is represented by the '|' character.
    """
    max_height = NUMBER_OF_DISKS
    for i in range(max_height - 1, -1, -1):
        print(
            f"{A[i] if i < len(A) else '|'} "
            f"{B[i] if i < len(B) else '|'} "
            f"{C[i] if i < len(C) else '|'}"
        )
    print('\n')

def move(n: int, source: list[int], auxiliary: list[int], target: list[int]) -> None:
    """
    Solve the Tower of Hanoi problem by moving n disks from the source rod to the target rod using an auxiliary rod.
    Parameters:
    n (int): The number of disks to move.
    source (list): The rod from which disks are moved initially.
    auxiliary (list): The rod used as an auxiliary for moving disks.
    target (list): The rod to which disks are moved finally.
    Returns:
    None
    The function uses recursion to move disks between rods and displays the progress after each move.
    """
    
    if n <= 0:
        return
    # move n - 1 disks from source to auxiliary, so they are out of the way
    move(n - 1, source, target, auxiliary)
    
    # move the nth disk from source to target
    target.append(source.pop())

    # display our progress
    display_towers(A, B, C)
    
    # move the n - 1 disks that we left on auxiliary onto target
    move(n - 1,  auxiliary, source, target)
              
# initiate call from source A to target C with auxiliary B
# display starting towers
display_towers(A, B, C)
move(NUMBER_OF_DISKS, A, B, C)