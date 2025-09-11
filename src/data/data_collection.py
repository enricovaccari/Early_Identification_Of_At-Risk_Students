# Script to download the dataset from UCI ML Repo and save it locally with checksum

# Modules
from pathlib import Path
import hashlib
from ucimlrepo import fetch_ucirepo

# Configure paths
DATA_DIR = Path("data/raw")        # cartella di destinazione
DATA_DIR.mkdir(parents=True, exist_ok=True)

dataset_file = DATA_DIR / "student_dropout_success.csv"
checksum_file = DATA_DIR / "student_dropout_success.sha256"

# Download dataset from UCI ML Repo
print("⬇️ Fetching dataset from UCI ML Repo...")
dataset = fetch_ucirepo(id=697)  # Student Dropout and Academic Success

# Combine features and target in one DataFrame
df = dataset.data.features.copy()
df["Target"] = dataset.data.targets

# Save .csv file in data/raw/
df.to_csv(dataset_file, index=False)
print(f"Dataset saved to {dataset_file}")

# Generate SHA256 checksum
sha256_hash = hashlib.sha256(dataset_file.read_bytes()).hexdigest()
checksum_file.write_text(sha256_hash)

print(f"SHA256 checksum saved to {checksum_file}")
print(f"   {sha256_hash}")
