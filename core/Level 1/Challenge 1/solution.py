import pickle

infile = open("data.pkl","rb")
new_dict = pickle.load(infile)
print(new_dict)
infile.close()