import threading
from queue import Queue
import numpy as np
import matplotlib.pyplot as plt
import warnings

from multithreading.inputs import plot_input, random_loop
from multithreading.texts import main_loop_info
from multithreading.classes import Packet


def main():
    warnings.simplefilter("ignore", UserWarning)

    communication_queue = Queue()

    t1 = threading.Thread(target=main_loop, args=(communication_queue,))
    t2 = threading.Thread(target=plot_loop, args=(communication_queue,))
    t3 = threading.Thread(target=random_loop, args=(communication_queue,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Exiting...")


def main_loop(out_q):
    print(main_loop_info)
    ans = ""
    while ans != "exit":
        ans = input(">_: ")
        match ans:
            case "plot":
                plot_input(out_q)


def plot_loop(in_q):
    plots = {}

    plot1 = plt.figure(1)
    ax = plot1.add_subplot(111)
    ax.set_title("Plot 1")

    plot2 = plt.figure(2)
    ax = plot2.add_subplot(111)
    ax.set_title("Plot 2")

    plots["plot1"] = plot1
    plots["plot2"] = plot2

    iss = {
        "plot1": 0,
        "plot2": 0
    }
    last_value = 0
    while True:
        if not in_q.empty():
            packet: Packet = in_q.get()
            value = packet.data
            match packet.origin:
                case "plot_input":
                    plots["plot1"].axes[0].plot(iss["plot1"], value, "ro")
                    iss["plot1"] += 1

                case "random_input":
                    plots["plot2"].axes[0].plot(
                        np.linspace(iss["plot2"]-1, iss["plot2"], num=100),
                        np.linspace(last_value, value, num=100), "g-")

                    last_value = value
                    iss["plot2"] += 1

        plt.pause(0.25)


if __name__ == "__main__":
    main()
