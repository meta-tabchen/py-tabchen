import pickle
import json

def save_pickle(data, path):
    with open(path, "wb") as f:
        pickle.dump(data, f)

def load_pickle(path):
    with open(path,'rb') as f:
        data = pickle.load(f)
    return data

def save_json(data, path):
    with open(path, "wb") as f:
        json.dump(data,path)

def load_json(path):
    with open(path,'rb') as f:
        data = json.load(f)
    return data

def io_hello():
    print("Hello from io!")