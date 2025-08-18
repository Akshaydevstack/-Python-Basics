def smaile_gen():
    yield 1
    yield 2
    
gen=smaile_gen()

print(next(gen))

print(next(gen))