from collections import deque

bullet_price = int(input())
gun_barrel = int(input())
bullets = list(map(int, input().split()))
locks = deque((map(int, input().split())))
intelligence_value = int(input())
shots = 0
gun_remains = gun_barrel

while True:
    gunshot = bullets.pop()
    lock = locks.popleft()

    if gunshot > lock:
        print("Ping!")
        locks.appendleft(lock)
        shots += 1
        gun_remains -= 1
    else:
        print("Bang!")
        shots += 1
        gun_remains -= 1

    if gun_remains == 0 and bullets:
        print("Reloading!")
        gun_remains = gun_barrel

    if (not locks) and (not bullets):
        bullets_cost = shots * bullet_price
        print(f"{len(bullets)} bullets left. Earned ${intelligence_value - bullets_cost}")
        break

    elif not bullets:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        break

    elif not locks:
        bullets_cost = shots * bullet_price
        print(f"{len(bullets)} bullets left. Earned ${intelligence_value - bullets_cost}")
        break
