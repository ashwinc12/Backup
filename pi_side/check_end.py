import os

for fname in os.listdir('.'):
    if fname.endswith('.avi'):
        # do stuff on the file
        print("hi");
        
        break
