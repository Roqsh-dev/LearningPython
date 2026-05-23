

def spellBottle(amount):
    if amount == 1:
        return "bottle"
    else:
        return "bottles"
    
for i in range (99):

    amount = 99 - i
    bottle = spellBottle(amount)

    print(f"{amount} {bottle} of beer on the wall, {amount} {bottle} of beer.")

    if amount == 1:
        print("Take it down and pass it around, no more bottles of beer on the wall.")

        print("\nNo more bottles of beer on the wall, no more bottles of beer.")
        print("Go to the store and buy some more, 99 bottles of beer on the wall.")
    else:
        print(f"Take one down and pass it around, {amount - 1} {spellBottle(amount - 1)} of beer on the wall.\n")