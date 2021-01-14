def arithmetic_arranger(problems, show_answers=False):
    all_addend1_str = ''
    all_addend2_str = ''
    all_dash_str = ''
    all_sum_str = ''

    # Greater than 5 problems submitted
    if len(problems) > 5:
        # raise ValueError('Too many problems.')
        return 'Error: Too many problems.'

    # Now loop through list parsing inputs
    for problem in problems:
        # consume parts of problem
        parts = problem.split()
        addend1 = parts[0]
        addend2 = parts[2]
        operator = parts[1]

        # Check operand is + or -
        if operator != '+' and operator != '-':
            # raise ValueError('Operator must be + or - .')
            return 'Error: Operator must be \'+\' or \'-\'.'

        # Make sure addends are max 4 digits
        if len(addend1) > 4 or len(addend2) > 4:
            # raise ValueError('Numbers cannot be more than four digits.')
            return 'Error: Numbers cannot be more than four digits.'

        # Make sure addends are only numbers
        try:
            addend1_int = int(addend1)
            addend2_int = int(addend2)
        except:
            # raise ValueError('Numbers must only contain digits.')
            return 'Error: Numbers must only contain digits.'

        # inputs are valid, now lets format
        max_addend_len = max(len(addend1), len(addend2))
        addend1 = addend1.rjust(max_addend_len+2)
        addend2 = f'{operator} {addend2.rjust(max_addend_len)}'
        dash_str = "-" * len(addend2)
        sum_str = addend1_int + addend2_int if operator == '+' else addend1_int - addend2_int

        all_addend1_str = all_addend1_str + addend1 + '    '
        all_addend2_str = all_addend2_str + addend2 + '    '
        all_dash_str = all_dash_str + dash_str + '    '
        all_sum_str = all_sum_str + \
            str(sum_str).rjust(max_addend_len+2) + '    '

    return f'{all_addend1_str.rstrip()}\n{all_addend2_str.rstrip()}\n{all_dash_str.rstrip()}' if show_answers == False else f'{all_addend1_str.rstrip()}\n{all_addend2_str.rstrip()}\n{all_dash_str.rstrip()}\n{all_sum_str.rstrip()}'
