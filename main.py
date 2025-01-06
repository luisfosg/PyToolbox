import os
from PyPDF2 import PdfReader, PdfWriter

def remove_pdf_passwords(folder_path, password):
    """
    Removes the password from all PDF files in the specified folder.

    Parameters:
    folder_path (str): Path to the folder containing the PDF files.
    password (str): Password to unlock the PDF files.
    """
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            try:
                reader = PdfReader(file_path)

                if reader.is_encrypted:
                    reader.decrypt(password)

                writer = PdfWriter()
                for page in reader.pages:
                    writer.add_page(page)

                with open(file_path, "wb") as output_pdf:
                    writer.write(output_pdf)

                print(f"Password removed from: {filename}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

if __name__ == "__main__":
    folder = input("Enter the folder path: ").strip()
    pdf_password = input("Enter the PDF password: ").strip()
    remove_pdf_passwords(folder, pdf_password)
