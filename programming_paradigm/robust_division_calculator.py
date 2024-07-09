def safe_divide(x, y):
  x = int(x)
  y= int (y)  
  if y == 0:
    raise ZeroDivisionError("Division by zero is not allowed")
  return x / y