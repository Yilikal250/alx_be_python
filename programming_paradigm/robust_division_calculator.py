def safe_divide(numerator, denominator):
  numerator = int(numerator)
  denominator = int (denominator)  
  try:
    return numerator / denominator 
  except ZeroDivisionError as e:
    return e
  