'''
投げられたボールのきせきをプロットする
'''
from matplotlib import pyplot as plt
from matplotlib import animation
import math

g=9.8
def get_intervals(u,theta):
    t_flight=2*u*math.sin(theta)/g
    intervals=[]
    start=0
    interval=0.05
    while start<t_flight:
        intervals.append(start)
        start+=interval
    return intervals


def update_position(i,circle,intervals,u,theta):
    t=intervals[i]
    x=u*math.cos(theta)*t
    y=u*math.sin(theta)*t-0.5*g*t*t
    circle.center=x,y
    return circle

def create_animation(u,theta):
    intervals=get_intervals(u,theta)
    xmin=0
    xmax=u*math.cos(theta)*intervals[-1]
    ymin=0
    t_max=u*math.sin(theta)/g
    ymax=u*math.sin(theta)*t_max-0.5*g*t_max**2
    fig=plt.gcf()

    ax=plt.axes(xlim=(xmin,xmax),ylim=(ymin,ymax))

    circle=plt.Circle((xmin,ymin),1.0)
    ax.add_patch(circle)
    anim=animation.FuncAnimation(fig,update_position,fargs=(circle,intervals,u,theta),

                                 frames=len(intervals),interval=1,repeat=False)

    plt.title("projectile motion")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

if __name__=="__main__":
    try:
        initial_v=100
        theta=20.0
    except ValueError:
        print("入力ふせい")
    else:
        theta=math.radians(theta)
        create_animation(initial_v,theta)












