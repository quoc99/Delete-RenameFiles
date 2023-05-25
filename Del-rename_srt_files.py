import re
import os
print('\033c')
# import os

# def delete_files_in_folder(folder_path, extensions):
#     for root, dirs, files in os.walk(folder_path):
#         for file in files:
#             for extension in extensions:
#                 if file.endswith(extension):
#                     try:
#                         os.remove(os.path.join(root, file))
#                         print(f'Deleted file: {os.path.join(root, file)}')
#                     except OSError as e:
#                         print(f'Error: {e.filename} - {e.strerror}.')

# folder_path = input('Enter the path of the folder you want to delete files from: ')
# extensions = ('Arabic.srt', 'Dutch.srt', 'French.srt', 'German.srt', 'Indonesian.srt', 'Italian.srt', 'Portuguese.srt', 'Russian.srt', 'Simplified Chinese.srt', 'Spanish.srt', 'Thai.srt', 'Turkish.srt')

# delete_files_in_folder(folder_path, extensions)

# import os

# def delete_files(folder_path, extensions):
#     for root, dirs, files in os.walk(folder_path):
#         for file in files:
#             if file.endswith(extensions):
#                 try:
#                     os.remove(os.path.join(root, file))
#                     print(f"{file} deleted successfully.")
#                 except OSError as e:
#                     print(f"Error: {file} : {e.strerror}")

# folder_path = input('Enter the path of the folder you want to delete files from: ')
# extensions = tuple(input('Enter the file extensions you want to delete (comma-separated): ').split(', '))

# delete_files(folder_path, extensions)

# import os
# import re

# folder_path = input('Enter the path of the folder you want to delete files from: ')

# # Regular expression to match filenames ending with ".srt"
# regex_pattern = r"\.srt$"

# # Iterate over the files in the folder and its subfolders
# for root, dirs, files in os.walk(folder_path):
#     for file in files:
#         # Check if the file matches the regular expression
#         if re.search(regex_pattern, file):
#             # Check if the file is not English or Vietnamese
#             if not file.endswith("English.srt") and not file.endswith("Vietnamese.srt"):
#                 # Construct the full path to the file
#                 file_path = os.path.join(root, file)
#                 # Delete the file
#                 os.remove(file_path)
#                 print(f"Deleted {file_path}")
# import os

# folder_path = input('Enter the path of the folder you want to delete files from: ')

# for subdir, dirs, files in os.walk(folder_path):
#     for file in files:
#         if file.endswith('.srt') and 'English.srt' not in file and 'Vietnamese.srt' not in file:
#             os.remove(os.path.join(subdir, file))
#         elif 'Vietnamese.srt' in file:
#             os.rename(os.path.join(subdir, file), os.path.join(subdir, file.replace('_Vietnamese.srt', '.srt')))

# import os
# import re

# folder_path = input('Enter the path of the folder you want to delete files from: ')

# # Regular expression to match filenames ending with ".srt"
# regex_pattern = r"\.srt$"

# # Iterate over the files in the folder and its subfolders
# for root, dirs, files in os.walk(folder_path):
#     for file in files:
#         # Check if the file matches the regular expression
#         if re.search(regex_pattern, file):
#             # Check if the file is not English or Vietnamese
#             if not file.endswith("English.srt") and not file.endswith(" Vietnamese.srt"):
#                 # Construct the full path to the file
#                 file_path = os.path.join(root, file)
#                 # Delete the file
#                 os.remove(file_path)
#                 print(f"Deleted {file_path}")
#             # Check if the file contains "Vietnamese.srt" in its name
#             elif " Vietnamese.srt" in file:
#                 # Construct the full path to the file
#                 file_path = os.path.join(root, file)
#                 # Construct the new file name without "Vietnamese.srt"
#                 new_file_name = file.replace(" Vietnamese.srt", ".srt")
#                 # Construct the full path to the new file
#                 new_file_path = os.path.join(root, new_file_name)
#                 # Rename the file
#                 os.rename(file_path, new_file_path)
#                 print(f"Renamed {file_path} to {new_file_path}")

# import os
# import re
# import shutil

# folder_path = input('Enter the path of the folder you want to delete files from: ')

# # Regular expression to match filenames ending with ".srt"
# regex_pattern = r"\.srt$"

# # Create the "En" folder to store the English.srt files
# en_folder_path = os.path.join(folder_path, "En")
# if not os.path.exists(en_folder_path):
#     os.makedirs(en_folder_path)

# # Iterate over the files in the folder and its subfolders
# for root, dirs, files in os.walk(folder_path):
#     for file in files:
#         # Check if the file matches the regular expression
#         if re.search(regex_pattern, file):
#             # Check if the file is not English or Vietnamese
#             if not file.endswith("English.srt") and not file.endswith(" Vietnamese.srt"):
#                 # Construct the full path to the file
#                 file_path = os.path.join(root, file)
#                 # Delete the file
#                 os.remove(file_path)
#                 print(f"Deleted {file_path}")
#             # Check if the file contains "Vietnamese.srt" in its name
#             elif " Vietnamese.srt" in file:
#                 # Construct the full path to the file
#                 file_path = os.path.join(root, file)
#                 # Construct the new file name without "Vietnamese.srt"
#                 new_file_name = file.replace(" Vietnamese.srt", ".srt")
#                 # Construct the full path to the new file
#                 new_file_path = os.path.join(root, new_file_name)
#                 # Rename the file
#                 os.rename(file_path, new_file_path)
#                 print(f"Renamed {file_path} to {new_file_path}")
#             # Check if the file is English.srt
#             elif file.endswith("English.srt"):
#                 # Construct the full path to the file
#                 file_path = os.path.join(root, file)
#                 # Construct the full path to the new file in the "En" folder
#                 new_file_path = os.path.join(en_folder_path, file)
#                 # Move the file to the "En" folder
#                 shutil.move(file_path, new_file_path)
#                 print(f"Moved {file_path} to {new_file_path}")
# ******************************************************************************

# import os
# import re

# folder_path = input('Path of the folder you want to delete files: ')
# # Regular expression to match filenames ending with ".srt"
# regex_pattern = r"\.srt$"

# # Iterate over the files in the folder and its subfolders
# for root, dirs, files in os.walk(folder_path):
#     for file in files:
#         # Check if the file matches the regular expression
#         if re.search(regex_pattern, file):
#             # Check if the file is not English or Vietnamese
#             if not file.endswith("English.srt") and not file.endswith("Vietnamese.srt"):
#                 # Construct the full path to the file
#                 file_path = os.path.join(root, file)
#                 # Delete the file
#                 os.remove(file_path)
#                 print(f"Deleted {file_path}")
#             # Check if the file contains "Vietnamese.srt" in its name
#             elif "Vietnamese.srt" in file:
#                 # Construct the full path to the file
#                 file_path = os.path.join(root, file)
#                 # Construct the new file name without "Vietnamese.srt"
#                 new_file_name = file.replace(" Vietnamese.srt", ".srt")
#                 # Construct the full path to the new file
#                 new_file_path = os.path.join(root, new_file_name)
#                 # Rename the file
#                 os.rename(file_path, new_file_path)
#                 print(f"Renamed {file_path} to {new_file_path}")
#             else:
#                 file_path = os.path.join(root, file)
#                 new_file_name = file.replace(" English.srt", ".en_US.srt")
#                 # Construct the full path to the new file
#                 new_file_path = os.path.join(root, new_file_name)
#                 # Rename the file
#                 os.rename(file_path, new_file_path)
#                 print(f"Renamed {file_path} to {new_file_path}")
#import shutil
# Check if the file is English.srt
# else file.endswith("English.srt"):

# Construct the full path to the file
#file_path = os.path.join(root, file)
# # Construct the path to the "English-Sub" folder
# en_folder_path = os.path.join(root, "English-Sub")
# # Create the "English-Sub" folder if it doesn't exist
# if not os.path.exists(en_folder_path):
#     os.makedirs(en_folder_path)
# # Construct the full path to the new file in the "English-Sub" folder
# new_file_path = os.path.join(en_folder_path, file)
# # Move the file to the "English-Sub" folder
# shutil.move(file_path, new_file_path)
# print(f"Moved {file_path} to {new_file_path}")
# Construct the new file name without "Vietnamese.srt"
# ____________________________________________________________________________________________________
# import os
# import re

# folder_path = input('Path of the folder you want to delete files: ')
# # Compiled regular expression to match filenames ending with ".srt"
# regex_pattern = re.compile(r"\.srt$")

# # Iterate over the files in the folder and its subfolders
# for root, dirs, files in os.walk(folder_path):
#     for file in files:
#         try:
#             # Check if the file matches the regular expression
#             if regex_pattern.search(file):
#                 # Check if the file is not English or Vietnamese
#                 if not file.endswith("English.srt") and not file.endswith("Vietnamese.srt"):
#                     # Construct the full path to the file
#                     file_path = os.path.join(root, file)
#                     # Delete the file
#                     os.remove(file_path)
#                     print(f"Deleted {file_path}")
#                 # Check if the file contains "Vietnamese.srt" in its name
#                 elif "Vietnamese.srt" in file:
#                     # Construct the full path to the file
#                     file_path = os.path.join(root, file)
#                     # Construct the new file name without "Vietnamese.srt"
#                     new_file_name = file.replace(" Vietnamese.srt", ".srt")
#                     # Construct the full path to the new file
#                     new_file_path = os.path.join(root, new_file_name)
#                     # Rename the file
#                     os.rename(file_path, new_file_path)
#                     print(f"Renamed {file_path} to {new_file_path}")
#                 else:
#                     file_path = os.path.join(root, file)
#                     new_file_name = file.replace(" English.srt", ".en_US.srt")
#                     # Construct the full path to the new file
#                     new_file_path = os.path.join(root, new_file_name)
#                     # Rename the file
#                     os.rename(file_path, new_file_path)
#                     print(f"Renamed {file_path} to {new_file_path}")
#         except Exception as e:
#             print(f"An error occurred while processing {file}: {e}")
# #____________________________________________________________________________________________________

# import os
# import re

# folder_path = input('Path of the folder you want to delete files: ')
# # Compiled regular expression to match filenames ending with ".srt"
# regex_pattern = re.compile(r"\.vtt$")

# # Iterate over the files in the folder and its subfolders
# for root, dirs, files in os.walk(folder_path):
#     for file in files:
#         try:
#             # Check if the file matches the regular expression
#             if regex_pattern.search(file):
#                 # Check if the file is not English or Vietnamese
#                 if file.endswith(" English.vtt"):
#                     file_path = os.path.join(root, file)
#                     new_file_name = file.replace(" English.vtt", ".en_US.vtt")
#                     # Construct the full path to the new file
#                     new_file_path = os.path.join(root, new_file_name)
#                     # Rename the file
#                     os.rename(file_path, new_file_path)
#                     print(f"Renamed {file_path} to {new_file_path}")
#                     continue
#         except Exception as e:
#             print(f"An error occurred while processing {file}: {e}")
# ------------------------------------------------------------------------------------------------------------

# import os
# import re

# folder_path = input('Path of the folder you want to delete files: ')
# # Compiled regular expression to match filenames ending with ".srt"
# regex_pattern = re.compile(r"\.srt$")

# # Iterate over the files in the folder and its subfolders
# for root, dirs, files in os.walk(folder_path):
#     for file in files:
#         try:
#             # Check if the file matches the regular expression
#             if regex_pattern.search(file):
#                 # Check if the file is not English or Vietnamese
#                 if file.endswith(".srt"):
#                     file_path = os.path.join(root, file)
#                     new_file_name = file.replace(".srt", ".en_US.srt")
#                     # Construct the full path to the new file
#                     new_file_path = os.path.join(root, new_file_name)
#                     # Rename the file
#                     os.rename(file_path, new_file_path)
#                     print(f"Renamed {file_path} to {new_file_path}")
#                     continue
#         except Exception as e:
#             print(f"An error occurred while processing {file}: {e}")


folder_path = input('Path of the folder you want to process files: ')
parent_folder = os.path.dirname(folder_path)
# Compiled regular expression to match filenames ending with ".srt"
regex_pattern = re.compile(r"\.srt$")

# Iterate over the files in the folder and its subfolders
for root, dirs, files in os.walk(folder_path):
    for file in files:
        try:
            # Check if the file matches the regular expression
            if regex_pattern.search(file):
                # Check if the file is not English or Vietnamese
                if file.endswith(".srt"):
                    file_path = os.path.join(root, file)
                    new_file_name = file.replace(".srt", ".en_US.srt")
                    # Construct the full path to the new file in the parent folder
                    new_file_path = os.path.join(parent_folder, new_file_name)
                    # Rename the file
                    os.rename(file_path, new_file_path)
                    print(f"Renamed {file_path} to {new_file_path}")
                    continue
        except Exception as e:
            print(f"An error occurred while processing {file}: {e}")

