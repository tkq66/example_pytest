class SampleClass:

    def __init__(self, a, b):
        self.aa = a
        self.bb = b

    def class_func_1(self):
        print("Hello " + self.aa)
    
    def class_func_2(self, cc):
        return self.aa + self.bb + cc