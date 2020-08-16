number_of_lines = int(input())
lines = [input() for lines in range(number_of_lines)]
winners = [winner[:-4] for winner in lines if 'win' in winner]
print(winners)
print(len(winners))
