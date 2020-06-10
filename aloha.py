import random
import matplotlib.pyplot as plt


class Station:
    """
    sendTime是当前时隙距离下一次传输的时隙间隔
    """

    def __init__(self, sendTime):
        self.sendTime = sendTime

    """
    tick 代表距离下一次发送时间减少了一个时隙
    """
    def tick(self):
        self.sendTime = self.sendTime - 1


def simulation():
    random.seed()

    for window_size in [ 8, 16, 32]:
    # for window_size in [8]:
        senderNum = []
        slotEfficiencies = []
        print("Window size: {0:2d}".format(window_size))

        for N in range(1, 33):  #N个发送方
            stations = [Station(random.randrange(0, window_size)) for _ in range(N)]
            successfulSlots = 0
            slotEfficiency = 0

            totalSlot = 0
            while (successfulSlots < 10000):
                totalSlot += 1

                transmitted_nodes = []

                for i in range(N):
                    if not stations[i].sendTime:
                        # 某个时间槽内要发送的节点
                        transmitted_nodes.append(i)

                        # 不管是否冲突都要设置下一次发送的时间
                        stations[i].sendTime = random.randrange(0, window_size)
                    else:
                        stations[i].tick()

                if (len(transmitted_nodes) == 1):
                    successfulSlots = successfulSlots + 1
                else:
                    pass

            slotEfficiency = (10000 / totalSlot)

            print("N = {0:2d}: {1:f}".format(N, slotEfficiency))

            senderNum.append(N)
            slotEfficiencies.append(slotEfficiency)

        plt.plot(senderNum, slotEfficiencies)
        print()

    plt.xlabel("Number of Nodes")
    plt.ylabel("Slot Efficiency")
    plt.legend(['W = 8', 'W = 16', 'W = 32'], loc='upper right')
    plt.axis([0, 32, 0, 1])
    plt.grid(linestyle='-')
    plt.title("Simulation of Aloha Protocol")
    plt.savefig("aloha.png")
    plt.show()

    return

if __name__ == "__main__":
    simulation()
