def square_root_bisection(square_target: float, tolerance: float = 1e-7, max_iterations: int = 100) -> float:
    """
    Calculate the square root of a given number using the bisection method.
    Parameters:
    square_target (float): The number to find the square root of. Must be non-negative.
    tolerance (float, optional): The tolerance for the approximation. Default is 1e-7.
    max_iterations (int, optional): The maximum number of iterations to perform. Default is 100.
    Returns:
    float: The approximate square root of the square_target.
    Raises:
    ValueError: If square_target is negative.
    """
    # Implementation of the bisection method to find the square root
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        low = 0
        high = max(1, square_target)
        root = None
        
        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid**2

            if abs(square_mid - square_target) < tolerance:
                root = mid
                break

            elif square_mid < square_target:
                low = mid
            else:
                high = mid

        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
    
        else:   
            print(f'The square root of {square_target} is approximately {root}')
    
    return root

N = 36
square_root_bisection(N)