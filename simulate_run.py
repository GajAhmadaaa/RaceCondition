import time
from datetime import datetime
from generate_file import generate_txt_file

if __name__ == "__main__":
    # Simulasi perbedaan beberapa milidetik
    generate_txt_file()
    print(f"File pertama dibuat pada: {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}")
    time.sleep(0.01)
    generate_txt_file()
    print(f"File kedua dibuat pada: {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}")