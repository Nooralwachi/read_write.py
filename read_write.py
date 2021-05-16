import time
import threading

def read_end(filename, interval, times):
    with open(filename, 'r') as f:
        for line in lines:
            f.seek(0, 2)
            for _ in range(times):
                    print(f.readline(), end="")
                    time.sleep(1)


def write_list(filename, lines, interval):
    with open(filename, 'a') as f:
        for line in lines:
            f.write(line)
            time.sleep(1)

file1 = './file_threading'
lines = ["this is line1\n", "this is line2\n", "this is line3\n", "this is line4\n"]

t1=threading.Thread(target=write_list, args=(file1,lines,1))
t2=threading.Thread(target=read_end, args=(file1, 1, 10))

t1.start()
t2.start()

t1.join()
t2.join()