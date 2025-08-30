from functions.get_files_info import get_files_info, get_file_content, write_file
from functions.run_python import run_python_file

def test(): 
    # files = [
    #     "lorem.txt",
    #     "main.py",
    #     "pkg/calculator.py",
    #     "/bin/cat", 
    #     "pkg/does_not_exist.py"
    # ]
    # for file in files: 
    #     result = get_file_content("calculator", file) 
    #     print("Result for " + file +  " directory:")
    #     print(result)
    #     print()

    result = run_python_file("calculator", "main.py")
    print(result)
    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result)
    result =run_python_file("calculator", "tests.py")
    print(result)
    result = run_python_file("calculator", "../main.py")
    print(result)
    result = run_python_file("calculator", "nonexistent.py")
    print(result)


if __name__ == "__main__":
    test()  