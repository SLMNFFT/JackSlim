import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from scipy.io import arff

class CSVToARFFConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV to ARFF Converter")

        self.choose_file_button = tk.Button(self.root, text="Choose CSV File", command=self.choose_csv_file)
        self.choose_file_button.pack(pady=10)

    def choose_csv_file(self):
        csv_file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if csv_file_path:
            arff_file_path = filedialog.asksaveasfilename(defaultextension=".arff", filetypes=[("ARFF Files", "*.arff")])

            if arff_file_path:
                self.convert_to_arff(csv_file_path, arff_file_path)
                messagebox.showinfo("Conversion Successful", f"CSV file '{csv_file_path}' has been successfully converted to ARFF format and saved to '{arff_file_path}'.")

    def convert_to_arff(self, csv_file_path, arff_file_path):
        df = pd.read_csv(csv_file_path)
        arff_data = df.values.tolist()
        attribute_names = list(df.columns)
        relation_name = "CSVToARFFConverter"

        arff_header = f"@relation {relation_name}\n\n"
        for attribute in attribute_names:
            arff_header += f"@attribute {attribute} numeric\n"
        arff_header += "\n@data\n"

        arff_content = arff_header + "\n".join(",".join(str(value) for value in row) for row in arff_data)

        with open(arff_file_path, 'w') as arff_file:
            arff_file.write(arff_content)

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVToARFFConverterApp(root)
    root.mainloop()

