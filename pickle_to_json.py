import pickle
import jsonpickle
import numpy as np

data = pickle.load( open( "plot_data.pickle", "rb" ), encoding='latin1' )
x = data['embeddings'][:, 0].tolist()
y = data['embeddings'][:, 1].tolist()
years = data['years']
ids = data['ids']

transformed_data = {'x': x, 'y': y, 'years': years, 'ids': ids}
json_data = jsonpickle.encode(transformed_data)
print("var data = " + json_data)