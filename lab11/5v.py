import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime

def add_expense():
    expense = entry_expense.get()
    amount = entry_amount.get()
    category = category_var.get()
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    expenses.append((date, expense, category, amount))

    entry_expense.delete(0, tk.END)
    entry_amount.delete(0, tk.END)

    update_expenses_list()

def update_expenses_list():
    listbox_expenses.delete(0, tk.END)
    for date, expense, category, amount in expenses:
        listbox_expenses.insert(tk.END, f"{date}: {category} - {expense} - {amount} руб.")

def clear_expenses():
    expenses.clear()
    listbox_expenses.delete(0, tk.END)

def show_summary():
    total = sum(float(amount) for _, _, _, amount in expenses)

    summary_window = tk.Toplevel(root)
    summary_window.title("Сводка расходов")

    categories = ["Еда", "Транспорт", "Жилье", "Развлечения", "Здоровье"]
    for category in categories:
        category_total = sum(float(amount) for _, _, cat, amount in expenses if cat == category)
        ttk.Label(summary_window, text=f"{category}: {category_total} руб.").pack()

    ttk.Label(summary_window, text=f"Общая сумма расходов: {total} руб.").pack()
    ttk.Button(summary_window, text="Закрыть", command=summary_window.destroy).pack()

root = tk.Tk()
root.title("Финансовый трекер расходов")

root.columnconfigure(1, weight=1)
root.rowconfigure(7, weight=1)  # Увеличили количество строк, чтобы разместить сводку и список расходов

label_expense = ttk.Label(root, text="Расход:")
label_expense.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

entry_expense = ttk.Entry(root)
entry_expense.grid(row=0, column=1, padx=5, pady=5, sticky="we")

label_amount = ttk.Label(root, text="Сумма:")
label_amount.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

entry_amount = ttk.Entry(root)
entry_amount.grid(row=1, column=1, padx=5, pady=5, sticky="we")

label_category = ttk.Label(root, text="Категория:")
label_category.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

category_var = tk.StringVar(root)
categories = ["Еда", "Транспорт", "Жилье", "Развлечения", "Здоровье"]
category_dropdown = ttk.Combobox(root, textvariable=category_var, values=categories)
category_dropdown.grid(row=2, column=1, padx=5, pady=5, sticky="we")
category_dropdown.current(0)

button_add = ttk.Button(root, text="Добавить", command=add_expense)
button_add.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")

button_summary = ttk.Button(root, text="Сводка", command=show_summary)
button_summary.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

button_clear = ttk.Button(root, text="Очистить", command=clear_expenses)
button_clear.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")

label_expenses = ttk.Label(root, text="Список расходов:")
label_expenses.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W)

listbox_expenses = tk.Listbox(root)
listbox_expenses.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="news")

root.mainloop()
