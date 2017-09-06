
"""
* * * *
 * * * *
* * * *
 * * * *
* * * *
 * * * *
* * * *
 * * * *
"""
for row in range(0,8):
    rowprint = ""
    for spaces in range(0,4):
        if row%2 > 0:
            rowprint += " "
            rowprint += "*"
        else:
            rowprint += "*"
            rowprint += " "
    print rowprint