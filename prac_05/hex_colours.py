"""
Hex Colour Code Lookup
Estimated time: 15 minutes
Actual time: 12 minutes

This program uses a constant dictionary of colour names to hex codes.
Users can enter a colour name (case-insensitive) to look up the hex code.
The loop continues until a blank line is entered.
"""

HEX_COLOURS = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "black": "#000000",
    "blue": "#0000ff",
    "blueviolet": "#8a2be2",
    "brown": "#a52a2a"
}

def main():
    print("Hex Colour Code Lookup")
    colour_name = input("Enter a colour name: ").strip().lower()
    while colour_name != "":
        if colour_name in HEX_COLOURS:
            print(f"The code for {colour_name} is {HEX_COLOURS[colour_name]}")
        else:
            print("Invalid colour name")
        colour_name = input("Enter a colour name: ").strip().lower()

if __name__ == "__main__":
    main()
