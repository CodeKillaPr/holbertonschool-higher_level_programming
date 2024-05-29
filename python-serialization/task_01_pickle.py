import pickle
""" serialize and deserialize """


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance and save it to the provided filename.

        Parameters:
        filename (str): The filename where the object will be serialized.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error during serialization: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance from the provided filename.

        Parameters:
        filename (str): The filename from
        where the object will be deserialized.

        Returns:
        CustomObject: An instance of CustomObject.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
                else:
                    print("Deserialized object is not of type CustomObject.")
                    return None
        except Exception as e:
            print(f"Error during deserialization: {e}")
            return None
