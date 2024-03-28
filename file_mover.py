import os
import shutil


class FileMover:
    def __init__(self, src_path, dest_path, file_format) -> None:
        self.src_path = src_path
        self.dest_path = dest_path
        self.file_format = file_format

    def move_files_by_format(self):
        files = os.listdir(self.src_path)

        for file in files:
            file_extension = os.path.splitext(file)[1]
            for category, extensions in self.file_format.items():
                if file_extension.lower() in extensions:
                    src = os.path.join(self.src_path, file)
                    dst = os.path.join(self.dest_path, 'dump', category, file)
                    shutil.move(src, dst)
                    print(f'{file} was moved from {src} to {dst}')
