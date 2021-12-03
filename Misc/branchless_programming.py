# Branching is when the flow of the program is split into two parts based on a
# runtime condition check. Branchless programming is a programming technique
# that eliminates the branches (if, switch, and other conditional statements)
# from the program. In certain situations this approach might get the code to
# run faster


def smaller(a, b):
    ''' Compare two values and return the smaller one using <if> statement
        (using branches) '''
    
    if a < b:
        return a

    else:
        return b


def smaller_branchless(a, b):
    ''' Compare two values and return the smaller one without using <if>
        statement (without using branches) '''

    # For example, if   a = 1, b = 2,
    # then   a < b --> True,
    # so   a * (a < b) --> a * True --> a * 1 --> a
    
    return a * (a < b) + b * (b <= a)


def to_upper(chars):
    ''' Convert a list of ASCII characters to upper case using <if> statement
        (using branches) '''

    for i in range(len(chars)):
        if (chars[i] >= 'a') and (chars[i] <= 'z'):
            chars[i] = chr(ord(chars[i]) - 32)


def to_upper_branchless(chars):
    ''' Convert a list of ASCII characters to upper case without using <if>
        statement (without using branches) '''

    for i in range(len(chars)):
        chars[i] = chr(ord(chars[i]) - (32 * ((chars[i] >= 'a') and (chars[i] <= 'z'))))



if __name__ == '__main__':
    import dis

    dis.dis(smaller)
    print('\n', '- ' * 40, '\n')
    
    dis.dis(smaller_branchless)
    print('\n', '- ' * 40, '\n')

    str1 = list('tHiS IS a test')
    str2 = list('this  IS  a  @#$%  ??')

    to_upper_branchless(str1)
    to_upper_branchless(str2)
    
    print(''.join(str1))
    print(''.join(str2))
