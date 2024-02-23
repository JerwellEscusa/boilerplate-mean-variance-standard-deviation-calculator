import numpy as np

def calculate(list):
    total = len(list) # Storing length for the if condition and for the formula
    if total <9 | total >9:
        raise ValueError("List must contain nine numbers.")
    else:
        a = np.array(list) # Convert list to array
        a = np.reshape(a, (3,3)) # Reshape into a 3 by 3 matrix
        shape = np.array(a.shape) # Record dimensions for extracting n value
        axis_0 = shape[0] # Count rows 
        axis_1 = shape[1] # Count columns
        axis0_sum = np.sum(a, axis=0) # Sum for each column
        axis1_sum = np.sum(a, axis=1) # Sum for each row
        list_sum = np.sum(list) # Sum for the list
        axis0_mean = axis0_sum/axis_0 # Mean for each column
        axis1_mean = axis1_sum/axis_1 # Mean for each row
        list_mean = list_sum/total # Mean for the list
        axis0_var = np.sum(((a - axis0_mean)**2), axis=0)/axis_0 # Variance for each column
        axis1_var = np.sum(((a - np.reshape(axis1_mean, (3,1)))**2), axis=1)/axis_1 # Variance for each row
        list_var = (np.sum((list - list_mean)**2))/total # Variance for the list
        axis0_std = axis0_var**0.5 # Standard deviation for each column
        axis1_std = axis1_var**0.5 # Standard deviation for each row
        list_std = list_var**0.5 # Standard deviation for the list
        axis0_max = np.max(a, axis=0) # Max for each column
        axis1_max = np.max(a, axis=1) # Max for each row
        list_max = np.max(list) # Max for the list
        axis0_min = np.min(a, axis=0) # Min for each column
        axis1_min = np.min(a, axis=1) # Min for each row
        list_min = np.min(list) # Min for the list
        mean_list = [axis0_mean.tolist(), axis1_mean.tolist(), list_mean.tolist()] # Compiling mean to a list
        var_list = [axis0_var.tolist(), axis1_var.tolist(), list_var.tolist()] # Compiling variance to a list
        std_list = [axis0_std.tolist(), axis1_std.tolist(), list_std.tolist()] # Compiling standard deviation to a list
        max_list = [axis0_max.tolist(), axis1_max.tolist(), list_max.tolist()] # Compiling max to a list
        min_list = [axis0_min.tolist(), axis1_min.tolist(), list_min.tolist()] # Compiling min to a list
        sum_list = [axis0_sum.tolist(), axis1_sum.tolist(), list_sum.tolist()] # Compiling sum to a list
        calculations = {} # Creating an empty dictionary to enter each list
        calculations['mean'] = mean_list
        calculations['variance'] = var_list
        calculations['standard deviation'] = std_list
        calculations['max'] = max_list
        calculations['min'] = min_list
        calculations['sum'] = sum_list
        return calculations