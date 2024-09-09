# PDF/EPUB File Organizer Alphabetically 

A Python script to organize and move PDF and EPUB files from a source folder to a destination folder. The script ensures that only these file types are considered and sorts them alphabetically before moving them.

## Features

- **Filters Files**: Moves only PDF and EPUB files.
- **Sorts Files**: Files are sorted alphabetically before moving.
- **Creates Destination Folder**: Automatically creates the destination folder if it doesn't exist.

## Requirements

- Python 3.12
- Standard Python libraries (`os`, `shutil`)

## Usage

1. **Clone the Repository**

   ```sh
   git clone https://github.com/Marwan-khadem9/Python-Script-to-Organize-PDFePUB-files-Alphabetically.git

2. **Navigate to the Script Directory**

   ```sh
   cd Python-Script-to-Organize-PDFePUB-files-Alphabetically
   
3. **Edit the Script**

   Open the script (organize_files.py) and set your source and destination folder paths:

   ```sh
    source_folder = "path/to/your/source/folder"
    destination_folder = "path/to/your/destination/folder"

4. **Run the Script**

   Execute the script using Python:

   ```sh
    python organize_files.py
   
The script will move all PDF and EPUB files from the source folder to the destination folder, sorting them alphabetically.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -am 'Add new feature').
5. Push to the branch (git push origin feature-branch).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

This script uses Python's standard libraries os and shutil.

Make sure to replace `https://github.com/Marwan-khadem9/Python-Script-to-Organize-PDFePUB-files-Alphabetically.git` with the actual URL of your repository and adjust any other placeholders accordingly.
