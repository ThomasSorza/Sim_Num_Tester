
class FileManager:
    def __init__(self, input_file_path = ''):
        self.input_file_path = input_file_path
        self.numbers = []

    def storage_numbers(self):
        try:
            with open(self.input_file_path, 'r') as input_file:
                lines = input_file.readlines()
                for line in lines:
                    line =  line[0:7]

                    self.numbers.append(line)
        except FileNotFoundError:
            print("El archivo de entrada no existe.")
        except Exception as e:
            print(f"Se ha producido un error: {str(e)}")