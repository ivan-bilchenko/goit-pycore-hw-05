"""Module implementing a cached Fibonacci function for optimized performance."""
def caching_fibonacci():
    """Create a Fibonacci function with caching to optimize performance.""" 

    cache = {}

    def fibonacci(n):
        """Calculate the nth Fibonacci number."""       
        # Base cases
        if n <= 0:
            return 0
        if n == 1:
            return 1

        # Return cached result if available
        if n in cache:
            return cache[n]

        # Calculate and cache the result
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]

    return fibonacci


# Create fibonacci function with caching
fib = caching_fibonacci()

# Test the function
print(f"fib(10) = {fib(10)}")
print(f"fib(15) = {fib(15)}")
