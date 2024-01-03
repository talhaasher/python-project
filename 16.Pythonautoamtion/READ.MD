# File Organizer Script

This script is designed to automatically organize files based on their types into specific directories. It monitors specified source directories for files with certain extensions and moves or copies them to corresponding destination directories based on the file type.

## Usage

1. Clone this repository to your local machine.

2. Modify the script according to your needs by specifying the source directories and their corresponding target directories for different file types.

3. Run the script using a Python interpreter.

The script will run in an infinite loop, continuously monitoring the specified source directories for files with matching extensions and organizing them into the respective destination directories.

## Features

- Organizes various file types including text files, PDFs, MS Office documents, media files, code files, and executables.
- Infinite loop ensures continuous monitoring and organization of files.
- Files are either moved or copied based on whether the source and destination are on the same drive.

## Directories and Extensions

The script is organized into sections for different file types. Each section contains the source directories where files are monitored and the target directories where files will be organized based on their extensions.

- Text Files: `.txt`
- PDFs: `.pdf`
- MS Office Documents: `.doc`, `.docx`, `.ppt`, `.pptx`, `.xls`, `.xlsx`, `.mdb`, `.accdb`, `.odt`, `.odp`
- Media Files: `.mp3`, `.mp4`, `.avi`, `.mkv`, `.jpg`, `.png`, `.gif`, `.bmp`, `.webm`, `.svg`
- Code Files: `.py`, `.java`, `.cpp`, `.html`, `.css`, `.js`, `.php`, `.rb`, `.swift`, `.kt`, `.lua`, `.asm`
- Executable Files: `.exe`, `.msi`

## Notes

- Be cautious when using an infinite loop as it can consume system resources. Use this script judiciously.

## License

This project is licensed under the [MIT License](LICENSE).
