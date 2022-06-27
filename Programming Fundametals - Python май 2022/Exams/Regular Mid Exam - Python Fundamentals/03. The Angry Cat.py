price_ratings = list(map(int, input().split(", ")))
entry_point = int(input())
item_type = input()
price_left = 0
price_right = 0

for left in range(0, entry_point):
    if item_type == "cheap":
        if price_ratings[left] < price_ratings[entry_point]:
            price_left += price_ratings[left]
    if item_type == "expensive":
        if price_ratings[left] >= price_ratings[entry_point]:
            price_left += price_ratings[left]

for right in range(entry_point + 1, len(price_ratings)):
    if item_type == "cheap":
        if price_ratings[right] < price_ratings[entry_point]:
            price_right += price_ratings[right]
    if item_type == "expensive":
        if price_ratings[right] >= price_ratings[entry_point]:
            price_right += price_ratings[right]

if price_left == price_right:
    print(f"Left - {price_left}")
elif price_left > price_right:
    print(f"Left - {price_left}")
elif price_right > price_left:
    print(f"Right - {price_right}")
