def get_starting_number():
    num = 0
    while num <= 0:
        inp = input("How many bottles of beer on the wall? ")
        if inp.isdigit():
            num = int(inp)
    return num
        
def sing(num_bottles):
    bottles = True
    num = num_bottles
    while(bottles):
        num2 = num - 1
        if num != 1 and num!=2:
            print(f"{num} bottles of beer on the wall, {num} bottles of beer.\nTake one down, pass it around, {num2} bottles of beer on the wall.")
        elif num == 2:
            print(f"{num} bottles of beer on the wall, {num} bottles of beer.\nTake one down, pass it around, {num2} bottle of beer on the wall.")
        elif num == 1:
            print(f"{num} bottle of beer on the wall, {num} bottle of beer.\nTake it down, pass it around, no more bottles of beer on the wall!")
        num+=-1
        if num == 0:
            bottles = False
