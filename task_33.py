i = str(input())
letters = set(list(i))

for letter in letters:
  print(f'Символ {letter} встречается в строке {i} {i.count(letter)} раз')