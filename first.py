print('Earned amount:')
bubblegum = 202
print(f'Bubblegum: ${bubblegum}')
toffee = 118
print(f'Toffee: ${toffee}')
ice = 2250
print(f'Ice cream: ${ice}')
chocolate = 1680
print(f'Milk chocolate: ${chocolate}')
doughnut = 1075
print(f'Doughnut: ${doughnut}')
pancake = 80
print(f'Pancake: ${pancake}')
print()
income = bubblegum + toffee + ice + chocolate + doughnut + pancake
print(f'Income: ${income}')
print('Staff expenses:')
staff = int(input())
print('Other expenses:')
other = int(input())
expenses = staff + other
net = income - expenses
print(f'Net income: ${net}')
