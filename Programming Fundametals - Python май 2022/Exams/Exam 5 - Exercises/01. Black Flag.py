days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
total_plunder = 0

for day in range(1, days + 1):
    total_plunder += daily_plunder

    if day % 3 == 0:
        additional_plunder = daily_plunder * 0.5
        total_plunder += additional_plunder
    if day % 5 == 0:
        warship = total_plunder * 0.3
        total_plunder -= warship

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {total_plunder / expected_plunder * 100:.2f}% of the plunder.")
