import os
import shutil
import hashlib
from datetime import datetime
from pathlib import Path

class SuperFix:
    def __init__(self, source_dir, target_dirs):
        self.source_dir = Path(source_dir)
        self.target_dirs = [Path(target) for target in target_dirs]
        self.file_hashes = {}

    def calculate_hash(self, file_path):
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def scan_source_files(self):
        for root, _, files in os.walk(self.source_dir):
            for file in files:
                file_path = Path(root) / file
                file_hash = self.calculate_hash(file_path)
                self.file_hashes[file_path] = file_hash

    def synchronize(self):
        self.scan_source_files()
        for target_dir in self.target_dirs:
            self.sync_to_target(target_dir)

    def sync_to_target(self, target_dir):
        if not target_dir.exists():
            print(f"Creating directory: {target_dir}")
            os.makedirs(target_dir)

        for file_path, file_hash in self.file_hashes.items():
            relative_path = file_path.relative_to(self.source_dir)
            target_file_path = target_dir / relative_path
            
            if target_file_path.exists():
                target_file_hash = self.calculate_hash(target_file_path)
                if target_file_hash == file_hash:
                    print(f"File is up-to-date: {target_file_path}")
                    continue
            
            print(f"Synchronizing: {target_file_path}")
            target_file_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(file_path, target_file_path)

    def run(self):
        start_time = datetime.now()
        print(f"Starting synchronization at {start_time}")
        self.synchronize()
        end_time = datetime.now()
        print(f"Synchronization completed at {end_time}, duration: {end_time - start_time}")

if __name__ == "__main__":
    source_directory = "C:/path/to/source"
    target_directories = [
        "C:/path/to/target1",
        "C:/path/to/target2",
    ]
    
    superfix = SuperFix(source_directory, target_directories)
    superfix.run()