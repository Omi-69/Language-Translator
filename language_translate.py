from deep_translator import GoogleTranslator
from tkinter import *
from tkinter import messagebox


def translate_function():
    src_v = src_entry.get("1.0", "end-1c").strip().lower()
    dest_v = dest_entry.get("1.0", "end-1c").strip().lower()

    text_v = text_entry.get("1.0", "end-1c").strip()
    if not text_v:
        messagebox.showerror("Error", "Please enter text to translate.")
        return

    if not dest_v:
        dest_v = "en"

    try:

        translated_text = GoogleTranslator(
            source=src_v if src_v else 'auto', target=dest_v).translate(text_v)
        messagebox.showinfo("Translated Text", translated_text)
    except Exception as e:
        messagebox.showerror("Translation Error",
                             f"An error occurred: {str(e)}")


def clear():
    text_entry.delete("1.0", "end-1c")
    src_entry.delete("1.0", "end-1c")
    dest_entry.delete("1.0", "end-1c")


window = Tk()
window.geometry("500x350")
window.title("Language Translator")


title_label = Label(
    window, text="Language Translator Using Python", font=("Arial", 14, "bold"))
title_label.pack(pady=10)


text_label = Label(window, text="Text to translate:")
text_label.place(x=10, y=50)
text_entry = Text(window, width=40, height=5, font=("Arial", 12), wrap=WORD)
text_entry.place(x=150, y=50)


src_label = Label(window, text="Source language (auto-detect if empty):")
src_label.place(x=10, y=150)
src_entry = Text(window, width=20, height=1, font=("Arial", 12))
src_entry.place(x=300, y=150)


dest_label = Label(window, text="Target language (default: English):")
dest_label.place(x=10, y=180)
dest_entry = Text(window, width=20, height=1, font=("Arial", 12))
dest_entry.place(x=300, y=180)


button1 = Button(window, text='Translate', bg='light green',
                 command=translate_function, font=("Arial", 12))
button1.place(x=150, y=230)
button2 = Button(window, text='Clear', bg='light coral',
                 command=clear, font=("Arial", 12))
button2.place(x=280, y=230)


instruction_label = Label(
    window, text="Note: Use ISO 639-1 language codes (e.g., 'en' for English, 'fr' for French)", font=("Arial", 10), fg="gray")
instruction_label.place(x=50, y=280)


window.mainloop()
