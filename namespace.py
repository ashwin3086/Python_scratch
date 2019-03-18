

## Basically a new way of importing modules
## but we have to use namespace which is sqrt_module.<functionname>

## ADvantage of this is now I can have a separate square function in this program
import sqrt_module
print(sqrt_module.square(9))

def square(i):
    return i*i
print("From main program")
print(square (20))