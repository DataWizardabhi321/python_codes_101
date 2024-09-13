import  threading
import  time
#functon  to stimulate some task
def  task(name):
    print(f'starting  task{name}')
    time.sleep(2) #simulate  some task
    print(f'task {name} completed')
#main  function  to create  amd  start  thread
def  main():
    #num of  threads  to create 
    num_threads= 5

    #create   start   threads
    threads= []
    for  i in range(num_threads):
        thread= threading.Thread(target= task, args=(f'Thread-{i+1}',))
        threads.append(thread)
        thread.start()
    #wait   for  other  thereads   to complete 
    for thread in threads:
        thread.join()
    print('all  task  completed')
if __name__ == "__main__":
    main()
    