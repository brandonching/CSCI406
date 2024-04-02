import sys
import random


def timber_recursive(log_sizes):
    # Base Case
    if len(log_sizes) == 1:
        return log_sizes[0]

    total_length = sum(log_sizes)

    # Recursive Case
    return total_length - min(timber_recursive(log_sizes[1:]), timber_recursive(log_sizes[:-1]))


def command_line_input():
    # Get the first argument as the input file
    input_file = sys.argv[1]

    # read the input file
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # close the file
    f.close()

    # Get the number of logs from the first line
    logs = int(lines[0])

    # Get the sizes of the logs from the second line
    log_sizes = list(map(int, lines[1].split()))

    print(timber_recursive(log_sizes))


def synthetic_test():
    # Test all log sizes from 1 to 20. Use a random number generator to generate the log sizes
    for i in range(1, 21):
        log_sizes = [random.randint(1, 1001) for _ in range(i)]
        print(i, ":", timber_recursive(log_sizes))


if __name__ == "__main__":
    command_line_input()
