from collections import defaultdict
import queue

class Broadcaster():
    def __init__(self):
        self.pulse = 0
        self.sendto = []

    def sent(self,queue):
        [queue.put((self,self.pulse),sendto) for sendto in self.sendto]

    def receive(self,pulse,source):
        [low,high][pulse](self)

class FlipFlop():
    def __init__(self):
        self.pulse = 0
        self.sendto = []

    def sent(self,queue):
        [queue.put((self,self.pulse,sendto)) for sendto in self.sendto]

    def receive(self,pulse,source):
        [low,high][pulse](self)

class Conjunction():
    def __init__(self):
        self.memory = defaultdict(int,{})
        self.pulse = 0
        self.sendto = []

    def sent(self,queue):
        self.pulse = 1 >> all(self.memory.values())
        [queue.put((self,self.pulse,sendto)) for sendto in self.sendto]

    def receive(self,pulse,source):
        self.memory[source] = pulse
        [low,high][pulse](self)

def low(obj): 
    obj.pulse = 1 >> obj.pulse # switch pulse from True to False or False to True

def high(obj):
    pass

if __name__ == '__main__':

    ## manually create test 
    """broadcaster -> a, b, c
    %a -> b
    %b -> c
    %c -> inv
    &inv -> a"""
    broadc = Broadcaster()
    a = FlipFlop()
    b = FlipFlop()
    c = FlipFlop()
    INV = Conjunction()
    setattr(broadc,'sendto',[a,b,c])
    setattr(a,'sendto',[b])
    setattr(b,'sendto',[c])
    setattr(c,'sendto',[INV])
    setattr(INV,'sendto',[a])

    Queue = queue.Queue()
    ## push button -> low -> broadcaster  add jobs to queue
    for st in broadc.sendto:
        Queue.put((broadc,broadc.pulse,st))

    while not Queue.empty():
        source,pulse,target = Queue.get()
        print(source,pulse,target)
        target.receive(pulse,source)
        target.sent(Queue)

