def InfiniteFunc(n, repeater=1):
    if n == 1: 
        return repeater
    n -= 1
    return str(repeater) + r"+\frac{" + str(InfiniteFunc(n, repeater*2)) + "}{" + str(InfiniteFunc(n, repeater*2+1)) + "}" #returned a list of strings in the order required, multiplied the repeater by 2 because i found the pattern it needed for the next output

print(InfiniteFunc(int(input()))) 