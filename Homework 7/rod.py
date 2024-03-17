def rod_bottom_up(n):
    # Create an array to store the results
    W = [0] * (max(n+1,4))
    # Base cases
    W[1] = 1
    W[2] = 2
    W[3] = 4
    # General Case
    for i in range(4, n+1):
        W[i] = W[i-1] + W[i-2] + W[i-3]
    return W[n]


if __name__ == "__main__":
    for n in range(1, 100):
        print("W(", n, ") =", rod_bottom_up(n), sep="")
