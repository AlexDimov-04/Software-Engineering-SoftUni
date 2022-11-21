def operate(numbers: list, command: str):
    if command == "negative":
        result = [x for x in numbers if x < 0]
    elif command == "positive":
        result = [x for x in numbers if x > 0]

    return sum(result)


nums = list(map(int, input().split()))
pos_value = operate(nums, command='positive')
neg_value = operate(nums, command='negative')

print(neg_value)
print(pos_value)
if abs(neg_value) > pos_value:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
