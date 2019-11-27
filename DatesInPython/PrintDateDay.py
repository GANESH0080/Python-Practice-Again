import datetime

l = datetime.datetime.now()
print("Todays date is :" ,l)

print(l.day)
print(l.strftime("%a"))  # a is used for printing abbreviated name of day.
print(l.strftime("%A"))  # A is used for printing the day
print(l.strftime("%w"))  # W is used for printing day number in week
print(l.strftime("%Z"))

print('hour:', l.hour)
print('Minutes:', l.minute)
print('Seconds:', l.second)
print('Microsecond:', l.microsecond)