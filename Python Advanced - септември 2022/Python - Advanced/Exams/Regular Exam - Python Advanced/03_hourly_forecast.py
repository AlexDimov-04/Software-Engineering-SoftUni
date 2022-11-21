def forecast(*args):
    result = ''
    weather_dict_priority = {'Sunny': [], 'Cloudy': [], 'Rainy': []}

    for elements in args:
        weather_dict_priority[elements[1]].append(elements[0])

    for weather, locations in weather_dict_priority.items():
        locations = sorted(locations)
        for location in locations:
            result += f'{location} - {weather}' + '\n'

    return result
