from functions.get_files_info import get_files_info, get_file_content

def test(): 
    # result = get_files_info("calculator", ".")
    # print("Result for current directory:")
    # print(result)
    # print()

    files = [
        "lorem.txt",
        "main.py",
        "pkg/calculator.py",
        "/bin/cat", 
        "pkg/does_not_exist.py"
    ]
    for file in files: 
        result = get_file_content("calculator", file) 
        print("Result for " + file +  " directory:")
        print(result)
        print()


if __name__ == "__main__":
    test()  