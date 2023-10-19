# ColorMorph

ColorMorph is a Python project that provides a set of functions for converting color values between various formats, including Hexadecimal (HEX), Red-Green-Blue (RGB), and Hue-Saturation-Lightness (HSL).

## Features

- Convert color values between HEX, RGB, and HSL formats.
- Handle both single and batch conversions.
- Robust error handling for invalid inputs.

## Getting Started

### Prerequisites

- This project requires Python 3 to run. 
- Colorsys library is needed but it's a part of the Python Standard Library, so you do not need to install it separately.

## Usage

To use the color conversion functions in your Python project, you need to import them:

```python
from colormorph import convert_color
```

Then, you can use the `convert_color` function to convert colors between different formats.

```python
# Example 1: Convert HEX to RGB
input_color = "#FFA500"  # Hex color for orange
input_format = "hex"
output_format = "rgb"
output_color = convert_color(input_color, input_format, output_format)
print(f"Converted color: {output_color}")

# Example 2: Convert RGB to HEX
r, g, b = 255, 69, 0
input_format = "rgb"
output_format = "hex"
output_color = convert_color((r, g, b), input_format, output_format)
print(f"Converted color: {output_color}")
```

## Functions

### `convert_color(input_color, input_format, output_format)`

This function converts color values between different formats:

- `input_color`: The input color value (HEX, RGB, or HSL).
- `input_format`: The format of the input color value ("hex", "rgb", or "hsl").
- `output_format`: The desired output format ("hex", "rgb", or "hsl").

## Color Conversion Examples

### Example 1: HEX to RGB

To convert a HEX color code to RGB format:

```python
input_color = "#FFA500"  # Hex color for orange
input_format = "hex"
output_format = "rgb"
output_color = convert_color(input_color, input_format, output_format)
print(f"Converted color: {output_color}")
```

### Example 2: RGB to HEX

To convert RGB components to a HEX color code:

```python
r, g, b = 255, 69, 0
input_format = "rgb"
output_format = "hex"
output_color = convert_color((r, g, b), input_format, output_format)
print(f"Converted color: {output_color}")
```

### Example 3: HEX to HSL

To convert a HEX color code to HSL format:

```python
input_color = "#0080FF"  # Hex color
input_format = "hex"
output_format = "hsl"
output_color = convert_color(input_color, input_format, output_format)
print(f"Converted color: {output_color}")
```