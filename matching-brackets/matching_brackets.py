
def is_paired(input_string):
    bracket = ""
    for char in input_string:
        if char == '{' or char == '(' or char == '[':
            bracket += char

        elif len(bracket) > 0 and (char == '}' and bracket[-1] == '{' or 
        char == ')' and bracket[-1] == '(' or char == ']' and bracket[-1] == '['):
            bracket = bracket[:-1]
        elif char == '}' or char == ')' or char == ']':
            return False
        
    if len(bracket) == 0:
        return True
    else:
        return False

