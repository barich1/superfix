# SuperFix

SuperFix is a Python program designed to synchronize files and folders across multiple Windows devices, ensuring that your data is always up-to-date. This tool is particularly useful for users who frequently switch between different devices and need to maintain consistent data.

## Features

- Synchronizes files from a source directory to multiple target directories.
- Preserves file metadata during synchronization.
- Efficiently checks file integrity using MD5 hashes to avoid unnecessary copying.
- Automatically creates target directories if they do not exist.

## Installation

1. Ensure you have Python installed on your Windows device. You can download it from [python.org](https://www.python.org/downloads/).
2. Clone or download this repository to your local machine.

## Usage

1. Open `superfix.py` in a text editor.
2. Modify the `source_directory` and `target_directories` in the `if __name__ == "__main__":` block to specify your source and target directories.
3. Run the script using the command:
   ```
   python superfix.py
   ```

## Example

```python
if __name__ == "__main__":
    source_directory = "C:/path/to/source"
    target_directories = [
        "C:/path/to/target1",
        "C:/path/to/target2",
    ]
    
    superfix = SuperFix(source_directory, target_directories)
    superfix.run()
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgments

This project uses Python's built-in libraries for file handling and hashing.