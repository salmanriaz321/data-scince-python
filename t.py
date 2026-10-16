RS = int(input("Enater number of red shirts: "))
BS = int(input("Enater number of blue shirts: "))
WS = int(input("Enater number of whight  shirts: "))

total = RS+BS+WS

prob_a = BS/total
prob_b = RS/total

prob_bga = prob_b
prob_a_and_b = prob_a*prob_b

print("Probability that the second shirt is red given tht the first shirt is blue: ")
print(round((prob_bga), 3))

print("Probability that the second shirt is red and the first shirt is blue: ")
print(round((prob_a_and_b), 3))
