# file_utils/pickle_utils.py
import pickle

def read_pickle(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)

def write_pickle(file_path, data):
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)
