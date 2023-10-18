import colorsys

def convert_color(input_color, input_format, output_format):
    if input_format not in ("hex", "rgb", "hsl") or output_format not in ("hex", "rgb", "hsl"):
        raise ValueError("Invalid input or output format")

    if input_format == output_format:
        return input_color

    if input_format == "hex":
        # Convert from hex to RGB
        r, g, b = tuple(int(input_color[i:i + 2], 16) for i in (0, 2, 4))
    elif input_format == "rgb":
        # Parse the RGB string
        r, g, b = map(int, input_color.split(","))
    else:
        # Parse the HSL string and convert to RGB
        h, s, l = map(float, input_color.strip('hsl()').split(","))
        r, g, b = [int(255 * x) for x in colorsys.hls_to_rgb(h / 360, l / 100, s / 100)]

    if output_format == "hex":
        # Convert RGB to hex
        return "#{:02X}{:02X}{:02X}".format(r, g, b)
    elif output_format == "rgb":
        # Convert RGB to string
        return f"{r}, {g}, {b}"
    else:
        # Convert RGB to HSL
        h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
        h, s, l = round(h * 360), round(s * 100), round(l * 100)
        return f"hsl({h}, {s}%, {l}%)"

def main():
    # Demonstrate color conversions
    input_color = "FFA500"  # Hex color for orange
    input_format = "hex"
    output_format = "rgb"
    output_color = convert_color(input_color, input_format, output_format)
    print(f"Converted color: {output_color}")

    # You can add more conversion demonstrations here
    # For example:
    # input_color = "rgb(255, 69, 0)"
    # input_format = "rgb"
    # output_format = "hsl"
    # output_color = convert_color(input_color, input_format, output_format)
    # print(f"Converted color: {output_color}")

if __name__ == "__main__":
    main()
