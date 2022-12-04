import re

data_file = "sample.txt"
data_file = "data.txt"

with open(data_file) as f:
    lines = f.read().splitlines()

    count = 0
    for l in lines:
        assigns = re.search("(\d*)-(\d*),(\d*)-(\d*)", l)
        first1, first2 = int(assigns.group(1)), int(assigns.group(2))
        second1, second2 = int(assigns.group(3)), int(assigns.group(4))
        if (
            (first1 <= second1 and first2 >= second1)
            or (first1 <= second2 and first2 >= second2)
            or (second1 <= first1 and second2 >= first1)
            or (second1 <= first2 and second2 >= first2)
        ):
            count += 1
    print(count)
