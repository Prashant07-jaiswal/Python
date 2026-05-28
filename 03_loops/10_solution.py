import time    #to make system sleep during wait time

wait_time = 1      #in second
max_retries = 5
attempt = 0

while attempt<max_retries:
    print("Attempt", attempt+1, "wait time", wait_time, "second")    #(attempt+1) just for better readability for user during o/p
    time.sleep(wait_time)     #system under goes sleep during wait time
    wait_time *= 2
    attempt += 1

