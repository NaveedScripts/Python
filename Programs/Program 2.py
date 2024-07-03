legend_list= []
for num in range(100, 1000):
    digit1 = int(num / 100)
    digit2 = int((num / 10) % 10)
    digit3 = int(num % 10)
    if (digit1 < digit2 < digit3):
        legend_list.append(num)
print(legend_list)