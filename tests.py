from functions.get_files_info import get_files_info, get_file_content, write_file

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

    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ispsum dolor sit amet")
    print(result)
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result)


if __name__ == "__main__":
    test()  