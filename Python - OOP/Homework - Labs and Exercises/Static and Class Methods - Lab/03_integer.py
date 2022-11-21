from math import floor


class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not type(float_value) == float:
            return "value is not a float"
        return cls(floor(float_value))

    @classmethod
    def convert_to_decimal(cls, num):
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i, c in enumerate(num):
            if (i + 1) == len(num) or roman_numerals[c] >= roman_numerals[num[i + 1]]:
                result += roman_numerals[c]
            else:
                result -= roman_numerals[c]
        return result

    @classmethod
    def from_roman(cls, num):
        result = Integer.convert_to_decimal(num)
        return cls(result)

    @staticmethod
    def from_string(num):
        if str(num).isdigit():
            return Integer(int(num))
        else:
            return "wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))

