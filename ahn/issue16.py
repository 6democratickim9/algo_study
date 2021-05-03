def solution():
    bowls = input()
    len = 0
    prev = "";
    for i, bowl in enumerate(bowls):
      if i == 0:
        len = len + 10
      else:
        if prev == bowl:
          len = len + 5
        else:
          len = len + 10
      prev = bowl
  
    return len

print(solution())