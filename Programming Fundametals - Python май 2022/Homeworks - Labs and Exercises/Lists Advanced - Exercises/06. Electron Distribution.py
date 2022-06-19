number = int(input())
position_of_shell = 0
distribution_el = []

while number > 0:
    position_of_shell += 1
    shell = 2 * position_of_shell ** 2

    if number >= shell:
        distribution_el.append(shell)
        number -= shell
    else:
        distribution_el.append(number)
        break

print(distribution_el)
