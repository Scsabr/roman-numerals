global lookup
lookup = {
    "I": 1,
    "V": 5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}

def splitter(roman):
    splitted = []
    
    start = 0
    end = 0

    while True:
        while lookup[roman[start]] <= lookup[roman[end]] and end<len(roman)-1:
            end += 1

        if roman[start:end] and end < len(roman)-1:
            splitted.append(roman[start:end])
        else:
            splitted.append(roman[start:])
            break
        start = end
        end = start
    # maybe this works??

    return splitted

def seg_validator(segment):
    # different errors are:
    #     more than 3 reps
    #     using anything other than ICX as a subtractive
    for i in range(len(segment)):
        reps = 0
        for j in range(i, len(segment)):
            if segment[j] == segment[i]:
                reps += 1
            else:
                break
        
        if segment[i] in ["V","L","D"] and reps > 1:
            return False
        
        if reps > 3:
            return False
    return True

def subtractive(seg):
    # checks if it's a subtractive?
    '''
    And how do we check?
    WELL
    if the seg len == 2
    and
    the value of the first is < 2nd
    and it's one of the permitted ones
    '''
    if len(seg) != 2:
        return False
    
    if lookup[seg[0]] >= lookup[seg[1]]:
        return False
    
    if seg not in ["IV","IX","XL","XC","CD", "CM"]:
        raise ValueError(f"Invalid subtractor: {seg}")
    
    return True
        
def evaluator(seg):
    value = 0
    if subtractive(seg):
        value = lookup[seg[1]]-lookup[seg[0]]
    else:
        for each in seg:
            value += lookup[each]
    return value

def roman_to_decimal(roman):
    for each in roman:
        try:
            lookup[each]
        except:
            raise ValueError(f"Invalid character {each}")

    seggies = splitter(roman)
    # print(seggies)
    total = 0
    for seg in seggies:
        if not seg_validator(seg):
            raise ValueError("Invalid repetition")
        total += evaluator(seg)
    # print(f"{roman} = {total}")
    return total


if __name__ == "__main__":
    roman_to_decimal("XC")
    roman_to_decimal("XI")
    roman_to_decimal("MMXXVII")
    roman_to_decimal("MCMXCII")
    roman_to_decimal("DCLXVI")
    roman_to_decimal("IX")
    roman_to_decimal("XCIX")
