
def char_count(input: str) -> dict:
    output = {}
    for i in input:
        output[i] = output.get(i, 0) + 1
    print(output)
input = "hello"
char_count(input)