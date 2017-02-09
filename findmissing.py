def find_missing(temp1, temp2):
  if len(temp1)==len(temp2):
    return [0]
  
  elif len(temp1)==len(temp2)==[0]:
   return [0]
   
  else:
    result = set(temp1) ^ set(temp2)
    result = list(result)
    return result[0]