def hex_to_rgb(hex_code: str) -> str:
    # Extract individual components from the HEX code and convert to decimal
    component_1 = str(int(hex_code[1:3], 16))
    component_2 = str(int(hex_code[3:5], 16))
    component_3 = str(int(hex_code[5:7], 16))

    # Create a list with formatted RGB components
    result = [
        "(r: ",
        component_1,
        ", g: ",
        component_2,
        ", b: ",
        component_3,
        ")",
    ]

    # Join the components to form the final RGB representation
    return "".join(result)


def rgb_to_hex(r: int, g: int, b: int) -> str:
    # Convert decimal RGB components to hexadecimal and format them
    component_1 = format(r, "02X")
    component_2 = format(g, "02X")
    component_3 = format(b, "02X")

    # Combine the components to create the HEX color code
    return "#" + component_1 + component_2 + component_3


def main():
    # Demonstrate RGB to HEX conversion
    print("Function to convert from RGB to HEX")
    print(rgb_to_hex(0, 0, 0))
    print(rgb_to_hex(34, 139, 34))
    print(rgb_to_hex(0, 128, 255))
    print(rgb_to_hex(255, 255, 0))
    print(rgb_to_hex(255, 0, 128))

    # Demonstrate HEX to RGB conversion
    print("Function to convert from HEX to RGB")
    print(hex_to_rgb("#000000"))
    print(hex_to_rgb("#228B22"))
    print(hex_to_rgb("#0080FF"))
    print(hex_to_rgb("#FFFF00"))
    print(hex_to_rgb("#FF0080"))


if __name__ == "__main__":
    # Run the main function if the script is executed
    main()
