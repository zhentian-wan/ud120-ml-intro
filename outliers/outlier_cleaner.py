#!/usr/bin/python
import math

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []
    total = int(len(predictions)*0.9)

    ### your code goes here
    for i in range(len(predictions)):
        tuple = (ages[i][0], net_worths[i][0], math.fabs(predictions[i][0] - net_worths[i][0]))
        cleaned_data.append(tuple)

    cleaned_data.sort(key=error_aesc_sort)

    return cleaned_data[:total]

def error_aesc_sort(e):
    return e[2]