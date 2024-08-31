class Vector:
    def __init__(self, dataset: list):
        self.data = dataset

    def __add__(self, addend):
        output = Vector([])
        if len(self) == 0 or (isinstance(addend, self.__class__) and len(addend) == 0):
            raise ValueError("Empty vectors cannot be used for addition.")
        if isinstance(addend, self.__class__):
            if len(self.data) != len(addend.data):
                raise ValueError("Vector dimensions must agree.")
            for idx in range(len(self.data)):
                if type(addend.data[idx]) is not type(self.data[idx]):
                    raise TypeError("Vector addition can only be performed on similar datatypes.")
                output.data.append(self.data[idx] + addend.data[idx])
            return output
        for dimension in self.data:
            if type(addend) is not type(dimension):
                raise TypeError("Vector addition can only be performed on similar datatypes.")
            output.data.append(dimension + addend)
        return output

    def __sub__(self, addend):
        output = Vector([])
        if len(self) == 0 or (isinstance(addend, self.__class__) and len(addend) == 0):
            raise ValueError("Empty vectors cannot be used for subtraction.")
        if isinstance(addend, self.__class__):
            if len(self.data) != len(addend.data):
                raise ValueError("Vector dimensions must agree.")
            for idx in range(len(self.data)):
                if type(addend.data[idx]) is not type(self.data[idx]):
                    raise TypeError("Vector subtraction can only be performed on similar datatypes.")
                output.data.append(self.data[idx] - addend.data[idx])
            return output
        for dimension in self.data:
            if type(addend) is not type(dimension):
                raise TypeError("Vector subtraction can only be performed on similar datatypes.")
            output.data.append(dimension - addend)
        return output

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return "Vector: " + str(self.data)