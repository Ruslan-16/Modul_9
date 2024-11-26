first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_strings if len(x) >= 5]
print(first_result)

second_result = [(first, second)  for first in first_strings for second in second_strings if len(first) == len(second)]
print(second_result)

third_result = { n: len(n)  for n in first_strings + second_strings if len(n) % 2 == 0 }
print(third_result)