

def foo(a,b):
    a = 'new'
    b = 42
    return a, b

def bar(a):
    a[0] = 'new'
    a[1] = a[1] + 1

def edit_duplicate(data):
    copied_list = data.copy()
    copied_list[0] = 100
    return copied_list



if __name__ == '__main__':
    print("Welcome. Testing...")
    # 1. returning a tuple of the results
    a = 'old'
    b = 0
    a,b = foo(a,b)

    assert(a=='new')
    assert(b==42)
    # 2. Global variables are not recommended 

    # 3. passing a mutable (changable in-place) object
    # lists and dictonaries are mutable
    # numbers, strings and tuples are immutable
    args = ['old', 99]
    bar(args)
    assert(args[0]=='new')
    assert(args[1]==100)


    # pass a mutable object and make a shallow copy.
    a = [1,2]
    print(a)
    dup = edit_duplicate(a)
    print(a)
    print(dup)

