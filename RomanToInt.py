def romanToInt(roman_input):
    roman = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
    resultInteger = 0
    for i in range(0, len(roman_input)-1):
        if roman[roman_input[i]] < roman[roman_input[i+1]]:
            resultInteger -= roman[roman_input[i]]
        else:
            resultInteger += roman[roman_input[i]]
    return resultInteger + roman[roman_input[-1]]
roman = input("Input roman numeral:")
print("Integer equivalent: ",romanToInt(roman))