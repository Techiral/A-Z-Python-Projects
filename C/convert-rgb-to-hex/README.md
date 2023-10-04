# RGB-HEX Converter

This Python script provides functions to convert between RGB (Red, Green, Blue) and HEX (Hexadecimal) color representations.

## Functions

### RGB to HEX Conversion

```python
def rgb_to_hex(r: int, g: int, b: int) -> str:
    """
    Converts RGB values to HEX format.

    Parameters:
    - r (int): Red component (0-255).
    - g (int): Green component (0-255).
    - b (int): Blue component (0-255).

    Returns:
    str: HEX color code.
    """
```

### HEX to RGB Conversion

```python
def hex_to_rgb(hex_code: str) -> str:
    """
    Converts HEX color code to RGB format.

    Parameters:
    - hex_code (str): HEX color code (e.g., "#RRGGBB").

    Returns:
    str: RGB color representation.
    """
```

## Usage

```python
def main():
    print("Function to convert from RGB to HEX")
    print(rgb_to_hex(0, 0, 0))
    print(rgb_to_hex(34, 139, 34))
    print(rgb_to_hex(0, 128, 255))
    print(rgb_to_hex(255, 255, 0))
    print(rgb_to_hex(255, 0, 128))

    print("Function to convert from HEX to RGB")
    print(hex_to_rgb("#000000"))
    print(hex_to_rgb("#228B22"))
    print(hex_to_rgb("#0080FF"))
    print(hex_to_rgb("#FFFF00"))
    print(hex_to_rgb("#FF0080"))


if __name__ == "__main__":
    main()
```

## How to Run

Simply execute the script, and it will demonstrate the conversion functions with example values.

```bash
python script_name.py
```
