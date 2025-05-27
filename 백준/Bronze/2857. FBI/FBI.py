agents = []
for _ in range(5):
    agent = input()
    agents.append(agent)
    
count = 0
for i in range(len(agents)):
    if "FBI" in agents[i]:
        count += 1
        print(i+1, end= " ")
    
if count == 0:
    print("HE GOT AWAY!")

       
            