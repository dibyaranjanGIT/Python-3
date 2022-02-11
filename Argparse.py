# If you ran the .py file with python Argparse.py -h , this will show all the arguments to be passed.
# For arguments if you pass -- then they became optional arguments.
# Command to run "python Arparse.py --n1 20 --n2 12 --op add"

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--number1", "--n1", help="First Number")
    parser.add_argument("--number2", "--n2", help="Second Number")
    parser.add_argument("--operation", "--op", help="Operation",
                        choices=['add', 'sub'])
    args = parser.parse_args()

    result = None
    n1 = int(args.number1)
    n2 = int(args.number2)
    op = args.operation
    print(args.number1)
    print(args.number2)
    print(args.operation)

    if op == 'add':
        result = n1 + n2
        print(f"Result : {result}")
    elif op == 'sub':
        result = n1 - n2
        print(f"Result : {result}")
