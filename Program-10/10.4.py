try:
    file=open("myfile.txt",'r')
except IOError:
    print("Error:unable to read the file!")
finally:
    file.close()
