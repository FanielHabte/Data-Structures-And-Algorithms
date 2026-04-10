def binary(number: int) -> str:
    if number == 0:
        return "0"

    remainder = []
    while number > 0:
        remainder.append(number % 2)
        number = number // 2

    return " ".join(str(remainder[i]) for i in range(len(remainder) - 1, -1, -1))


binaryValue = binary(10)

print(binaryValue)
