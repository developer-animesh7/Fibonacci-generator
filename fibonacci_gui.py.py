import tkinter as tk

def fibonacci_generator(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def generate_fibonacci():
    try:
        n = int(entry.get())
        if n <= 0:
            raise ValueError("Input must be a positive integer")
        sequence = fibonacci_generator(n)
        result_text = ', '.join(map(str, sequence))
        result_label.config(text=result_text)
        result_label.update_idletasks()
        result_textbox.delete("1.0", tk.END)
        result_textbox.insert(tk.END, result_text)
    except ValueError as e:
        result_label.config(text=f"Error: {e}")

# Create the main window
root = tk.Tk()
root.title("Fibonacci Generator")
root.geometry("500x300")  # Set the window size

# Create and place the input field
entry_label = tk.Label(root, text="Enter number of terms:")
entry_label.pack()
entry = tk.Entry(root)
entry.pack()

# Create and place the generate button
generate_button = tk.Button(root, text="Generate", command=generate_fibonacci)
generate_button.pack()

# Create and place the result label
result_label = tk.Label(root, text="")
result_label.pack()

# Create a Text widget to display the result in a larger, scrollable area
result_textbox = tk.Text(root, wrap=tk.WORD, height=10, width=40)
result_textbox.pack()

# Start the Tkinter event loop
root.mainloop()
