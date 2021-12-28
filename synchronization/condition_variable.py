import threading

soup_lid = threading.Lock()
soup_servings = 500
soup_taken = threading.Condition(lock=soup_lid)

def hungry_philosophers(person_id: int) -> None:
    global soup_servings
    while soup_servings > 0:
        with soup_lid:
            while (person_id!=(soup_servings%2)) and (soup_servings>0):
                print(f"Person {person_id} checked..and then put the lid back")
                # Release the lock and wait (blocking) until notified or a timeout occurs
                soup_taken.wait()
            if (soup_servings > 0):
                soup_servings -= 1
                print(f"Person {person_id} took soup! Servings left {soup_servings}")
                # wake up the thread waiting for condition variable "soup_taken"
                soup_taken.notify() # if there are more than 2 threads, use .notify_all()


if __name__ == "__main__":
    for person in range(2):
        threading.Thread(target=hungry_philosophers,args=(person,)).start()

