from itertools import accumulate, count, islice

def running_mean(sequence):
    cumulative_sum = list(accumulate(sequence))  #use accumulate from itertools to calculate cumulative sum from sequence
    #because accumulate returns an iterator; list converts it to a list 
    running_means = [round(cumulative_sum[i] / (i + 1), 2) for i in range(len(sequence))]
    #use a list comprehension; For each index i, we calculate the running mean by dividing the cumulative sum at index i (from cumulative_sum) by i + 1 since index starts at zero.
    #round function rounds the result to two decimal places, 
    #calculated means are stored in running means list


    return running_means

