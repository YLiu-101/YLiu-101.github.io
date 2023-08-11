import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
def run_simulation(positions, velocities, masses, restitution):

  """  Generates and saves the graph and data on positions + velocities of objects in question given initial conditions

  @param: Initial positions, velocities, masses, and
  """

  positions = np.array(positions).astype('float64')
  velocities = np.array(velocities).astype('float64')
  masses = np.array(masses).astype('float64')
  collision_count = 0
  time=0
  time_delta=0.01
  block_vel_data = []
  block_position_data = []
  num_blocks = positions.size
  def single_collision_sim(m_0,m_1,v_0,v_1,restitution):
    p_0 = m_0*v_0+m_1*v_1
    total_mass = m_0+m_1
    rel_vel_0 = v_1-v_0
    v_0 = (p_0 + m_1*restitution*(rel_vel_0))/total_mass
    v_1 = (p_0-m_0*v_0)/m_1
    return (v_0,v_1)
  def check_collision(position_arr):
    """
    Checks if a collision has occured
    """
    collisions = []
    for i in range(len(position_arr)-1): #inspiration for a circular world here!
        if position_arr[i]-position_arr[i+1]>=-0.95+0.94999999999999:
          collisions.append(i)
    return collisions

  def update_metrics():
    nonlocal positions, velocities, masses, restitution, collision_count
    #How to account for multiple collisions at once? --> Need some if-else statement for that?
    collisions = check_collision(positions.tolist())
    for i in collisions:
      vel_pair = single_collision_sim(masses[i],masses[i+1],velocities[i],velocities[i+1],restitution)
      collision_count+=1
      velocities[i] = vel_pair[0]
      velocities[i+1] = vel_pair[1]

  def simulation_ongoing():
    """
    Checks if there are any more collisions to occur
    """
    for i in range(len(velocities)-1):
      if (velocities[i+1] - velocities[i] < 0):
        return True
    return False

  ## Running the simulations
  while (simulation_ongoing()):
    # counter+=1
    block_position_data.append(positions.tolist())
    block_vel_data.append(velocities.tolist())

    update_metrics()
    # print(counter)
    time+= time_delta

    positions += velocities*time_delta
  def legend_gen(num):
    legend = []
    for i in range(num):
      legend.append("Block " + str((i+1)))
    return legend

  def draw_time_graphs(ax, data, time_delta,y_axis,title="Title", x_axis="Time (seoncds)", log=False):
    datapoints = len(data)
    time_series = []
    for i in range(datapoints):
      time_series.append((i)*time_delta)
    ax.set_title(title)
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    for i in range(num_blocks):
      ax.plot(time_series, data[:,i])
    ax.legend(legend_gen(num_blocks))
    if log:
      ax.set_yscale("log")
    # ax.tight_layout()
    # ax.show()
  plt.style.use('seaborn')
  fig,ax = plt.subplots(nrows=1, ncols=2)
  draw_time_graphs(ax[0], np.array(block_vel_data), time_delta, y_axis="Velocity Data", title="Block Velocities over time with " + str(collision_count) + " total collisions", x_axis="Time (seoncds)")
  draw_time_graphs(ax[1], np.array(block_position_data), time_delta, y_axis="Position Data", title="Block Positions over time with " + str(collision_count) + " total collisions", x_axis="Time (seoncds)")
  plt.subplots_adjust(left=0.1,
                      bottom=0.1,
                      right=1.5,
                      top=0.9,
                      wspace=0.4,
                      hspace=0.4)
  plt.savefig("x-v-analysis.png")
  pd.DataFrame(block_position_data, ).to_csv("Block-Postion-Data.csv")
  pd.DataFrame(block_vel_data).to_csv("Block-Velocity-Data.csv")

  plt.show()
positions = [0,1,2] #For now, we'll make the positions array in increasing order, but we'll have to write an algorithm to implement this later!
velocities = [0,0,-5]
masses = [1e99,1,1000000000]
restitution = 1
positions = np.array(positions).astype('float64')
velocities = np.array(velocities).astype('float64')
masses = np.array(masses).astype('float64')
# collision_count = 0
run_simulation(positions, velocities, masses, restitution)
