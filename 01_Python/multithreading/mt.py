from threading import Thread 
def task():
    print("Thread is running")
    
t=Thread(target =task)
t.start()
t.join()
print("Main program end")