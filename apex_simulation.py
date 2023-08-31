from tournament import Tournament


tournament = Tournament()
tournament.simulate_multiple_tournaments(n=500)

print("""                 
     /\                    
    /  \   _ __   _____  __
   / /\ \ | '_ \ / _ \ \/ /
  / ____ \| |_) |  __/>  < 
 /_/    \_\ .__/ \___/_/\_\
          | |              
          |_|    
                
""")
      
try:
    for i,j in enumerate(tournament.top5_winners()):
        print(f"{i+1} Lugar: {j[0]} con {j[1]} victorias.")
except:
    print(tournament.top5_winners())
