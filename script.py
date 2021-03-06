import bpy

def save_file(file_path):
    bpy.ops.wm.save_as_mainfile(filepath=file_path)


if __name__ == '__main__':
    save_file("script.blend")