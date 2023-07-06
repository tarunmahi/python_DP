def called(func):
    def triple():
        print("hello")
        func()
    return triple
        
        
def square():
    print("my god")

val=called(square)
val()

