input_string = ""
used_letters = list()
letter_scores = dict()

def reduce(string):
    i = 0
    while i < len(string)-1:
        window = string[i:i + 2]
        if window[0] != window[1] and window[0].upper() == window[1].upper():
            if window[0].upper() not in used_letters:
                used_letters.append(window[0].upper())
            string.pop(i)
            string.pop(i)
            i = 0
        else:
            i += 1

    return string


with open("input1.txt") as file:
    for row in file:
        input_string = row.strip()

# part 1
print(len(''.join(reduce([x for x in input_string]))))

# part 2
for letter in used_letters:
    print("running letter {}".format(letter))
    letterless_string = input_string.replace(letter, '').replace(letter.lower(), '')
    letter_scores[letter] = len(''.join(reduce([x for x in letterless_string])))
    print("letter score = {}".format(letter_scores[letter]))

print(letter_scores)
print(min(letter_scores, key=letter_scores.get))




