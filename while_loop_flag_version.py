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
    keep_looping = True
    while keep_looping:
        if n > 2:
            print(f"{n} bottles of beer on the wall, {n} bottles of beer.")
            print(f"Take one down, pass it around, {n - 1} bottles of beer on the wall.\n")
        elif n == 2:
            print(f"{n} bottles of beer on the wall, {n} bottles of beer.")
            print(f"Take one down, pass it around, {n - 1} bottle of beer on the wall.\n")
        elif n == 1:
            print(f"{n} bottle of beer on the wall, {n} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
            keep_looping = False
        n -= 1
        if n <= 0:
            keep_looping = False

if __name__ == "__main__":
    num_bottles = get_starting_number()
    sing(num_bottles)