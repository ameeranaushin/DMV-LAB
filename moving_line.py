import matplotlib.pyplot as graph
print("Line graph generator")

numbers= input("enter values separated by space:")
values=[]
for item in numbers.split():
    values.append(float(item))

    positions=list(range(1,len(values)+1))

    graph.plot(positions,values,marker='o')

    graph.title("Line graph of user data")
    graph.xlabel("Data position")
    graph.ylabel("Entered values")
    graph.grid()
    graph.show