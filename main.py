import os
os.system('pip install -r requirements.txt')
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math
import sys
import platform
import addcopyfighandler



matplotlib.use('qt5agg')

platform = platform.system()

if platform == "Windows":
    clear_command = 'cls'

elif platform == "Linux":
    clear_command = 'clear'

else:
    print("Your OS is currently not supported!")
    sys.exit(0)

os.system(clear_command)
mode = input("Available modes:\nTable mode - [T]\nPlot mode - [P]\n> ")

if mode == "t" or mode == "T":
    os.system(clear_command)
    startval = input("Enter starting value:\n> ")

    os.system(clear_command)
    print("Starting value: " + startval)
    endval = input("\nEnter end value:\n> ")

    os.system(clear_command)
    print("Starting value: " + startval)
    print("Ending value: " + endval)
    function = input("\nEnter function:\n> ")

    os.system(clear_command)
    print("Function: " + function + "\n")

    diff = abs(int(startval) - int(endval))
    if int(startval) <= 0 and int(endval) >= 0:
        diff += 1

    x = np.linspace(int(startval), int(endval), diff)

    print(x)
    print(eval(function))
    sys.exit(0)

elif mode == "p" or mode == "P":
    os.system(clear_command)
    plot_amt = input("Enter amount of graphs you want to plot:\n> ")

    for i in range(int(plot_amt)):
        os.system(clear_command)
        startval = input("Enter starting value:\n> ")

        os.system(clear_command)
        print("Starting value: " + startval)
        endval = input("\nEnter end value:\n> ")

        os.system(clear_command)
        print("Starting value: " + startval)
        print("Ending value: " + endval)
        x = np.linspace(int(startval), int(endval), 250)
        function = input("\nEnter function:\n> ")

        y = eval(function)
        plt.plot(x, y)

    os.system(clear_command)
    scale_x = input("Enter x axis length: \n> ")

    os.system(clear_command)
    print("X axis length: " + scale_x)
    scale_y = input("\nEnter y axis length: \n> ")

    plt.axis([-(int(scale_x) / 2), int(scale_x) / 2, -(int(scale_y) / 2), int(scale_y) / 2])

    os.system(clear_command)
    print("X axis length: " + scale_x)
    print("Y axis length: " + scale_y)
    centered = input("\nCenter axes? [y/n] \n> ")
    os.system(clear_command)

    ax = plt.gca()

    if centered == "y":
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

    plt.show()
