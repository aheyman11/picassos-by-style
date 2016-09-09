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

def onclick(event):
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          (event.button, event.x, event.y, event.xdata, event.ydata))
    global subfig,ax_list
    img2 = mpimg.imread('picasso/391.jpg')
    ax_list[1].imshow(img2)    
    plt.draw()

def onmotion(event):
    pass #print ('motion event')

def onpick(event):
    global subfig,ax_list
    ax_list[1].clear()
    ind = event.ind[0]
    img2 = mpimg.imread('picasso/' + str(ids[ind]) + '.jpg')
    ax_list[1].imshow(img2)    
    plt.draw()
    print(ind, years[ind], ids[ind])

img=mpimg.imread('picasso/466.jpg')

N = 4
colors = np.random.rand(N)
area = np.ones(N)*50

subfig, ax_list = plt.subplots(1,2)

#cid = subfig.canvas.mpl_connect('button_press_event', onclick)
pid = subfig.canvas.mpl_connect('pick_event', onpick)
cidmotion = subfig.canvas.mpl_connect('motion_notify_event', onmotion)
scatter = ax_list[0].scatter(x, y, s=area, c=years, alpha=0.5, picker=True)
ax_list[1].imshow(img)

subfig.subplots_adjust(left=0.25)
cbar_ax = subfig.add_axes([0.05, 0.15, 0.05, 0.7])
subfig.colorbar(scatter, cax=cbar_ax)

plt.show()
#subfig.canvas.mpl_disconnect(cid)
subfig.canvas.mpl_disconnect(pid)
subfig.canvas.mpl_disconnect(cidmotion)