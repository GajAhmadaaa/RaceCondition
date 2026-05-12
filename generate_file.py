import os

def generate_txt_file():
    # Pastikan folder 'GeneratedFile/' ada
    folder_path = 'GeneratedFile/'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Nama file dengan format "data-yyyymmdd-hhmmss.txt"
    from datetime import datetime
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    file_name = f"data-{timestamp}.txt"
    file_path = os.path.join(folder_path, file_name)

    # Konten yang akan ditulis ke file
    content = f"Ini adalah file yang di-generate secara otomatis pada {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}"

    # Menulis konten ke file
    with open(file_path, 'w') as file:
        file.write(content)

    print(f"File berhasil dibuat di: {file_path}")

if __name__ == "__main__":
    generate_txt_file()