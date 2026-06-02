def get_starting_number():
    num = 0
    while num <= 0:
        inp = input("How many bottles of beer on the wall? ")
        if inp.isdigit():
            num = int(inp)
    return num
    
def sing(num_bottles):
    down = 0
    while(down < num_bottles):
        wall = num_bottles - down
        wall2 = wall-1
        if wall != 1 and wall!=2:
            print(f"{wall} bottles of beer on the wall, {wall} bottles of beer.\nTake one down, pass it around, {wall2} bottles of beer on the wall.")
        elif wall == 2:
            print(f"{wall} bottles of beer on the wall, {wall} bottles of beer.\nTake one down, pass it around, {wall2} bottle of beer on the wall.")
        elif wall == 1:
            print(f"{wall} bottle of beer on the wall, {wall} bottle of beer.\nTake it down, pass it around, no more bottles of beer on the wall!")
        down+=1