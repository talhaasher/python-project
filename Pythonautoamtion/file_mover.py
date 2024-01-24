import os
import shutil
import time

# Define directories and target extensions for different file types
txt_directories = {
    "C:\\Users\\Talha": 'D:\\autoamte\\txt',
    "C:\\Users\\Talha\\Documents": 'D:\\autoamte\\txt',
    "C:\\Users\\Talha\\Downloads": 'D:\\autoamte\\txt'
}
txt_target_extensions = ['.txt']

pdf_directories = {
    "C:\\Users\\Talha": 'D:\\autoamte\\pdf',
    "C:\\Users\\Talha\\Documents": 'D:\\autoamte\\pdf',
    "C:\\Users\\Talha\\Downloads": 'D:\\autoamte\\pdf'
}
pdf_target_extensions = ['.pdf']

msoffice_directories = {
    "C:\\Users\\Talha": 'D:\\autoamte\\ms_office',
    "C:\\Users\\Talha\\Documents": 'D:\\autoamte\\ms_office',
    "C:\\Users\\Talha\\Downloads": 'D:\\autoamte\\ms_office'
}
msoffice_target_extensions = ['.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx', '.mdb', '.accdb', '.odt', '.odp']

media_directories = {
    "C:\\Users\\Talha": 'D:\\autoamte\\media',
    "C:\\Users\\Talha\\Documents": 'D:\\autoamte\\media',
    "C:\\Users\\Talha\\Downloads": 'D:\\autoamte\\media'
}
media_target_extensions = ['.mp3', '.mp4', '.avi', '.mkv', '.jpg', '.png', '.gif', '.bmp', '.webm', '.svg']

coding_directories = {
    "C:\\Users\\Talha": 'D:\\autoamte\\code',
    "C:\\Users\\Talha\\Documents": 'D:\\autoamte\\code',
    "C:\\Users\\Talha\\Downloads": 'D:\\autoamte\\code'
}
coding_target_extensions = ['.py', '.java', '.cpp', '.html', '.css', '.js', '.php', '.rb', '.swift', '.kt', '.lua', '.asm']

excietable_directories = {
    "C:\\Users\\Talha": 'D:\\autoamte\\excietable',
    "C:\\Users\\Talha\\Documents": 'D:\\autoamte\\excietable',
    "C:\\Users\\Talha\\Downloads": 'D:\\autoamte\\excietable'
}
excietable_target_extensions = ['.exe', '.msi']

# Combine all directories and target extensions
all_directories = [txt_directories, pdf_directories, msoffice_directories, media_directories, coding_directories, excietable_directories]
all_target_extensions = [txt_target_extensions, pdf_target_extensions, msoffice_target_extensions, media_target_extensions, coding_target_extensions, excietable_target_extensions]

# Infinite loop to keep the script running
while True:
    # Iterate through different types of files and their target extensions
    for directories, target_extensions in zip(all_directories, all_target_extensions):
        # Iterate through source and destination directories for each file type
        for source_directory, destination_directory in directories.items():
            # Get a list of files in the source directory
            files = os.listdir(source_directory)
            for file in files:
                # Check if the current file has a target extension
                if any(file.endswith(ext) for ext in target_extensions):
                    source_path = os.path.join(source_directory, file)
                    destination_path = os.path.join(destination_directory, file)
                    
                    # Extract drive letters from source and destination paths
                    source_drive = os.path.splitdrive(source_path)[0]
                    destination_drive = os.path.splitdrive(destination_path)[0]

                    # Check if source and destination are on different drives
                    if source_drive != destination_drive:
                        # Copy the file from source to destination
                        shutil.copy(source_path, destination_path)
                        # Remove the file from the source
                        os.remove(source_path)
                    else:
                        # Move the file from source to destination
                        shutil.move(source_path, destination_path)

                    # Print a message about the file movement
                    print(f"Moved {file} to {destination_directory}")

# End of script
