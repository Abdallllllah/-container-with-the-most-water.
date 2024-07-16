def the_most_water_container(s):
         p1=0
         p2 = len(s)-1
         mostw = 0
         while p1<p2:
             if s[p1]>s[p2]:
                 mostw = max(mostw,s[p2]*(p2-p1))
                 p2 = p2-1
             else:
                 mostw = max(mostw,s[p1]*(p2-p1))
                 p1=p1+1
         return mostw
height = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,12,3444,50000,49000,50,67,4900,650000000,4567885,566778]
print(the_most_water_container(height))
                 
                 
                 
                 
            
            


