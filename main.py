import re



def validator(line):
    validation_pattern = r'''
                        ^
                        (
                        (\(*)
                        (\-?)
                        (\(*)
                        (\-?)
                        (0|[1-9]\d*)(\.\d*)?
                        (\)*)
                        ([+\-\/\*]{1})
                        )+
                        (\(*)
                        (\-?)
                        (0|[1-9]\d*)(\.\d*)?
                        (\)*)
                        $
                         '''
    isValid = False
    if line.count('(') == line.count(')'):
        if re.fullmatch(validation_pattern, line, re.VERBOSE):
            isValid = True
    return isValid


def calculation(line):
    if isValid:
        res = eval(line)
    else:
        res = None
    return res


if __name__ == '__main__':
    line = str(input())
    isValid = validator(line)
    res = calculation(line)
    if res != None:
        print(res)
    else:
        print('Syntax Error')
