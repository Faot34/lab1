def percentage_chart_simple(filename):
    with open(filename, 'r') as file:
        numbers = [float(line.strip()) for line in file]

    even_positions = [numbers[i] for i in range(1, len(numbers), 2)]  # 2nd, 4th, etc.
    odd_positions = [numbers[i] for i in range(0, len(numbers), 2)]   # 1st, 3rd, etc.

    avg_even = sum(abs(num) for num in even_positions) / len(even_positions)
    avg_odd = sum(abs(num) for num in odd_positions) / len(odd_positions)

    total = avg_even + avg_odd
    even_percentage = avg_even / total * 100
    odd_percentage = avg_odd / total * 100

    print(f"Even positions: {even_percentage:.1f}%")
    print(f"Odd positions:  {odd_percentage:.1f}%")
    print(f"Chart:")
    print(f"Even: {'#' * int(even_percentage // 5)}")
    print(f"Odd:  {'#' * int(odd_percentage // 5)}")

percentage_chart_simple('sequence.txt')
