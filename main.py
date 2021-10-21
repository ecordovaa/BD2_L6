import os.path
from preprocesamiento.create_book import read_book
from index.builder import build_index

if __name__ == "__main__":
    for i in range(6):
        read_book(i + 1)
    build_index()