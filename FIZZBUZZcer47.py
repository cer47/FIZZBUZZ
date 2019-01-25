for FIZZBUZZ in range(101):
    if FIZZBUZZ % 3 == 0 and FIZZBUZZ % 5 == 0:
        print("FIZZBUZZ")
    elif FIZZBUZZ % 3 == 0:
        print("FIZZ")
        continue
    elif FIZZBUZZ % 5 == 0:
        print("BUZZ")
        continue
    print(FIZZBUZZ)
