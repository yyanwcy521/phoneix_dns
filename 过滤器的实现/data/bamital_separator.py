bamital_a = open("bamital_a.txt", "w")
bamital_b = open("bamital_b.txt", "w")
bamital_c = open("bamital_c.txt", "w")

with open("bamital.txt") as f:
    for line in f:
        length = len(line.rstrip('\n'))
        if length == 37 or length == 36:
            bamital_a.write(line)
        elif length == 15 or length == 17 or length == 16:
            bamital_c.write(line)
        else:
            bamital_b.write(line)

bamital_a.close()
bamital_b.close()
bamital_c.close()