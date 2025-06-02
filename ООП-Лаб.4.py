from abc import ABC, abstractmethod

# Composite Pattern

class FileComponent(ABC):
    @abstractmethod
    def display(self, indent=0):
        pass

class File(FileComponent):
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        print('  ' * indent + f'- File: {self.name}')

class Directory(FileComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: FileComponent):
        self.children.append(component)

    def display(self, indent=0):
        print('  ' * indent + f'+ Directory: {self.name}')
        for child in self.children:
            child.display(indent + 1)

# Facade Pattern

class FileSystemFacade:
    def __init__(self):
        self.root = Directory("root")

    def create_file(self, directory: Directory, filename: str):
        new_file = File(filename)
        directory.add(new_file)

    def create_directory(self, parent: Directory, name: str) -> Directory:
        new_dir = Directory(name)
        parent.add(new_dir)
        return new_dir

    def show_structure(self):
        self.root.display()

# Головна програма

def main():
    facade = FileSystemFacade()

    # Створення структури
    docs = facade.create_directory(facade.root, "Documents")
    pics = facade.create_directory(facade.root, "Pictures")

    facade.create_file(docs, "resume.docx")
    facade.create_file(docs, "report.pdf")

    holidays = facade.create_directory(pics, "Holidays")
    facade.create_file(holidays, "beach.png")
    facade.create_file(pics, "selfie.jpg")

    # Виведення
    print("File System Structure:\n")
    facade.show_structure()

if __name__ == "__main__":
    main()
