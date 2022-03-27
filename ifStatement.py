is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a tall man")

elif is_male and not(is_tall):
    print("You are not a tall man")

elif not(is_male) and is_tall:
    print("You are tall but not male")

else:
    print("You are neither male nor tall")