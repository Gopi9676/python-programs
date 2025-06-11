f=open("c:\\users\\MICLAB\\Desktop\\demo.txt",'r')
print("The file pointer is at byte:",f.tell())
f.seek(10);
print("After reading the file pointer is at:",f.tell())
