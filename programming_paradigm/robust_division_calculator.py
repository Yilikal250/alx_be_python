def safe_divide(numerator, denominator):
  numerator = float(numerator)
  denominator = float(denominator)  
  try:
    return numerator / denominator 
  except ZeroDivisionError:
    return "Error: Cannot divide by zero."
  