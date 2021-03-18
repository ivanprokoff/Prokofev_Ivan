class Error(Exception):
    pass


class EmptyInstructionError(Error):
    pass


class WrongPathError(Error):
    pass


def rabbits_hole(*args, start_point=(0, 0),
                 eliminate_direction=''):
    x = start_point[0]
    y = start_point[1]
    if len(args) == 0:
        raise EmptyInstructionError('No instructions')
    for i in args:
        if eliminate_direction.isalpha() or eliminate_direction == '':
            pass
            if i[0] != eliminate_direction:
                if i[0] == 'north':
                    y += i[1]
                elif i[0] == 'south':
                    y -= i[1]
                elif i[0] == 'east':
                    x += i[1]
                elif i[0] == 'west':
                    x -= i[1]
        else:
            raise TypeError('Not available value')
    if x == start_point[0] and y == start_point[1]:
        raise WrongPathError('This is a wrong place')
    else:
        return (x, y)
