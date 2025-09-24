import os


def get_files_info(working_directory, directory="."):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_directory_abs = os.path.abspath(os.path.join(working_directory, directory))

        if not target_directory_abs.startswith(working_directory_abs):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_directory_abs):
            return f'Error: "{directory}" is not a directory'

        entries = []
        for entry in os.listdir(target_directory_abs):
            entry_path = os.path.join(target_directory_abs, entry)
            try:
                file_size = os.path.getsize(entry_path)
                is_dir = os.path.isdir(entry_path)
                entries.append(f"- {entry}: file_size={file_size} bytes, is_dir={is_dir}")
            except Exception as e:
                entries.append(f"- {entry}: Error: {str(e)}")

        return "\n".join(entries)

    except Exception as e:
        return f"Error: {str(e)}"