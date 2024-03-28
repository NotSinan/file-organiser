import os


class InputReader:

    def __init__(self) -> None:
        self.src_path = None
        self.dest_path = None

    def set_src_path(self):
        src_path = input('Set the source path: ')
        while not os.path.exists(src_path):
            src_path = input(
                'Invalid path, please enter a valid source path: ')

        print(f'Source path has been set to {src_path}')
        self.src_path = src_path

    def set_dest_path(self):
        dest_path = input('Set the destination path: ')
        while not os.path.exists(dest_path):
            dest_path = input(
                'Invalid path, please enter a valid destination path: ')

        print(f'Destination path has been set to {dest_path}')
        self.dest_path = dest_path

    def get_src_path(self):
        return self.src_path

    def get_dest_path(self):
        return self.dest_path
