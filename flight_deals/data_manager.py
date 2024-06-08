class DataManager:
    def __init__(self):
        self.data = []

    def get_data(self):
        return self.data

    def add_data(self, new_data):
        self.data.append(new_data)

    def update_data(self, index, new_data):
        self.data[index] = new_data

    def delete_data(self, index):
        self.data.pop(index)

    def save_data(self):
        with open("data.txt", mode="w") as file:
            for item in self.data:
                file.write(f"{item}\n")

    def load_data(self):
        with open("data.txt", mode="r") as file:
            self.data = [item.strip() for item in file.readlines()]

    def clear_data(self):
        self.data = []
        self.save_data()

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)

