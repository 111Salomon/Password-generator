import random
import string
import tkinter as tk
from tkinter import messagebox

# --- Génération du mot de passe ---
def generate_password(length: int) -> str:
    if length < 6:
        raise ValueError("La longueur doit être au moins 6 caractères.")

    all_chars = string.ascii_letters + string.digits + string.punctuation

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)

    return ''.join(password)

# --- Actions des boutons ---
def on_generate():
    try:
        length = int(entry_length.get())
        pwd = generate_password(length)
        result_var.set(pwd)
    except ValueError as e:
        messagebox.showerror("Erreur", str(e))

def on_copy():
    pwd = result_var.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        messagebox.showinfo("✅ Copié", "Mot de passe copié dans le presse-papiers !")
    else:
        messagebox.showwarning("⚠️ Attention", "Aucun mot de passe à copier.")

# --- Interface Tkinter ---
root = tk.Tk()
root.title("🔐 Générateur de mots de passe")
root.geometry("450x300")
root.configure(bg="#1e1e2f")  # fond sombre moderne
root.resizable(False, False)

# Style global
font_title = ("Helvetica", 16, "bold")
font_normal = ("Helvetica", 12)

# Titre
tk.Label(root, text="🔐 Générateur de mots de passe", font=font_title, fg="#FFD700", bg="#1e1e2f").pack(pady=15)

# Zone de saisie longueur
frame_input = tk.Frame(root, bg="#1e1e2f")
frame_input.pack(pady=10)
tk.Label(frame_input, text="Longueur :", font=font_normal, fg="white", bg="#1e1e2f").pack(side="left", padx=5)
entry_length = tk.Entry(frame_input, width=10, font=font_normal, justify="center")
entry_length.pack(side="left")

# Bouton générer
btn_generate = tk.Button(root, text="Générer", font=font_normal, bg="#4CAF50", fg="white",
                         activebackground="#45a049", relief="flat", command=on_generate)
btn_generate.pack(pady=10, ipadx=20, ipady=5)

# Affichage mot de passe
result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, font=("Courier", 14, "bold"), fg="#00BFFF", bg="#1e1e2f").pack(pady=15)

# Bouton copier
btn_copy = tk.Button(root, text="Copier", font=font_normal, bg="#2196F3", fg="white",
                     activebackground="#0b79d0", relief="flat", command=on_copy)
btn_copy.pack(pady=5, ipadx=20, ipady=5)

root.mainloop()
