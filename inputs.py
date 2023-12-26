import time

from multithreading.classes import Packet


def plot_input(out_q):
    ans = ""
    while True:
        ans = input("Plot what? (type 'exit' to exit): ")
        if ans == "exit":
            break
        try:
            ans = int(ans)
        except:
            print("Invalid input.")
            continue
        out_q.put(Packet(ans, "plot_input"))


def random_loop(out_q):
    import random
    while True:
        out_q.put(Packet(random.randint(0, 100), "random_input"))
        time.sleep(1)
