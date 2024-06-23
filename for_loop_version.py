def get_starting_number():
    while True:
        try:
            n = int(input("How many bottles of beer on the wall? "))
            if n >= 1:
                return n
            else:
                print("Please enter an integer 1 or greater.")
        except ValueError:
            print("Please enter a valid integer.")

def sing(n):
    for i in range(n, 0, -1):
        if i > 2:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down, pass it around, {i - 1} bottles of beer on the wall.\n")
        elif i == 2:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down, pass it around, {i - 1} bottle of beer on the wall.\n")
        elif i == 1:
            print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")

if __name__ == "__main__":
    num_bottles = get_starting_number()
    sing(num_bottles)