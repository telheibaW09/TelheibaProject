# Function to add two polynomials
def add_polynomials(poly1, poly2):
    # Determine the degree of the larger polynomial
    max_len = max(len(poly1), len(poly2))
    
    # Extend both polynomials to the same length (by padding with 0s)
    poly1.extend([0] * (max_len - len(poly1)))
    poly2.extend([0] * (max_len - len(poly2)))
    
    # Add corresponding coefficients
    result = [poly1[i] + poly2[i] for i in range(max_len)]
    
    return result

# Function to print polynomial in a readable format
def print_polynomial(poly):
    terms = []
    degree = len(poly) - 1
    for i, coeff in enumerate(poly):
        if coeff != 0:
            if degree - i == 0:
                terms.append(f"{coeff}")
            elif degree - i == 1:
                terms.append(f"{coeff}x")
            else:
                terms.append(f"{coeff}x^{degree - i}")
    
    return " + ".join(terms) if terms else "0"

# Example usage
poly1 = [1, 0, -4, 3]  # 1x^3 + 0x^2 - 4x + 3
poly2 = [2, -1, 3]     # 2x^2 - x + 3

result = add_polynomials(poly1, poly2)

# Print result
print(f"Polynomial 1: {print_polynomial(poly1)}")
print(f"Polynomial 2: {print_polynomial(poly2)}")
print(f"Result of addition: {print_polynomial(result)}")
