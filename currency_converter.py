import tkinter as tk
from tkinter import scrolledtext, ttk

# --- Global Variables for Converter Logic ---
from_currency_selected = None
to_currency_selected = None
recent_conversions = []
MAX_HISTORY_LINES = 3

# --- Exchange Rate Data (Simulated for this example) ---
EXCHANGE_RATES = {
    "USD": 1.0,
    "EUR": 0.92,
    "GBP": 0.79,
    "JPY": 155.0,
    "INR": 83.5,
    "AUD": 1.50,
    "CAD": 1.37,
    "CHF": 0.90,
    "CNY": 7.25,
    "BRL": 5.20,
    "ZAR": 18.50,
}
AVAILABLE_CURRENCIES = sorted(list(EXCHANGE_RATES.keys()))
BASE_CURRENCY = "USD"

# --- Theme Variables ---
current_theme = "light"

# Define color palettes for both themes
# Light Theme Colors (Calculator-inspired, with refined accent)
LIGHT_BG_COLOR = "#F0F0F0"         # Overall window background
LIGHT_DISPLAY_COLOR = "#FFFFFF"     # Amount input and result display background
LIGHT_HISTORY_BG_COLOR = "#FFFFFF"  # Background for the small history label
LIGHT_TEXT_COLOR = "#333333"       # General text color
LIGHT_BUTTON_BG_COLOR = "#FFFFFF"   # Base button background (for inputs, like numbers in calculator)
LIGHT_OPERATOR_BG_COLOR = "#F8F8F8" # Background for Theme and Swap buttons (like operators in calculator)
LIGHT_CONVERT_BUTTON_BG_COLOR = "#4285F4" # MODERN BLUE for main conversion button
LIGHT_CONVERT_BUTTON_FG_COLOR = "#FFFFFF" # White text for convert button
LIGHT_CLEAR_BG_COLOR = "#F8F8F8"    # Background for Clear All button
LIGHT_ACTIVE_BG_COLOR = "#DDDDDD"  # Color when a general button is pressed
LIGHT_CONVERT_ACTIVE_BG_COLOR = "#3367D6" # Darker blue when convert button is pressed

# Dark Theme Colors (Remains unchanged)
DARK_BG_COLOR = "#2B2B2B"
DARK_DISPLAY_COLOR = "#1C1C1C"
DARK_HISTORY_BG_COLOR = "#222222"
DARK_TEXT_COLOR = "#E0E0E0"
DARK_BUTTON_BG_COLOR = "#444444"
DARK_OPERATOR_BG_COLOR = "#555555"
DARK_CONVERT_BUTTON_BG_COLOR = "#28a745"
DARK_CONVERT_BUTTON_FG_COLOR = "#FFFFFF"
DARK_CLEAR_BG_COLOR = "#666666"
DARK_ACTIVE_BG_COLOR = "#666666"
DARK_CONVERT_ACTIVE_BG_COLOR = "#218838"

# --- Font Settings ---
HISTORY_FONT = ("Segoe UI", 10)
DISPLAY_FONT = ("Segoe UI", 24, "bold")
BUTTON_FONT = ("Segoe UI", 16)
CURRENCY_LABEL_FONT = ("Segoe UI", 14)
AMOUNT_INPUT_FONT = ("Segoe UI", 20)

# --- Converter Logic Functions ---

def get_rate(currency_code):
    return EXCHANGE_RATES.get(currency_code, None)

def convert_currency():
    try:
        amount = float(amount_input.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()

        if not from_currency or not to_currency:
            result_label.config(text="Select currencies!", fg="red")
            return
        if from_currency not in EXCHANGE_RATES or to_currency not in EXCHANGE_RATES:
            result_label.config(text="Invalid currency!", fg="red")
            return

        from_rate = get_rate(from_currency)
        to_rate = get_rate(to_currency)

        if from_rate is None or to_rate is None:
            result_label.config(text="Rate unavailable!", fg="red")
            return

        amount_in_base = amount / from_rate
        converted_amount = amount_in_base * to_rate

        formatted_result = f"{converted_amount:,.2f} {to_currency}"
        result_label.config(text=formatted_result, fg=get_current_text_color())

        log_conversion(amount, from_currency, converted_amount, to_currency)

    except ValueError:
        result_label.config(text="Enter valid amount!", fg="red")
    except Exception as e:
        result_label.config(text=f"Error: {e}", fg="red")
        print(f"Conversion error: {e}")

def log_conversion(amount, from_cur, converted_amount, to_cur):
    global recent_conversions
    new_entry = f"{amount:,.2f} {from_cur} = {converted_amount:,.2f} {to_cur}"
    recent_conversions.append(new_entry)

    if len(recent_conversions) > MAX_HISTORY_LINES:
        recent_conversions = recent_conversions[-MAX_HISTORY_LINES:]

    recent_conversions_var.set("\n".join(recent_conversions))

def clear_all_inputs():
    global recent_conversions
    amount_input.delete(0, tk.END)
    amount_input.insert(0, "1.00")
    result_label.config(text="Result:", fg=get_current_text_color())
    
    recent_conversions = []
    recent_conversions_var.set("")

def swap_currencies():
    temp_from = from_currency_var.get()
    temp_to = to_currency_var.get()
    from_currency_var.set(temp_to)
    to_currency_var.set(temp_from)

# --- Theme Management ---

def get_current_text_color():
    return LIGHT_TEXT_COLOR if current_theme == "light" else DARK_TEXT_COLOR

def toggle_theme():
    global current_theme
    if current_theme == "light":
        current_theme = "dark"
        apply_theme(DARK_BG_COLOR, DARK_DISPLAY_COLOR, DARK_HISTORY_BG_COLOR,
                    DARK_TEXT_COLOR, DARK_BUTTON_BG_COLOR, DARK_OPERATOR_BG_COLOR,
                    DARK_CONVERT_BUTTON_BG_COLOR, DARK_CONVERT_BUTTON_FG_COLOR, DARK_CLEAR_BG_COLOR,
                    DARK_ACTIVE_BG_COLOR, DARK_CONVERT_ACTIVE_BG_COLOR)
    else:
        current_theme = "light"
        apply_theme(LIGHT_BG_COLOR, LIGHT_DISPLAY_COLOR, LIGHT_HISTORY_BG_COLOR,
                    LIGHT_TEXT_COLOR, LIGHT_BUTTON_BG_COLOR, LIGHT_OPERATOR_BG_COLOR,
                    LIGHT_CONVERT_BUTTON_BG_COLOR, LIGHT_CONVERT_BUTTON_FG_COLOR, LIGHT_CLEAR_BG_COLOR,
                    LIGHT_ACTIVE_BG_COLOR, LIGHT_CONVERT_ACTIVE_BG_COLOR)

def apply_theme(bg, display_bg, history_bg, text_fg, btn_bg, op_btn_bg, convert_btn_bg, convert_btn_fg, clear_btn_bg, active_bg, convert_active_bg):
    root.config(bg=bg)
    recent_conversions_label.config(bg=history_bg, fg=text_fg)

    amount_label.config(bg=bg, fg=text_fg)
    amount_input.config(bg=display_bg, fg=text_fg)
    from_currency_label.config(bg=bg, fg=text_fg)
    to_currency_label.config(bg=bg, fg=text_fg)
    result_label.config(bg=display_bg, fg=text_fg)

    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", fieldbackground=display_bg, background=op_btn_bg,
                    foreground=text_fg, selectbackground=op_btn_bg, selectforeground=text_fg,
                    bordercolor=op_btn_bg, arrowcolor=text_fg)
    style.map('TCombobox',
              fieldbackground=[('readonly', display_bg)],
              background=[('readonly', op_btn_bg)],
              foreground=[('readonly', text_fg)],
              selectbackground=[('readonly', op_btn_bg)],
              selectforeground=[('readonly', text_fg)],
              bordercolor=[('readonly', op_btn_bg)],
              arrowcolor=[('readonly', text_fg)])

    for btn_name, btn_widget in button_widgets.items():
        if btn_name == 'Convert':
            btn_widget.config(bg=convert_btn_bg, fg=convert_btn_fg, activebackground=convert_active_bg)
        elif btn_name == 'Clear All':
            btn_widget.config(bg=clear_btn_bg, fg=text_fg, activebackground=active_bg)
        elif btn_name == 'Theme':
            btn_widget.config(bg=op_btn_bg, fg=text_fg, activebackground=active_bg)
        elif btn_name == '↔':
            btn_widget.config(bg=op_btn_bg, fg=text_fg, activebackground=active_bg)

# --- GUI Setup ---
root = tk.Tk()
root.title("Currency Converter")

initial_width = 400
initial_height = 600
root.geometry(f"{initial_width}x{initial_height}")
root.minsize(initial_width, initial_height)
root.configure(bg=LIGHT_BG_COLOR)

aspect_ratio = initial_width / initial_height

def _on_resize(event):
    if root.state() == 'normal':
        current_width = event.width
        current_height = event.height

        if current_width / current_height > aspect_ratio:
            new_width = int(current_height * aspect_ratio)
            root.geometry(f"{new_width}x{current_height}")
        else:
            new_height = int(current_width / aspect_ratio)
            root.geometry(f"{current_width}x{new_height}")

root.bind("<Configure>", _on_resize)


# --- Layout Components ---

# 1. Limited History Display Area (Row 0)
recent_conversions_var = tk.StringVar(root)
recent_conversions_label = tk.Label(root, textvariable=recent_conversions_var,
                                     font=HISTORY_FONT, anchor="e", justify="right",
                                     bg=LIGHT_HISTORY_BG_COLOR, fg=LIGHT_TEXT_COLOR,
                                     padx=10, pady=5)
recent_conversions_label.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=(10, 0))

# 2. Amount Input Section (Row 1)
amount_label = tk.Label(root, text="Amount:", font=CURRENCY_LABEL_FONT, bg=LIGHT_BG_COLOR, fg=LIGHT_TEXT_COLOR)
amount_label.grid(row=1, column=0, sticky="w", padx=(10, 0), pady=(10, 5))

amount_input = tk.Entry(root, font=AMOUNT_INPUT_FONT, borderwidth=0, relief="flat", justify="right",
                        bg=LIGHT_DISPLAY_COLOR, fg=LIGHT_TEXT_COLOR, highlightthickness=0)
amount_input.grid(row=1, column=1, columnspan=3, sticky="nsew", padx=(0, 10), pady=(10, 5))
amount_input.insert(0, "1.00")

# 3. Currency Selection Dropdowns and Swap Button (Rows 2 & 3)
from_currency_label = tk.Label(root, text="From:", font=CURRENCY_LABEL_FONT, bg=LIGHT_BG_COLOR, fg=LIGHT_TEXT_COLOR)
from_currency_label.grid(row=2, column=0, sticky="w", padx=(10, 0), pady=5)

from_currency_var = tk.StringVar(root)
from_currency_var.set("USD")

from_currency_dropdown = ttk.Combobox(root, textvariable=from_currency_var, values=AVAILABLE_CURRENCIES,
                                      font=CURRENCY_LABEL_FONT, state="readonly")
from_currency_dropdown.grid(row=2, column=1, columnspan=1, sticky="nsew", padx=(0, 5), pady=5)

swap_button = tk.Button(root, text="↔", font=BUTTON_FONT, command=swap_currencies,
                        bg=LIGHT_OPERATOR_BG_COLOR, fg=LIGHT_TEXT_COLOR,
                        activebackground=LIGHT_ACTIVE_BG_COLOR, relief="flat", bd=0)
swap_button.grid(row=2, column=2, sticky="nsew", padx=3, pady=3) # Consistent button padding

to_currency_label = tk.Label(root, text="To:", font=CURRENCY_LABEL_FONT, bg=LIGHT_BG_COLOR, fg=LIGHT_TEXT_COLOR)
to_currency_label.grid(row=2, column=3, sticky="w", padx=(0, 0), pady=5)

to_currency_var = tk.StringVar(root)
to_currency_var.set("INR")

to_currency_dropdown = ttk.Combobox(root, textvariable=to_currency_var, values=AVAILABLE_CURRENCIES,
                                    font=CURRENCY_LABEL_FONT, state="readonly")
to_currency_dropdown.grid(row=3, column=0, columnspan=4, sticky="nsew", padx=10, pady=5)

# 4. Result Display Label (Row 4)
result_label = tk.Label(root, text="Result:", font=DISPLAY_FONT, anchor="e", padx=10, pady=10,
                        bg=LIGHT_DISPLAY_COLOR, fg=LIGHT_TEXT_COLOR, relief="flat", borderwidth=0)
result_label.grid(row=4, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)


# --- Control Buttons (Rows 5 & 6) ---
buttons_data = [
    ('Convert', 5, 0, 4, 'convert'),
    ('Clear All', 6, 0, 2, 'clear'),
    ('Theme', 6, 2, 2, 'theme'),
]

# Configure grid row weights for ~10:90 ratio (Limited History:Converter Tool)
root.grid_rowconfigure(0, weight=10) # Limited history display (smaller)
root.grid_rowconfigure(1, weight=15) # Amount input
root.grid_rowconfigure(2, weight=15) # From/Swap
root.grid_rowconfigure(3, weight=15) # To dropdown
root.grid_rowconfigure(4, weight=25) # Result display (prominent)
root.grid_rowconfigure(5, weight=15) # Convert button
root.grid_rowconfigure(6, weight=5)  # Clear/Theme buttons

for i in range(4): # All 4 columns expand equally
    root.grid_columnconfigure(i, weight=1)

button_widgets = {}
button_widgets['↔'] = swap_button # Add swap button to the dictionary for theme application

for (text, r, c, cs, btn_type) in buttons_data:
    button_command = None
    button_bg = LIGHT_BUTTON_BG_COLOR
    button_fg = LIGHT_TEXT_COLOR
    active_bg = LIGHT_ACTIVE_BG_COLOR

    if btn_type == 'convert':
        button_command = convert_currency
        button_bg = LIGHT_CONVERT_BUTTON_BG_COLOR
        button_fg = LIGHT_CONVERT_BUTTON_FG_COLOR
        active_bg = LIGHT_CONVERT_ACTIVE_BG_COLOR
    elif btn_type == 'clear':
        button_command = clear_all_inputs
        button_bg = LIGHT_CLEAR_BG_COLOR
    elif btn_type == 'theme':
        button_command = toggle_theme
        button_bg = LIGHT_OPERATOR_BG_COLOR

    btn = tk.Button(root, text=text, font=BUTTON_FONT, command=button_command,
                    bg=button_bg, fg=button_fg, activebackground=active_bg,
                    relief="flat", bd=0)
    btn.grid(row=r, column=c, columnspan=cs, sticky="nsew", padx=3, pady=3) # Consistent button padding
    button_widgets[text] = btn

# Initial theme application
apply_theme(LIGHT_BG_COLOR, LIGHT_DISPLAY_COLOR, LIGHT_HISTORY_BG_COLOR,
            LIGHT_TEXT_COLOR, LIGHT_BUTTON_BG_COLOR, LIGHT_OPERATOR_BG_COLOR,
            LIGHT_CONVERT_BUTTON_BG_COLOR, LIGHT_CONVERT_BUTTON_FG_COLOR, LIGHT_CLEAR_BG_COLOR,
            LIGHT_ACTIVE_BG_COLOR, LIGHT_CONVERT_ACTIVE_BG_COLOR)

root.mainloop()