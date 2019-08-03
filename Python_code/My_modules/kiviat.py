#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

def kiviat(skills, ratings, rating_max, abs_path='', name='', svg=False, png=False):
    '''
    Function for create a Kiviat or Radar charts (PES charts).
    
    Args:
        skills (list): The list of labels(str) to display in the chart
        
        ratings (list): The list of ratings(float) for fill the area  of chart
        
        rating_max (float): Value of the maximum ratings
        
        abs_path (str): Absolute path for saving the chart
        
        name (str): name of picture of the chart
        
        svg (boolean): Boolean for saving in svg the chart
        
        png (boolean): Boolean for saving in png the chart
        
    Returns:
        fig: matplotlib figure or None
        
    '''
    if (len(ratings) == len(skills)) and (len(ratings)>0):
        r = np.concatenate((ratings,[ratings[0]]))
        angles = np.linspace(0, 2*np.pi, len(skills), endpoint=False)
        angles = np.concatenate((angles,[angles[0]]))
        fig = plt.figure()
        ax = fig.add_subplot(111,polar=True)
        ax.plot(angles, r,'o-',linewidth=2)
        ax.fill(angles, r, alpha=0.25,color='green')
        ax.set_rlim(0,rating_max)
        ax.set_thetagrids(angles * 180/np.pi, skills)
        ax.grid(True)
        if (abs_path!='') and (name!='') and (svg or png):
            path = abs_path.replace('\\','/')
            print(path)
            if svg:
                plt.savefig(path+'/'+name+'.svg')
            else:
                plt.savefig(path+'/'+name+'.png')
        return fig
    else:
        return None



    