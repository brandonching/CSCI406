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
    # Prefix sum of the log sizes
    sums = [0] * n
    for i in range(n):
        sums[i] = log_sizes[i] + (sums[i - 1] if i > 0 else 0)

    # Create a table to store the results and fill in the base case (i == j)
    table = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        table[i][i] = log_sizes[i]

    # Fill in the table using the bottom-up approach (traverse diagonally)
    for diag in range(1, n):
        for i in range(n - diag):
            j = i + diag
            table[i][j] = sums[j] - (sums[i - 1] if i > 0 else 0) - \
                min(table[i + 1][j], table[i][j - 1])

    return table[0][n - 1]


def timber_bottom_up_traverse(log_sizes):
    '''
    This function solves the timber problem using a bottom-up approach
    :param log_sizes: A list of log sizes
    :return: The maximum value that can be obtained from cutting the logs
    '''
    n = len(log_sizes)
    # Prefix sum of the log sizes
    sums = [0] * n
    for i in range(n):
        sums[i] = log_sizes[i] + (sums[i - 1] if i > 0 else 0)

    # Create a table to store the results and fill in the base case (i == j)
    table = [[0 for _ in range(n)] for _ in range(n)]
    parent_table = [[(0, 0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        table[i][i] = log_sizes[i]
        parent_table[i][i] = (i, i)

    # Fill in the table using the bottom-up approach (traverse diagonally)
    for diag in range(1, n):
        for i in range(n - diag):
            j = i + diag
            table[i][j] = sums[j] - (sums[i - 1] if i > 0 else 0) - \
                min(table[i + 1][j], table[i][j - 1])
            if (table[i + 1][j] == table[i][j - 1]):
                parent_table[i][j] = (i+1, j)
            elif (table[i + 1][j] < table[i][j - 1]):
                parent_table[i][j] = (i + 1, j)
            else:
                parent_table[i][j] = (i, j-1)

    print(table[0][n - 1])

    # Traverse the table to get the logs that were cut
    # start in the top right corner

    # Print out the traversal, start in the top right corner
    next_i = 0
    next_j = n - 1
    next_log = parent_table[next_i][next_j]
    for log in range(n):
        # if the next log points to the same log, we are done
        if next_log == (next_i, next_j):
            print(next_i + 1, end=" ")

        # if the next log points to the log below
        elif next_log[0] == next_i + 1:
            print(next_i + 1, end=" ")
            next_i = next_log[0]
            next_log = parent_table[next_i][next_j]

        # if the next log points to the log to the left
        elif next_log[1] == next_j - 1:
            print(next_j + 1, end=" ")
            next_j = next_log[1]
            next_log = parent_table[next_i][next_j]

    print()


def command_line_input():
    '''
    This function reads the input file from the command line and runs 
    the timber_bottom_up function
    :return: None
    '''
    # Get the first argument as the input file
    input_file = sys.argv[1]

    # Read the input file
    with open(input_file, 'r') as f:
        lines = f.readlines()
    f.close()

    # Get the sizes of the logs from the second line and run the algorithm
    log_sizes = list(map(int, lines[1].split()))
    timber_bottom_up_traverse(log_sizes)


def synthetic_test(max_size=20, test_count=100):
    '''
    This function runs a synthetic test on the timber_recursive function
    The results are written to an output file
    :param range: The range of log sizes to test from 1 to range (default is 20)
    :return: None
    '''
    with open("output_recursive.csv", "w") as f:
        for i in range(1, max_size + 1):
            print("Testing log size: ", i)
            total_time = 0
            for _ in range(test_count):
                # Use a random number generator to generate the log sizes
                log_sizes = [random.randint(1, 1001) for _ in range(i)]
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
    The results are written to an output file
    :param range: The range of log sizes to test (default is 2000)
    :return: None
    '''
    with open("output_bottom_up.csv", "w") as f:
        for i in range(10, max_size + 1, 10):
            print("Testing log size: ", i)
            total_time = 0
            for _ in range(test_count):
                # Use a random number generator to generate the log sizes
                log_sizes = [random.randint(1, 1001) for _ in range(i)]
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
