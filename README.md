
# Number Converter
![image](https://github.com/user-attachments/assets/b450766f-6e91-422e-ad07-4319c34a3f7f)

## Overview
The Number Converter is a simple GUI application built using Python's Tkinter library. It allows users to convert numbers between different bases: Decimal, Binary, Octal, and Hexadecimal.

## Features
- Convert numbers from one base to another.
- User-friendly interface with dropdown menus for selecting bases.
- Input and output fields for entering and displaying numbers.
- A 'Calculate' button to perform the conversion.

## Requirements
- Python 3.x
- Tkinter library (usually included with Python)

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/ritwickrajmakhal/Number-Converter-using-python.git
    ```
2. Navigate to the project directory:
    ```sh
    cd number_converter
    ```

## Usage
1. Run the application:
    ```sh
    python number_converter.py
    ```
2. Select the base of the input number from the "From" dropdown menu.
3. Select the base to convert to from the "To" dropdown menu.
4. Enter the number in the input field.
5. Click the "Calculate" button to see the converted number in the output field.

## File Structure
- `number_converter.py`: Main script containing the GUI code.
- `main.py`: Contains the `calculate` function which performs the number conversion.

## Example
1. Select "Decimal" from the "From" dropdown menu.
2. Select "Binary" from the "To" dropdown menu.
3. Enter `10` in the input field.
4. Click "Calculate" to see `1010` in the output field.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.
