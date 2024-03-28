from file_mover import FileMover
from directory_category_creator import DirectoryCategoryCreator
from input_reader import InputReader


if __name__ == '__main__':

    file_format = {
        "Web": [".html5", ".html", ".htm", ".xhtml"],
        "Picture": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg", ".heif", ".psd"],
        "Video": [".avi", ".mkv", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],
        "Document": [".oxps", ".epub", ".pages", ".docx", ".txt", ".pdf", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", ".pptx"],
        "Compressed": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip"],
        "Audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"],
    }

    input_reader = InputReader()
    input_reader.set_src_path()
    input_reader.set_dest_path()
    src_path = input_reader.get_src_path()
    dest_path = input_reader.get_dest_path()

    file_mover = FileMover(
        src_path=src_path,
        dest_path=dest_path,
        file_format=file_format
    )

    directory_category_creator = DirectoryCategoryCreator(
        file_format=file_format,
        dest_path=dest_path
    )

    directory_category_creator.create_dump_folder()
    directory_category_creator.make_category_dirs()

    file_mover.move_files_by_format()
