import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pickle

data = pickle.load( open( "plot_data.pickle", "rb" ), encoding='latin1' )

embeddings = data['embeddings']
years = data['years']
ids = data['ids']

x = embeddings[:, 0]
y = embeddings[:, 1]

def onpick(event):
    global subfig,ax_list
    ax_list[1].clear()
    ind = event.ind[0] # event.ind returns list -> take first element
    img = mpimg.imread('picasso/' + str(ids[ind]) + '.jpg')
    ax_list[1].imshow(img)    
    plt.draw()
    print(ind, years[ind], ids[ind])

N = 4
area = np.ones(N)*50

subfig, ax_list = plt.subplots(1,2)

pid = subfig.canvas.mpl_connect('pick_event', onpick)
scatter = ax_list[0].scatter(x, y, s=area, c=years, cmap="hot", alpha=0.5, picker=True)

subfig.subplots_adjust(left=0.25)
cbar_ax = subfig.add_axes([0.05, 0.15, 0.05, 0.7])
subfig.colorbar(scatter, cax=cbar_ax)

plt.show()
subfig.canvas.mpl_disconnect(pid)