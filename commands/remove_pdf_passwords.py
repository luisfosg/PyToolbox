import os
from PyPDF2 import PdfReader, PdfWriter

def run():
    """
    Removes the password from all PDF files in the specified folder.
    """
    folder_path = input("Enter the folder path: ").strip()
    password = input("Enter the PDF password: ").strip()

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
