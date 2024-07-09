def safe_divide(numerator, denominator):
  numerator = int(numerator)
  denominator = int (denominator)  
  if denominator == 0:
    raise ZeroDivisionError("Division by zero is not allowed")
  return numerator / denominator