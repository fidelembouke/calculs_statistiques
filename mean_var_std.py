import numpy as np

def calculate(list):
    
    if(len(my_list)!=9):
        raise ValueError("List must contain nine numbers.")
        
    #Transformation liste en matrice 3*3
    # print("List regerenated in 3*3 matrix: ")
    matrix = np.array(my_list).reshape(3,3)
       
    #Calcul des moyennes
    mean_columns = np.mean(matrix, axis=0)
    mean_lines = np.mean(matrix, axis=1)
    mean_flattened = np.mean(matrix)

    #Calcul variances
    var_columns = np.var(matrix, axis=0)
    var_lines = np.var(matrix, axis=1)
    var_flattened = np.var(matrix)

     # Calcul des écarts-types
    std_columns = np.std(matrix, axis=0)
    std_lines = np.std(matrix, axis=1)
    std_flattened = np.std(matrix)

    # Calcul des maximums
    max_columns = np.max(matrix, axis=0)
    max_lines = np.max(matrix, axis=1)
    max_flattened = np.max(matrix)

    # Calcul des minimums
    min_columns = np.min(matrix, axis=0)
    min_lines = np.min(matrix, axis=1)
    min_flattened = np.min(matrix)

    # Calcul des sommes
    sum_columns = np.sum(matrix, axis=0)
    sum_lines = np.sum(matrix, axis=1)
    sum_flattened = np.sum(matrix)

    calculations = {
        "mean":[mean_columns.tolist(), mean_lines.tolist(), mean_flattened],
        "variance": [var_columns.tolist(), var_lines.tolist(), var_flattened],
        "standard deviation": [std_columns.tolist(), std_lines.tolist(), std_flattened],
        "max": [max_columns.tolist(), max_lines.tolist(), max_flattened],
        "min": [min_columns.tolist(), min_lines.tolist(), min_flattened],
        "sum": [sum_columns.tolist(), sum_lines.tolist(), sum_flattened]
     }

        
    return calculations




