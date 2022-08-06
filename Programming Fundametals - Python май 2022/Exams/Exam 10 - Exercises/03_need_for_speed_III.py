def create_cars(cars, number):
    for _ in range(number):
        data = input().split('|')
        car_name = data[0]
        mileage = int(data[1])
        fuel = int(data[2])

        cars[car_name] = {'mileage': mileage, 'fuel': fuel}

    return cars


def addition_data(cars):

    while True:
        command = input().split(' : ')
        if command[0] == "Stop":
            break

        elif command[0] == "Drive":
            car_name = command[1]
            distance = int(command[2])
            fuel = int(command[3])
            if cars[car_name]['fuel'] < fuel:
                print("Not enough fuel to make that ride")
            else:
                cars[car_name]['mileage'] += distance
                cars[car_name]['fuel'] -= fuel
                print(f"{car_name} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[car_name]['mileage'] >= 100000:
                del cars[car_name]
                print(f"Time to sell the {car_name}!")

        elif command[0] == "Refuel":
            car_name = command[1]
            fuel = int(command[2])
            if cars[car_name]['fuel'] + fuel > 75:
                fuel = 75 - cars[car_name]['fuel']
                cars[car_name]['fuel'] = 75
            else:
                cars[car_name]['fuel'] += fuel
            print(f"{car_name} refueled with {fuel} liters")

        elif command[0] == "Revert":
            car_name = command[1]
            kilometers = int(command[2])
            cars[car_name]['mileage'] -= kilometers
            if cars[car_name]['mileage'] < 10000:
                cars[car_name]['mileage'] = 10000
                continue
            print(f"{car_name} mileage decreased by {kilometers} kilometers")

    return cars


def final_result(cars):
    for element in cars:
        print(f"{element} -> Mileage: {cars[element]['mileage']} kms, Fuel in the tank: {cars[element]['fuel']} lt.")


def need_for_speed(number):
    cars = {}

    create_cars(cars, number)
    addition_data(cars)
    final_result(cars)


n = int(input())
need_for_speed(n)
