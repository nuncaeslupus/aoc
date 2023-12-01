from timeit import default_timer as timer

data_file = "sample2.txt"
data_file = "data.txt"

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def convert_text_to_numbers(text: str) -> str:
    new_text = ""
    for i in range(len(text)):
        if text[i].isdigit():
            new_text += text[i]
        else:
            for text_num in numbers:
                if text[i:].startswith(text_num):
                    new_text += numbers[text_num]
    return new_text


start = timer()
with open(data_file, "r") as f:
    result: list[int] = []
    for l in f:
        l = convert_text_to_numbers(l)
        result.append(int(l[0]) * 10 + int(l[-1]))
    print(f"Result: {sum(result)}")

end = timer()
print(f"Total time: {end - start:.5f} seconds.")
