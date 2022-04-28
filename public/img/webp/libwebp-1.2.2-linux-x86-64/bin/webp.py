import os
import subprocess
file_list = []
dir_list = os.listdir()
for i in dir_list:
    if i.endswith(".png") or i.endswith(".jpeg") or i.endswith(".jpg"):
        file_list.append(i)
if file_list:
    for file_name in file_list:
        print("\nConverting "+ file_name + "\n")
        command = ["./cwebp", file_name, "-q", "80", "-o", file_name.split(".")[0] + ".webp"]
        print("\nPassed command: {}\n".format(command))
        try:
            result = subprocess.run(command, stdout=subprocess.PIPE)
            print(result.stdout)
        except Exception as e:
            print("Error occurred\n{}".format(e))
else:
    print("No image files (jpg, png, jpeg) found")