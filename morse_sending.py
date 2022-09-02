import string
import random
import time
#   "1 2 3 4 5 6 7 8 9 10111213"
s = "ETANIMSODURKCPBGWLQHFYZVXJ"
level = int(input("Enter level from 1-13 : "));
delay = int(input("Enter delay time in second: "));

print("(Press Ctl+C to quit)");
while True:
    idx = random.randint(0,level*2-1)
    print(s[idx]);
    time.sleep(delay);

    
    
