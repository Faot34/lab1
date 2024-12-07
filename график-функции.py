def graph_function():
    height = 9
    width = 9
    for y in range(height, 0, -1):
        line = f'{y:>2} |'
        for x in range(1, width + 1):
            if y == x:
                line += ' * '
            else:
                line += '   '
        print(line)
    print('   ' + '-' * (4 * width))
    print('     ' + ''.join([f'{x:>3}' for x in range(1, width + 1)]))

graph_function()
