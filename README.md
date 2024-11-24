# epub-token-counter

# EPUB Token Counter

A Python GUI application that helps you analyze and organize EPUB files based on their token count. This tool is particularly useful for managing large EPUB collections and identifying files that fit within specific token limits.

## Features

- Count tokens in EPUB files using OpenAI's tiktoken library
- Move files under a specified token count to a separate directory
- Generate CSV reports with token counts for all processed files
- Save and restore user preferences
- Progress tracking for batch processing
- Detailed logging for troubleshooting

## Installation

1. Clone the repository
2. Install the package and dependencies:

## Requirements

- Python 3.7+
- PyQt5
- ebooklib
- tiktoken

## Usage

1. Run the application
2. Select the source folder containing your EPUB files
3. Enter the maximum token count threshold
4. Choose a destination folder for files below the threshold
5. Click "Start" to begin processing

The application will:
- Count tokens in each EPUB file
- Generate a CSV report with token counts
- Move files below the threshold to the destination folder
- Display progress and completion status

## Configuration

Settings are automatically saved to `~/.epubtokens_settings.json` and include:
- Last used input folder
- Last used output folder
- Previous token count threshold

## Logging

The application logs operations and errors to `epubtokens.log` in the application directory.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
