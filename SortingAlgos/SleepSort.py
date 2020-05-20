from time import sleep
from threading import Timer
 
def sleepSort(values):
    sleepSort.result = []
    def add1(x):
        sleepSort.result.append(x)
    mx = values[0]
    for v in values:
        if mx < v: mx = v
        Timer(v, add1, [v]).start()
    sleep(mx+1)
    return sleepSort.result
 
