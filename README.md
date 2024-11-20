# BookBot Report Generator

This is a simple Python script that processes the text of a book and generates a report, including the number of words and a count of each character found in the text.

## Features
1. **Read File Content**: Reads the content of a file from a given path.
2. **Count Words**: Counts the total number of words in the file.
3. **Character Frequency**: Computes how many times each character appears in the file, ignoring case sensitivity.

## How It Works
The script performs the following steps:
1. Reads the content of the file specified in the `main()` function.
2. Counts the total number of words in the document.
3. Counts the frequency of each character in the document (case-insensitive).
4. Displays a report summarizing the word and character counts.

### Example Report
For the file `books/frankenstein.txt`, the script generates a report similar to the following:

--- Begin report of books/frankenstein.txt ---
84321 words found in the document
The 'a' character was found 7211 times
The 'b' character was found 4312 times
....
The 'z' character was found 22 times
--- End report ---


## File Structure
- `get_file_content(path)`: Reads the content of a file from the given `path`.
- `get_counts_of_words(content)`: Calculates the number of words in the provided content.
- `get_counts_of_character(content)`: Returns a dictionary with the frequency of each character in the content.
- `main()`: The main function orchestrating the flow.

## Usage
1. Ensure you have Python installed on your system.
2. Place the text file you want to analyze at the specified path in the script. By default, the file is located at:
   ```
   /home/<your-abspath>
   ```
   Update the `fpath` variable in the `main()` function if needed.
3. Run the script:
   ```bash
   python3 script_name.py
   ```
   Replace `script_name.py` with the name of your Python script.

## Customization
- **Change File Path**: Update the `fpath` variable in the `main()` function to analyze a different file.
- **Modify Report Format**: Edit the `print` statements in the `main()` function to change the output formatting.

## Requirements
- Python 3.x
- A text file to analyze (e.g., `books/frankenstein.txt`)

## Limitations
- The script does not handle non-existent or inaccessible file paths gracefully.
- Punctuation and whitespace are treated as characters during the character frequency analysis.

## License
This project is open-source and available under the MIT License.

## Author
Developed by **OMONA-EMMANUEL**
