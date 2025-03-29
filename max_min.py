#b) Create a python program to input marks of 10 students and print the maximum mark, minimum mark and average mark of the students. 
list1 = []
#while loop____________________________________________________________________________________
i = 0
while i < 10:
    stumarks = int(input("Enter a mark: "))
    list1.append(stumarks)
    i += 1
#def____________________________________________________________________________________________
def process (a):
    suming = sum(list1)
    count2 = len(list1)
    avg = (suming/count2)
    print("Maximum mark: " ,max(list1),
          "Minimum mark: ",min(list1),
          "Avarage marks: ",avg )

#calling out the function
process(list1)



