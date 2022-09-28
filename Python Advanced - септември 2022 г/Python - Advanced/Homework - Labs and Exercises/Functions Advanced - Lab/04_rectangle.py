def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"
    else:
        def area():
            return f"Rectangle area: {length * width}"

        def perimeter():
            return f"Rectangle perimeter: {length * 2 + width * 2}"

        return area() + '\n' + perimeter()
