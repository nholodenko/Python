# def salary(hours, rate_per_hour, bonus):
#     result = hours*rate_per_hour+bonus
#     return result
#
# print(salary(hours=180, rate_per_hour=300, bonus=10000))

from sys import argv

script_name, hours, rate_per_hour, bonus = argv

result = int(hours) * int(rate_per_hour) + int(bonus)

print(result)
