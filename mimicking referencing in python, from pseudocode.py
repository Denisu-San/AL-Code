#using subroutines to mimic referencing in pseudocode

def ManipulatingValues(a, b):
    a += 2
    b += 10
    return a,b

#example of usage

x = 5
y = 7

x, y = ManipulatingValues(x, y)
print(f"Modified x: {x}, Modified y: {y}")