from pathlib import Path

from src.data_loader import load_all_documents


def main():
    data_dir = Path(__file__).resolve().parent / "data"
    documents = load_all_documents(data_dir)
    if not documents:
        raise RuntimeError(f"No supported documents found in {data_dir}")
    print(f"Loaded {len(documents)} documents from {data_dir}.")


if __name__ == "__main__":
    main()
