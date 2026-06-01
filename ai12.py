P = input("Enter truth value for P (True/False): ").strip().capitalize() == "True"
Q = input("Enter truth value for Q (True/False): ").strip().capitalize() == "True"
and_result = P and Q                 
or_result = P or Q                  
not_p = not P                     
implication = (not P) or Q           
biconditional = P == Q              
print("\nLogical Operations Results:")
print("P AND Q :", and_result)
print("P OR Q  :", or_result)
print("NOT P   :", not_p)
print("P → Q   :", implication)
print("P ↔ Q   :", biconditional)

    