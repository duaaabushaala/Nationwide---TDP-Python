class First:
    def message1(self):
        print("Hello from First")

    
class Second(First):
    def message2(self):
        print("Hello from Second")


class Third(Second):
    def message3(self):
        print("Hello from third")

ref = Second()
ref.message1()