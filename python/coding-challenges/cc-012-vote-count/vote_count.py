from collections import Counter  
  
votes =["A", "A", "A", "B", "C", "A"]  
  
vote_count=Counter(votes) 
  
max_votes=max(vote_count.values()) 
  
lst=[i for i in vote_count.keys() if vote_count[i]==max_votes] 
  
print(sorted(lst)[0]) 