from calculate import mul
import py_compile # efficient bcz it will not create binary file each time if it is latest

def write():
    print("Hello world")
def main():
    write()
    mul()
    py_compile.compile('writing.py')
main()

