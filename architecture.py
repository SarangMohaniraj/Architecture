from matplotlib import pyplot as plt

class Architecture:

  def __init__(self,shape=[4,5,3,5],figsize=None,xkcd=False):
    self.shape = shape;
    self.fig = plt.figure(figsize=figsize)
    ax=self.fig.add_axes([0,0,1,1]) #position: left, bottom, width, height
    ax.set_axis_off()
    self.figsize = figsize if figsize != None else self.fig.get_size_inches() # width,height
    self.radius = self.get_radius()
    self.horizontal_scale = 1

    # self.distance_between_layers = round(self.get_distance_between_layers()+1)
    
    
    # self.radius_neuron = plt.figure()
    plt.xkcd() if xkcd else None
  """
  def get_distance_between_layers(self):
    # return self.figsize[0]/len(self.shape)"""
    # return max(self.shape)**2/2

  def get_radius(self):
    return (self.figsize[1]+self.figsize[0])/max(self.shape)/8

  def draw(self):
    for x in range(len(self.shape)):
      # each layer has to have a different margin from bottom
      margin = (max(self.shape)-self.shape[x])*0.5 #may need to fix this for smaller sizes(radius)
      
      for y in range(self.shape[x]):
        circle = plt.Circle((x*self.horizontal_scale, y+margin), radius=self.radius, fill=None)
        plt.gca().add_patch(circle)

        
        if x != len(self.shape)-1:
          margin_next_layer = (max(self.shape)-self.shape[x+1])*0.5
          for y_n in range(self.shape[x+1]):
            plt.plot([x*self.horizontal_scale+self.radius,x*self.horizontal_scale+1-self.radius],[y+margin,y_n+margin_next_layer], linewidth=.8,c="0.6")
        
    plt.axis('scaled')
    plt.axis('off')
    plt.show()

# a = Architecture().draw()
# a = Architecture([4,5,3,5],figsize=None,xkcd=True).draw()