import tkinter as tk
import re

# Function to generate a simple regex pattern
def generate_regex(text):
    # Escape special characters in the text
    return re.escape(text)

# Function to test the regex pattern
def test_regex():
    pattern = regex_entry.get()
    test_text = test_text_entry.get("1.0", tk.END)
    try:
        matches = re.findall(pattern, test_text)
        if matches:
            result_label.config(text=f"Matches: {matches}")
        else:
            result_label.config(text="No match found.")
    except re.error as e:
        result_label.config(text=f"Invalid regex: {e}")

# Function to handle regex generation based on input text
def on_generate_regex():
    text = word_entry.get()
    regex = generate_regex(text)
    generated_regex_label.config(text=regex)

# Main window
root = tk.Tk()
root.title("Regex Generator and Tester")

# Layout using grid
tk.Label(root, text="Enter word or sentence:").grid(row=0, column=0, sticky="e")
word_entry = tk.Entry(root, width=40)
word_entry.grid(row=0, column=1)

tk.Button(root, text="Generate Regex", command=on_generate_regex).grid(row=1, column=1, pady=5)

tk.Label(root, text="Generated Regex:").grid(row=2, column=0, sticky="e")
generated_regex_label = tk.Label(root, text="")
generated_regex_label.grid(row=2, column=1)

tk.Label(root, text="Enter custom Regex for testing:").grid(row=3, column=0, sticky="e")
regex_entry = tk.Entry(root, width=40)
regex_entry.grid(row=3, column=1)

tk.Label(root, text="Text to test Regex:").grid(row=4, column=0, sticky="ne")
test_text_entry = tk.Text(root, height=5, width=40)
test_text_entry.grid(row=4, column=1)

tk.Button(root, text="Test Regex", command=test_regex).grid(row=5, column=1, pady=5)

result_label = tk.Label(root, text="")
result_label.grid(row=6, column=1)

# Start the main loop
root.mainloop()
