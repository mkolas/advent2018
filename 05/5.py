import copy

input_string = ""
used_letters = list()
letter_scores = dict()


def reduce(char_list):
    while True:
        original = copy.copy(char_list)
        x = 0
        while x < len(char_list)-1:
            window = char_list[x:x + 2]
            if window[0] != window[1] and window[0].upper() == window[1].upper():
                if window[0].upper() not in used_letters:
                    used_letters.append(window[0].upper())
                char_list.pop(x)
                char_list.pop(x)
            else:
                x += 1
        if original == char_list:
            break

    return char_list


with open("input1.txt") as file:
    for row in file:
        input_string = row.strip()

# part 1
print(len(''.join(reduce([x for x in input_string]))))

# part 2
for letter in used_letters:
    # print("running letter {}".format(letter))
    letterless_string = input_string.replace(letter, '').replace(letter.lower(), '')
    letter_scores[letter] = len(''.join(reduce([x for x in letterless_string])))
    # print("letter score = {}".format(letter_scores[letter]))

# print(letter_scores)
print(min(letter_scores, key=letter_scores.get))




