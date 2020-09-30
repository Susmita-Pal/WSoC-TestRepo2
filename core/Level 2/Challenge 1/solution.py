import pickle
import matplotlib.pyplot as plt
name="data.pkl"
file=open(name,"rb")
data=pickle.load(file)
print(data)
keys=data.keys()
print(keys)
values=data.values()
print(values)
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.bar(data.keys(), data.values())
ax.set_xticklabels(data.keys())
plt.show()
fig = plt.figure(figsize=(10, 10))
plt.pie(data.values(), labels=data.keys())

# show plot
plt.show()
