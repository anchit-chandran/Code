import pickle

data = {
    "a": 1,
    "b": 2,
    "c": 3,
}

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

with open('data.pickle','rb') as f:
    loaded_data = pickle.load(f)

print(loaded_data)