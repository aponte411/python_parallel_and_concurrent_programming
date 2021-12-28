import threading

bag_of_chips = 1
pencil = threading.Lock()

def cpu_work(work_units: int) -> None:
    x=0
    for i in range(work_units*1000000):
        x += 1

def baron_shopper():
    global bag_of_chips
    cpu_work(1)
    with pencil:
        bag_of_chips *= 2
        print("Baron doubled the chips")

def olivia_shopper():
    global bag_of_chips
    cpu_work(1)
    with pencil:
        bag_of_chips += 3
        print("Olivia added 3 bags of chips")

if __name__ == "__main__":
    shoppers = []
    for i in range(5):
        shoppers.append(threading.Thread(target=baron_shopper))
        shoppers.append(threading.Thread(target=olivia_shopper))
    for s in shoppers:
        s.start()
    for s in shoppers:
        s.join()
    print(f"We need to buy {bag_of_chips}")
