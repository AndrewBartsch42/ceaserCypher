import random
import string

random.seed()
random_strings = []
random_strings_encoded = []
characters = string.ascii_letters + string.digits
for i in range(50):
    random_strings.append(''.join(random.choice(characters) for i in range(7)))


for i in range (50):
    shift_value = random.randint(1,10)
    LorR = random.randint(1,2)
    right_shifted_characters = characters[-shift_value:] + characters[:-shift_value]
    left_shifted_characters = characters[shift_value:] + characters[:shift_value]
    new_string = random_strings[i]
    if LorR == 1:
        for j in range(7):
            indexOfRSH = right_shifted_characters[characters.index(new_string[j-1])]
            new_string = new_string.replace(new_string[j - 1], indexOfRSH)
    else:
        for j in range(7):
            indexOfLSH = left_shifted_characters[characters.index(new_string[j-1])]
            new_string = new_string.replace(new_string[j - 1], indexOfLSH)
    random_strings_encoded.append(new_string)
    if LorR == 1:
        leftorright = "right"
    else:
        leftorright = "left"
    print("This is the shift value: "  + str(shift_value))
    print("Left or Right: " + leftorright)
    print("This is the old string: " + random_strings[i])
    print("This is the new string: " + new_string)
    print("\n")

