def FormattedNumber(strArr):
  count = 0
  startcount = "false" 
  if strArr.count(".") > 1:
    return "false"
  for c in reversed(strArr):
    if c == ".":
      startcount = True 
      count = 0
    elif  c == "," and startcount:
      if count % 3 != 0:
        return "false"
    elif c == "," and not startcount:
      return "false"
    elif startcount:
      count += 1
  return "true"

print(FormattedNumber("0.232567"))
print(FormattedNumber("1,093,222.04"))
print(FormattedNumber("1,093,22.04"))
print(FormattedNumber("0.232567"))

print(FormattedNumber(",093,222.04"))
print(FormattedNumber("2,567.00.2"))
print(FormattedNumber("12321,213.213213"))