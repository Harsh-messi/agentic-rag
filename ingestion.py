import os

def load_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def chunk_text(text, chunk_size=400, overlap=80):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap

    return chunks


def load_all_docs(folder_path="data"):
    all_chunks = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            path = os.path.join(folder_path, file_name)

            text = load_txt(path)
            chunks = chunk_text(text)

            for c in chunks:
                all_chunks.append({
                    "text": c,
                    "source": file_name
                })

    return all_chunks