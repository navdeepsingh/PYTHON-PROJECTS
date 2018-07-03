import time, webbrowser

counter = 1
loop_time = 3
while(counter <= 3):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=5kIe6UZHSXw")
    print(counter)
    counter = counter + 1
