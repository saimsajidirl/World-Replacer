import tkinter as tk

def replace_word(text, old_word, new_word):
    lines = text.split('\n')

    for i in range(len(lines)):
        words = lines[i].split()
        for j in range(len(words)):
            if words[j] == old_word:
                words[j] = new_word

        lines[i] = ' '.join(words)

    modified_text = '\n'.join(lines)

    return modified_text

def replace_and_update():
    old_word = input_old_word.get()
    new_word = input_new_word.get()

    if old_word and new_word:
        user_text = textbox.get("1.0", tk.END)
        result_text = replace_word(user_text, old_word, new_word)

        textbox.delete("1.0", tk.END)
        textbox.insert(tk.END, result_text)

        replaced_word_label.config(text=f"Replaced word: {new_word}")

        # Clear entry fields for a better user experience
        input_old_word.delete(0, tk.END)
        input_new_word.delete(0, tk.END)
    else:
        replaced_word_label.config(text="Please enter both old and new words.")

root = tk.Tk()

instruction_label = tk.Label(root, text=" In The First Text Box Add the word that you want to replace and in the Second Box add the word you want to have in the string after replacing The Word")
instruction_label.pack(pady=10)

textbox = tk.Text(root, font=("arial", 14), wrap="word")
textbox.pack(expand=True, fill="both")

scrollbar_y = tk.Scrollbar(root, command=textbox.yview)
scrollbar_y.pack(side="right", fill="y")
textbox.config(yscrollcommand=scrollbar_y.set)

scrollbar_x = tk.Scrollbar(root, command=textbox.xview, orient="horizontal")
scrollbar_x.pack(side="bottom", fill="x")
textbox.config(xscrollcommand=scrollbar_x.set)

input_old_word = tk.Entry(root, width=20)
input_old_word.pack(pady=5)

input_new_word = tk.Entry(root, width=20)
input_new_word.pack(pady=5)

replace_button = tk.Button(root, text="Update", command=replace_and_update)
replace_button.pack()

replaced_word_label = tk.Label(root, text="")
replaced_word_label.pack()

tk.mainloop()
