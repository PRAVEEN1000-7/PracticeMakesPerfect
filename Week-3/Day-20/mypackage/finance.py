def simple_interest(principal, rate, time):
    """Calculate Simple Interest. Formula: (P * R * T) / 100"""
    return (principal * rate * time) / 100


def compound_interest(principal, rate, time, n):
    """Calculate Compound Interest.Formula: A = P * (1 + R/(100*n))^(n*T), CI = A - P"""
    amount = principal * (1 + (rate / (100 * n)))**(n * time)
    return amount - principal


