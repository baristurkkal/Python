# logs.txt dosyasından "error" içeren satırları ayıklama

def extract_error_lines(file_path):
    errors = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if "error" in line.lower():  # küçük/büyük harf farkını yok saymak için
                errors.append(line.strip())
    return errors


# Kullanım
file_path = "logs.txt"  # buraya kendi dosya yolunu yaz
error_lines = extract_error_lines(file_path)

print("Error satırları:")
for err in error_lines:
    print(err)

