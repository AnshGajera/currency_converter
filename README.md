Python Currency Converter
This is a simple and modern currency converter application built using Python and the Tkinter library. It allows users to convert amounts between various currencies, view a limited history of recent conversions, and switch between light and dark themes.

Features:
Real-time Conversion (Simulated): Converts amounts based on a predefined set of exchange rates. (Can be extended to fetch live rates from an API).

Limited Conversion History: Displays the last 3 conversions directly on the main interface.

Dynamic Theming: Toggle between a clean light theme (inspired by Windows Calculator) and a sleek dark theme.

Intuitive UI: User-friendly interface with input fields, dropdowns for currency selection, and clear result display.

Swap Currencies: Easily switch the "From" and "To" currencies with a single button.

Clear Functionality: Reset inputs and clear the conversion history.

Fixed Aspect Ratio: The application window maintains its proportions when resized or maximized, ensuring a consistent look.

Technologies Used:
Python 3.x

Tkinter: Python's standard GUI (Graphical User Interface) library.

tkinter.ttk: Themed Tkinter widgets for a more modern look (e.g., Combobox for dropdowns).

How to Run:
Prerequisites:

Ensure you have Python 3.x installed on your system.

Tkinter is usually included with standard Python installations. If you encounter a ModuleNotFoundError related to tkinter, you might need to install it:

On Debian/Ubuntu: sudo apt-get install python3-tk

On Fedora/RHEL: sudo dnf install python3-tkinter

On macOS: Tkinter should be part of the Python installation from python.org.

Clone the Repository:
Open your terminal or command prompt and clone this repository:

git clone https://github.com/AnshGajera/currency_converter.git
cd currency_converter

Run the Application:
Execute the Python script:

python currency_converter.py

(Depending on your Python setup, you might need to use python3 currency_converter.py instead.)

Usage:
Enter the amount you wish to convert in the "Amount:" field.

Select the source currency from the "From:" dropdown.

Select the target currency from the "To:" dropdown.

Click the "Convert" button to see the result.

The recent conversions will appear at the top of the window.

Use the "↔" (Swap) button to quickly interchange the selected "From" and "To" currencies.

Click "Clear All" to reset the input and clear the history.

Click "Theme" to switch between light and dark modes.

Screenshots:
![image](https://github.com/user-attachme![image](https://github.com/user-attachments/assets/0523ba9f-b740-4adb-9234-c112caae35fe)
nts/assets/70363128-7b80-48c4-974c-2c86c261b4e4)

![Uploading image.png…]()

Future Enhancements:
Integrate with a real-time exchange rate API (e.g., ExchangeRate-API, FreeCurrencyAPI) to get up-to-date rates.

Add more currencies to the EXCHANGE_RATES dictionary.

Implement input validation to ensure only numbers are entered in the amount field.

Add a feature to copy the result to the clipboard.

Contributing:
Contributions are welcome! If you have suggestions for improvements or new features, feel free to:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeatureName).

Make your changes.

Commit your changes (git commit -m 'Add YourFeatureName').

Push to the branch (git push origin feature/YourFeatureName).

Open a Pull Request.

License:
This project is open-source and available under the MIT License. See the LICENSE file for more details.
