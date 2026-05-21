

Solution = {
    "chickens": 0,
    "rabbits": 0
}

# i are chickens (we can have 47 chickens at max because 94 / 2 = 47)
for i in range(47 + 1):
    legsLeft = 94 - (2 * i)

    if legsLeft % 4 == 0:
        if (i + (legsLeft / 4)) == 35:
            Solution["chickens"] = i
            Solution["rabbits"] = int(legsLeft / 4)
            break


print(f"There are {Solution['chickens']} Chickens and {Solution['rabbits']} Rabbits!")