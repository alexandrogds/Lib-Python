import os
import argparse

def count_lines_in_directory(directory):
    total_lines = 0

    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
                lines = file.readlines()
                total_lines += len(lines)
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            count_lines_in_directory(dir_path)

    return total_lines

def main():
    parser = argparse.ArgumentParser(description="Count lines of code in text files recursive.")
    parser.add_argument("directory", help="Directory to search for text files.")
    args = parser.parse_args()

    directory = args.directory
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return

    total_lines = count_lines_in_directory(directory)
    print(f"Total lines of code in text files: {total_lines}")

if __name__ == "__main__":
    main()
