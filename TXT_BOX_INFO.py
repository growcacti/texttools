import tkinter as tk

class TextWidgetInfo:
    def __init__(self, parent, textwidget, row, column):
        self.parent = parent
        self.textwidget = textwidget
        self.row = row
        self.column = column
        self.info_label = tk.Label(self.parent, text="Lines: 0  \n 
        self.info_label2 = tk.Label(self.parent, text="Words: 0   \n|
        self.info_label3 = tk.Label(self.parent, text=" Characters: 0 \n
        self.info_label4 = tk.Label(self.parent, text=" Cursor Position: Line 1   , Column 0       ")
           
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

