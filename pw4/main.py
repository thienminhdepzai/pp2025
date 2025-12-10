from input import get_input
from output import display
from domains.student import Student

def main():
    name = get_input("Name: ")
    s = Student(name)
    display(f"Student: {s.name}")

if __name__ == "__main__":
    main()
