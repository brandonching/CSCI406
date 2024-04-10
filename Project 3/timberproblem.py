import sys
import random
import time


def timber_recursive(log_sizes):
    '''
    This function solves the timber problem using a recursive approach
    :param log_sizes: A list of log sizes
    :return: The maximum value that can be obtained from cutting the logs
    '''
    # Base Case
    if len(log_sizes) == 1:
        return log_sizes[0]

    # Recursive Case
    return sum(log_sizes) - min(timber_recursive(log_sizes[1:]),
                                timber_recursive(log_sizes[:-1]))


def timber_bottom_up(log_sizes):
    '''
    This function solves the timber problem using a bottom-up approach
    :param log_sizes: A list of log sizes
    :return: The maximum value that can be obtained from cutting the logs
    '''
    n = len(log_sizes)
    # Create a table to store the sum of the legnth of all the logs from 1 to j for each index
    sums = [0] * n
    for i in range(n):
        sums[i] = log_sizes[i] + (sums[i - 1] if i > 0 else 0)

    # Create a table to store the results
    table = [[0 for _ in range(n)] for _ in range(n)]

    # Fill in the base case (i.e. when i == j the value is the length of the log)
    for i in range(n):
        table[i][i] = log_sizes[i]

    # Fill in the table
    for diag in range(1, n):
        for i in range(n - diag):
            j = i + diag
            table[i][j] = sums[j] - (sums[i - 1] if i > 0 else 0) - \
                min(table[i + 1][j], table[i][j - 1])

    return table[0][n - 1]


def command_line_input():
    '''
    This function reads the input file from the command line and runs the timber_recursive function
    :return: None
    '''
    # Get the first argument as the input file
    input_file = sys.argv[1]

    # read the input file
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # close the file
    f.close()

    # Get the sizes of the logs from the second line
    log_sizes = list(map(int, lines[1].split()))

    print(timber_bottom_up(log_sizes))


def synthetic_test(max_size=20, test_count=100):
    '''
    This function runs a synthetic test on the timber_recursive function
    :param range: The range of log sizes to test from 1 to range (default is 20)
    :return: None
    '''
    # Test all log sizes from 1 to 20. Use a random number generator to generate the log sizes
    # Log files to an output file
    with open("output_recursive.csv", "w") as f:
        for i in range(1, max_size + 1):
            print("Testing log size: ", i)
            total_time = 0
            for _ in range(test_count):
                log_sizes = [random.randint(1, 1001) for _ in range(i)]

                # Test the recursive approach
                # Get the start time of the algorithm
                start_time = time.time()
                # Run the algorithm
                timber_recursive(log_sizes)
                # Get the end time of the algorithm
                end_time = time.time()
                # Calculate the time taken in milliseconds
                total_time += (end_time - start_time) * 1000

            # Write the results to the output file
            f.write(f"{i}, {total_time / test_count}\n")

    f.close()


def synthetic_test_bottom_up(max_size=2000, test_count=100):
    '''
    This function runs a synthetic test on the timber_bottom_up function
    :param range: The range of log sizes to test from 1 to range (default is 2000)
    :return: None
    '''
    # Test all log sizes from 1 to 2000. Use a random number generator to generate the log sizes
    # Log files to an output file
    with open("output_bottom_up.csv", "w") as f:
        for i in range(1, max_size + 1):
            print("Testing log size: ", i)
            total_time = 0
            for _ in range(test_count):
                log_sizes = [random.randint(1, 1001) for _ in range(i)]

                # Test the bottom-up approach
                # Get the start time of the algorithm
                start_time = time.time()
                # Run the algorithm
                timber_bottom_up(log_sizes)
                # Get the end time of the algorithm
                end_time = time.time()
                # Calculate the time taken in milliseconds
                total_time += (end_time - start_time) * 1000

            # Write the results to the output file
            f.write(f"{i}, {total_time / test_count}\n")

    f.close()


def validate_methods():
    '''
    This function validates the timber_recursive and timber_bottom_up functions
    :return: None
    '''
    # Test random log lengths (1-20) and random log sizes (1-1000) for 1000 iterations
    for _ in range(1000):
        if _ % 100 == 0:
            print(f"Testing iteration: {_}")
        log_sizes = [random.randint(1, 1001)
                     for _ in range(random.randint(1, 21))]
        # print if the results are not the same
        if timber_recursive(log_sizes) != timber_bottom_up(log_sizes):
            print("Results are not the same")
            print(log_sizes)
            print(timber_recursive(log_sizes))
            print(timber_bottom_up(log_sizes))
            return


if __name__ == "__main__":
    # Uncomment the line below to run the command line input
    command_line_input()  # This one is used for grading
    # synthetic_test()
    # synthetic_test_bottom_up()
    # validate_methods()
