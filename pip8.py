class stack:
    def __init__(self):  # create the constructor
        self.arr = []

    def push(this, data):  # using push method you can add the element in stack
        this.arr.append(data)

    def pop(this):  # using pop methi\od you can delete the top most element in stack
        return this.arr.pop()

    def isEmpty(this):  # check if stack is empty or not
        return this.arr == []

    def display(this):  # traversal method
        if (this.isEmpty()):  # first check if stack is empty or not
            print("No element in stack")
        for i in this.arr:
            print(i, end=" ")
        print("\n")


st = stack()  # create the object

if st.isEmpty():
  print("\nstack is Empty\n")

else:
  print("stack is not Empty\n")


st.isEmpty()

st.push(11)  # push the element 1
st.push(2)  # push the element 2
st.push(34)  # push the element 3
st.push(224)  # push the element 4
st.push(14)  # push the element 5
print("element of stack\n")
st.display()  # display 
st.pop()  # pop the element its pop top most element 
print("element of stack\n")
st.display()  # display 

if st.isEmpty():
  print("stack is Empty\n")

else:
  print("stack is not Empty\n")


print("\nNAME AND ID :: DHRUV PUVAR AND 20CE117\n")
