import tkinter as tk
from tkinter import ttk, INSERT,END,font,Toplevel
from tkinter import messagebox as mb
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText




class TextFileComparator:
    def __init__(self, parent):
        self.parent = parent
        self.e1= tk.Entry(self.root,bd=5, width=50)
        self.e1.grid(row=0, column=1, padx=5, pady=5)
        self.e2= tk.Entry(self.root, bd=5,width=50)
        self.e2.grid(row=0, column=4, padx=5, pady=5)
        self.btfr = ttk.Frame(parent, width=10, height=10)
        self.btfr.grid(row=4, column=1)
        self.txtfrm1 = ttk.Frame(self.parent, width=60, height=60)
        self.txtfrm1.grid(row=5, column=1)
        self.txtfrm2 = ttk.Frame(self.parent, width=60, height=60)
        self.txtfrm2.grid(row=6, column=2)
        self.txtfrm3 = ttk.Frame(self.parent, width=50, height=15)
        self.txtfrm3.grid(row=10, column=2, columnspan=4)
        self.text1 = ScrolledText(self.txtfrm1)
        self.text1.grid(row=1, column=1, sticky="nsew")
        self.text2 = ScrolledText(self.txtfrm2)
        self.text2.grid(row=1, column=3, sticky="nsew")
        self.text_content1 = ""
        self.text_content2 
        # Create the output text widget
        self.output_text = tk.Text(self.txtfrm3,bd=5, height=15)
        self.output_text.grid(row=10, column=2, columnspan=2, sticky="nsew")

        # Create a button to load the files
        load_button = tk.Button(self.btfr,bd=5, text="Load Files", command=self.load_files)
        load_button.grid(row=2, column=0, sticky="w")

        # Create a button to compare the files
        compare_button = tk.Button(
            self.btfr, text="Compare", command=self.compare_files
        )
        compare_button.grid(row=3, column=4, sticky="w")

        # Create a button to clear all text widgets
        clear_button = tk.Button(
            self.btfr,bd=5, text="Clear All", command=self.clear_textwidgets
        )
        clear_button.grid(row=4, column=5, sticky="w")
        self.infotxt1 =  TextWidgetInfo(self.txtfrm1, self.text1,0,0)
        self.infotxt2 =  TextWidgetInfo(self.txtfrm2, self.text2,0,2)
        self.outtxtinfo =TextWidgetInfo(self.txtfrm3, self.output_text,10,2)
    def clear_textwidgets(self):
        self.e1.delete(0, tk.END)
        self.e2.delete(0, tk.END)
        self.text1.delete("1.0", tk.END)
        self.text2.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)

    def load_files(self):
        self.e1.delete(0, tk.END)
        self.e2.delete(0, tk.END)
        file1 = filedialog.askopenfilename(title="Select First File")
        if file1:
            self.e1.insert(0, file1)
            with open(file1, "r") as f:
                content1 = f.read()
                self.text1.delete("1.0", tk.END)
                self.text1.insert(tk.END, content1)

        file2 = filedialog.askopenfilename(title="Select Second File")
        if file2:
            self.e2.insert(0, file2)
            with open(file2, "r") as f:
                content2 = f.read()
                self.text2.delete("1.0", tk.END)
                self.text2.insert(tk.END, content2)

    def compare_files(self):
        # Get the content from the text widgets
        content1 = self.text1.get("1.0", tk.END)
        content2 = self.text2.get("1.0", tk.END)

        # Split the content into lines
        lines1 = content1.splitlines()
        lines2 = content2.splitlines()

        # Initialize a counter for differences
        diff_count = 0

        # Clear the text widgets
        self.text1.delete("1.0", tk.END)
        self.text2.delete("1.0", tk.END)

        # Compare the lines and highlight the differences
        diff_line_numbers = []
        for i, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
            if line1 != line2:
                # Increase the difference count
                diff_count += 1
                diff_line_numbers.append(i)

                # Highlight the difference by inserting tags
                self.text1.insert(tk.END, line1 + "\n", "diff")
                self.text2.insert(tk.END, line2 + "\n", "diff")
            else:
                # Insert the lines without any difference
                self.text1.insert(tk.END, line1 + "\n")
                self.text2.insert(tk.END, line2 + "\n")

        # Add the remaining lines, if any
        if len(lines1) > len(lines2):
            for line in lines1[len(lines2) :]:
                self.text1.insert(tk.END, line + "\n")
                diff_count += 1
                diff_line_numbers.append(len(lines2) + 1)
        elif len(lines2) > len(lines1):
            for line in lines2[len(lines1) :]:
                self.text2.insert(tk.END, line + "\n")
                diff_count += 1
                diff_line_numbers.append(len(lines1) + 1)

        # Configure the tag for highlighting differences
        self.text1.tag_configure("diff", background="wheat1")
        self.text2.tag_configure("diff", background="sky blue")

        # Show the difference count and line numbers
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, f"Number of differences: {diff_count}\n")
        self.output_text.insert(tk.END, f"Lines in Text 1: {len(lines1)}\n")
        self.output_text.insert(tk.END, f"Lines in Text 2: {len(lines2)}\n")
        self.output_text.insert(tk.END, "Line numbers with differences: ")
        self.output_text.insert(tk.END, ", ".join(map(str, diff_line_numbers)))
        if not content1 or not text2_path:
            messagebox.showwarning("Input Error", "Please select both text1 and text2 files.")
            return

        try:
            with open(content1_path, 'r') as content1_file:
                content1_strings = set(line.strip() for line in content1_file.readlines())

            with open(text2_path, 'r') as text2_file:
                text2_strings = set(line.strip() for line in text2_file.readlines())

            matched = content1_strings & text2_strings
            unmatched = text2_strings - content1_strings

            self.save_results(matched, unmatched)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def save_results(self, matched, unmatched):
        matched_path = filedialog.asksaveasfilename(defaultextension=".txt", title="Save Matched Results", filetypes=[("Text Files", "*.txt"), ("CSV Files", "*.csv"), ("JSON Files", "*.json"), ("XML Files", "*.xml"), ("All Files", "*.*")])
        if matched_path:
            with open(matched_path, 'w') as matched_file:
                matched_file.write("\n".join(matched))

        unmatched_path = filedialog.asksaveasfilename(defaultextension=".txt", title="Save Unmatched Results", filetypes=[("Text Files", "*.txt"), ("CSV Files", "*.csv"), ("JSON Files", "*.json"), ("XML Files", "*.xml"), ("All Files", "*.*")])
        if unmatched_path:
            with open(unmatched_path, 'w') as unmatched_file:
                unmatched_file.write("\n".join(unmatched))

        messagebox.showinfo("Success", "Files text and results saved.")


    def update_info(self, event=None):
        self.content1 = self.text1.get("1.0", "end-1c")
        self.content2 = self.text2.get("1.0", "end-1c")

      
        
        
        self.contentout = self.textwidget.get("1.0", "end-1c")

        # Count the lines, words, and characters
        self.infotxt1.update()
        self.infotxt2.update()
        self.outtxtinfo.update()
             

    def run(self):
        self.create_gui()
class TextWidgetInfo:
    def __init__(self, parent, textwidget, row, column):
        self.parent = parent
        self.textwidget = textwidget
        self.row = row
        self.column = column
        self.info_label = tk.Label(self.parent, text="Lines: 0 /n" )
        self.info_label2 = tk.Label(self.parent, text="Words: 0   ")|
        self.info_label3 = tk.Label(self.parent, text=" Characters: 0 )")
        self.info_label4 = tk.Label(self.parent, text=" Cursor Position: Line 1")         
        self.info_label.grid(row = self.row, column = self.column)
        self.info_label2.grid(row = self.row + 1, column = self.column)
        self.info_label3.grid(row = self.row +2, column = self.column)
        self.info_label4.grid(row = self.row +3, column = self.column)

        # Bind to text change and cursor movement events
        self.textwidget.bind("<KeyRelease>", self.update_info)
        self.textwidget.bind("<ButtonRelease-1>", self.update_info)
        self.textwidget.bind("<<Modified>>", self.on_text_modified)
        self.textwidget.bind("<ButtonRelease-2>", self.update_info)
    def on_text_modified(self, event):
        if self.textwidget.edit_modified():
            self.update_info(event)
            self.textwidget.edit_modified(False)

    def update_info(self, event=None):
        # Get the current text content
        content = self.textwidget.get("1.0", "end-1c")

        # Count the lines, words, and characters
        lines = self.textwidget.index("end-1c").split(".")[0]
        words = len(content.split())
        characters = len(content)

        # Get the current cursor position (line and column)
        cursor_position = self.textwidget.index("insert")
        cursor_line, cursor_column = cursor_position.split(".")

        # Update the label with the new information
        self.info_label.config(text=f"Lines: {lines}"   \n)
        self.info_label2.config(text= f"Words: {words}       "\n)
        self.info_label3.config(text= f"Characters: {characters}   "  \n)
        self.info_label4.config(text= f"Cursor Position: Line {cursor_line}, Column {cursor_column}" \n)

