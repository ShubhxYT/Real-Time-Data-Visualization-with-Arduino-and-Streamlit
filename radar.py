from matplotlib import pyplot as plt
import matplotlib
import numpy as np
import random
import keyboard
# from arduino import radar_value
import time

matplotlib.use('TkAgg')

angle = 0
pos = 0

def fake_radar_data():
    global angle, pos
    if pos == 1:
        angle -= 1
        dist = random.randint(0, 100)
        if angle <= 0:
            pos = 0
        return [angle, dist]
    elif pos == 0:
        angle += 1
        dist = random.randint(0, 100)
        if angle >= 180:
            pos = 1
        return [angle, dist]

def radar_plot():
    fig = plt.figure(facecolor='k')
    fig.canvas.toolbar.pack_forget()
    fig.canvas.manager.set_window_title('Ultrasonic Radar Plot')
    
    mng = plt.get_current_fig_manager()

    window_width = 1223
    window_height = 860
    window_offset_x = 100
    window_offset_y = 100

    # Calculate subplot position relative to the window
    left = (window_offset_x / window_width)-0.17
    bottom = window_offset_y / window_height
    width = 1.0 - left  # Use full width of the window
    height = 1.0 - bottom  # Use full height of the window

    # Set subplot position
    mng.window.wm_geometry(f"{window_width}x{window_height}+600+193")

    ax = fig.add_subplot(1, 1, 1, polar=True, facecolor='#006b70')
    # mng.window.state('zoomed')

    ax.tick_params(axis='both', colors='w')
    r_max = 75.0
    ax.set_ylim([0.0, r_max])
    ax.set_xlim([0.0, np.pi])
    ax.set_position([left, bottom, 1, 1])
    # ax.set_position([-0.1, -0.1, 0.8, 0.8])  # Adjusted to fit better within the window
    ax.set_rticks(np.linspace(0.0, r_max, 5))
    ax.set_thetagrids(np.linspace(0, 180, 10))
    ax.grid(color='w', alpha=0.4)

    angles = np.arange(0, 181, 1)
    theta = angles * (np.pi / 180.0)

    pols, = ax.plot([], linestyle='', marker='o', markerfacecolor='r',
                    markeredgecolor='w', markeredgewidth=1.0, markersize=3.0,
                    alpha=0.9)

    line1, = ax.plot([], color='w', linewidth=4.0)

    fig.canvas.draw()
    dists = np.ones((len(angles),))
    fig.show()
    fig.canvas.blit(ax.bbox)
    fig.canvas.flush_events()
    axbackground = fig.canvas.copy_from_bbox(ax.bbox)

    while True:
        try:
        # angle, dist = fake_radar_data()
            from arduino import all_values
            try :
                _,_,_,_,_,radar_value = all_values()
            except :
                radar_value = [0,0]   
            print(radar_value)
            angle,dist = radar_value
            dists[int(angle)] = dist
            pols.set_data(theta, dists)
            fig.canvas.restore_region(axbackground)
            ax.draw_artist(pols)
            line1.set_data(np.repeat((angle * (np.pi / 180)), 2),
                        np.linspace(0.0, r_max, 2))
            ax.draw_artist(line1)
            fig.canvas.blit(ax.bbox)
            fig.canvas.flush_events()
            # time.sleep(0.1)
            if keyboard.is_pressed('q'):
                plt.close('all')
                print("User need to Quit the application")
                break   
        except KeyboardInterrupt:
            plt.close('all')
            print('Keyboard Interrupt')
            break

# Call the function when you want to open the radar plot window
# radar_plot()
