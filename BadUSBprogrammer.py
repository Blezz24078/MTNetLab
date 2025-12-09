# safe_hid_generator.py

# Ask the user for key inputs
user_input = input("Enter keys (example: w a s d): ").strip()
keys = user_input.split()

# Begin building the Arduino sketch
arduino_code = [
    "#include <Keyboard.h>",
    "",
    "void setup() {",
    "    Keyboard.begin();",
    "}",
    "",
    "void loop() {"
]

for key in keys:
    arduino_code.append(f"    Keyboard.press('{key}');")
    arduino_code.append("    delay(100);")
    arduino_code.append(f"    Keyboard.release('{key}');")
    arduino_code.append("    delay(1000);")
    arduino_code.append("")  # spacer line for readability

arduino_code.append("}")  # properly close loop()

# Output final code
print("\nGenerated Arduino Code:\n")
print("\n".join(arduino_code))
