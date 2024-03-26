def outer(func):
    def inner():
        print('Something is happening before the function')
        func()
        print('Something is happening after the function')
    return inner

def jump():
    print('I am junping')


def swim():
    print('I am swimming')