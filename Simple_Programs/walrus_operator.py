# The walrus operator (:=) allows assignment and return of a value in the same expression.

# will assign iterator + 1 then check the condition
iterator = 0
while (iterator := iterator + 1) < 5:
    print(f"Current iterator value: {iterator}")