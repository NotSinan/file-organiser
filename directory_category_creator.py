import os


class DirectoryCategoryCreator:
    def __init__(self, file_format, dest_path) -> None:
        self.file_format = file_format
        self.dest_path = dest_path
        self.dump_file_path = os.path.join(self.dest_path, 'dump')

    def create_dump_folder(self):
        if not os.path.exists(self.dump_file_path):
            os.mkdir(self.dump_file_path)
            print(f'Dump folder has been made at {self.dest_path}')

    def make_category_dirs(self):
        for category in self.file_format.keys():
            if not os.path.exists(os.path.join(self.dump_file_path, category)):
                os.mkdir(os.path.join(self.dump_file_path, category))
                print(f'{category} has been made at {self.dump_file_path}')
