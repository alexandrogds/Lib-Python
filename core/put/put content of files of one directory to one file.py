import os

def concatenate_files(folder_path, base_output_file, seek):
    output_file = base_output_file
    output_index = 1
    file_counter = seek
    for filename in sorted(os.listdir(folder_path)):
        file_counter += 1
        if file_counter <= seek:
            continue
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                file_content = file.read() + '\n'
                while len(file_content) > 0:
                    with open(output_file, 'a', encoding='utf-8') as output:
                        if len(file_content) <= 1300:
                            output.write(file_content)
                            file_content = ''
                        else:
                            chunk = file_content[:1300]
                            output.write(chunk)
                            file_content = file_content[1300:]
                    output_file = f"{base_output_file}_{output_index}"
                    output_index += 1
    print(f"Contents of all files in '{folder_path}' have been concatenated starting with base output file '{base_output_file}'.")

def main():
    folder_path = input("Enter the path of the folder containing files: ")
    base_output_file = input("Enter the path of the base output file: ")

    concatenate_files(folder_path, base_output_file, 0)

if __name__ == "__main__":
    main()