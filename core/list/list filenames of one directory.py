import os

def list_files(directory):
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        return files
    except OSError as e:
        print(f"Error: {e}")
        return []

def main():
    directory = input("Enter the path of the directory: ")
    
    if os.path.isdir(directory):
        files = list_files(directory)
        if files:
            print("Files in the directory:")
            for file in files:
                print(file)
        else:
            print("No files found in the directory.")
    else:
        print("Error: Not a valid directory path.")

if __name__ == "__main__":
    main()
