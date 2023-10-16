from itertools import accumulate, count, islice

def running_mean(sequence):
    cumulative_sum = list(accumulate(sequence))
    running_means = [round(cumulative_sum[i] / (i + 1), 2) for i in range(len(sequence))]

    return running_means

