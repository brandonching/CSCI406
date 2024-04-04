import sys
import random
import time


def timber_recursive(log_sizes):
    # Base Case
    if len(log_sizes) == 1:
        return log_sizes[0]

    # Recursive Case
    return sum(log_sizes) - min(timber_recursive(log_sizes[1:]),
                                timber_recursive(log_sizes[:-1]))


def command_line_input():
    # Get the first argument as the input file
    input_file = sys.argv[1]

    # read the input file
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # close the file
    f.close()

    # Get the sizes of the logs from the second line
    log_sizes = list(map(int, lines[1].split()))

    print(timber_recursive(log_sizes))


def synthetic_test():
    # Test all log sizes from 1 to 20. Use a random number generator to generate the log sizes
    # Log files to an output file
    with open("output.csv", "w") as f:
        for i in range(1, 21):
            print("Testing log size: ", i)
            # test each size 100 times
            for _ in range(100):
                log_sizes = [random.randint(1, 1001) for _ in range(i)]
                # Get the start time of the algorithm
                start_time = time.time()
                # Run the algorithm
                timber_recursive(log_sizes)
                # Get the end time of the algorithm
                end_time = time.time()
                # Calculate the time taken in milliseconds
                time_taken = (end_time - start_time) * 1000
                # Write the results to the output file
                f.write(f"{i}, {timber_recursive(log_sizes)}, {time_taken}\n")

    f.close()


if __name__ == "__main__":
    synthetic_test()
