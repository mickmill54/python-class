import os
from p6_shared import pad_left, pad_right

label_spacing = 10
number_spacing = 10

while True:
    filename = input("Enter the filename: ").strip()

    if not os.path.exists(filename):
        print(f"The file '{filename}' does not exist. Please enter a valid filename or press Enter to exit.")
        continue
    else:
        try:
            with open(filename, 'r') as file1:
                hash_start = 0
                reg_start = 0
                total = 0

                for line in file1:
                    if line.startswith("#"):
                        hash_start += 1
                    else:
                        reg_start += 1
                        total += int(line)

                avg = total / reg_start if reg_start != 0 else 0

                print(pad_right("Comment:", label_spacing), pad_left(str(hash_start), number_spacing))
                print(pad_right("Count:", label_spacing), pad_left(str(reg_start), number_spacing))
                print(pad_right("Total:", label_spacing), pad_left(str(total), number_spacing))
                print(pad_right("Average:", label_spacing), pad_left(f"{avg:.2f}", number_spacing))
        except:
            print("Error")
    if 'file1' in locals() and not file1.closed:
        file1.close()    
print("Program exited.")