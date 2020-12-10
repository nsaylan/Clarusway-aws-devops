
votes =["A", "A", "A", "B", "C", "A"]  
  
num_first_vote = 0
num_second_vote = 0
num_third_vote = 0
for v in votes:
    if v == "A":
        num_first_vote += 1
    elif v == "B":
        num_second_vote += 1
    else:
        num_third_vote += 1

if num_first_vote > num_second_vote and num_first_vote > num_third_vote:
    print ("A")
elif num_second_vote > num_first_vote and num_second_vote > num_third_vote:
    print ("B")
else:
    print ("C")
