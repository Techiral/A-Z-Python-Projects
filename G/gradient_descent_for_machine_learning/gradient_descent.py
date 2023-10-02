import numpy as np #Numpy is implemented for the usage of arrays and mathematical functions

def gradient_descent(x, y):
    m_current = b_current = 0
    iterations = 1000 #The number of iterations can be changed but it is recommended to keep it between 1000 and 10000
    n = len(x)
    learning_rate = 0.01350  #The learning rate can be changed but it is recommended to keep it between 0.01 and 0.001

    for i in range(iterations):
        y_pred = m_current * x + b_current
        cost = (1 / (2 * n)) * sum((y_pred - y) ** 2) #The cost function is the mean squared error function which is more efficient than the mean absolute error function
        
        # Calculate the gradients
        md = -(1 / n) * sum(x * (y - y_pred)) #The partial derivative of the cost function with respect to m
        bd = -(1 / n) * sum(y - y_pred) #The partial derivative of the cost function with respect to b
        
        # Update the coefficients using gradient descent
        m_current -= learning_rate * md #The learning rate is multiplied by the partial derivative of the cost function with respect to m
        b_current -= learning_rate * bd #The learning rate is multiplied by the partial derivative of the cost function with respect to b
        
        print(f"Iteration {i + 1}: m = {m_current}, b = {b_current}, cost = {cost}") #Print the values of m, b and the cost function for each iteration

    return m_current, b_current #Return the final values of m and b

# Example usage:
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

final_m, final_b = gradient_descent(x, y)
print(f"Final slope (m): {final_m}")
print(f"Final intercept (b): {final_b}")
