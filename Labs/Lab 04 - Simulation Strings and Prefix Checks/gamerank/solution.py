def solution():
  history = input().strip()
  rank = 25
  streak = 0
  stars = 0
  
  for game in history:
    if game == 'W':
      streak += 1
      if streak >= 3 and rank >= 6:
        stars += 2
      else:
        stars += 1
    else:
      streak = 0
      if rank > 20:
        continue
      elif rank == 20:
        if stars > 0:
          stars -= 1
        continue
      
      stars -= 1
      if stars < 0:
        rank +=1
        if rank > 20:
          stars = 1
        elif rank > 15:
          stars = 2
        elif rank > 10:
          stars = 3
        else:
          stars = 4
        continue
    
        #BUG: if inc rank and its above the thresh hold, need to set it +1
    if game == 'W' and rank > 20:
      if stars > 2:
        rank -= 1
        stars = stars - 2
        # if streak >=3:
        #   stars = 2
        # else:
        #   stars = 1
    elif rank > 15:
      if stars > 3:
        rank -= 1
        stars = stars - 3
        # if streak >=3:
        #   stars = 2
        # else:
        #   stars = 1
    elif rank > 10:
      
      if stars > 4:
        rank -= 1
        stars = stars - 4
        # if streak >=3:
        #   stars = 2
        # else:
        #   stars = 1
    elif rank > 0:
      
      if stars > 5:
        if rank == 1:
          print("Legend")
          return
        else:
          rank -= 1
          stars = stars - 5
          # if streak >=3:
          #   stars = 2
          # else:
          #   stars = 1
  
  print(rank)
  
solution()
