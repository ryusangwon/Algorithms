def recursive_function(i):
    print("print", i, "th recursive function")
    if i==100:
        return
    return recursive_function(i+1)
recursive_function(1)