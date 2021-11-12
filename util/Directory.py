import os
import glob


def create_dir(dir_name, path):
    dir_struct = ("Geo",
                  "Geo/Variant",
                  "Geo/Variant/Abc",
                  "Looks",
                  "Looks/Texture",
                  "Looks/Texture/Preview",
                  "Looks/Texture/Render",
                  )
    if not os.path.exists(path + "/" + dir_name):
        for folder in dir_struct:
            os.makedirs(path + "/" + dir_name + "/" + folder)


def get_directory_files(dir_path):
    files_path = []
    files_name = []
    for file_path in glob.glob(os.path.join(dir_path, "*")):
        files_path.append(file_path)
        files_name.append(file_path.split("/")[-1])
    return files_path, files_name


def rename(file_path, new_name):
    dir = "/".join(file_path.split("/")[:-1])
    path = os.path.join(dir, new_name)
    os.rename(file_path, path)


def get_texture_type(tex_name):
    ref_type = ("Basecolor",
                "Albedo",
                "Specular",
                "Gloss",
                "Roughness",
                "Normal",
                "Bump",
                "Opacity",
                "Translucency",
                "Displacement",
                )
    tex_type = ""
    for type in ref_type:
        if tex_name.lower().find(type.lower()) != -1:
            tex_type = type
    return tex_type

def get_tex_res(tex_name):
    ref_res = ("1K",
               "2K",
               "4K",
               "8K",
               "16K")
    tex_res = ""
    for res in ref_res:
        if tex_name.lower().find(res.lower()) != -1:
            tex_res = res
    return tex_res


if __name__ == '__main__':
    file = get_directory_files("/home/passion/Desktop/test/Texture")
    for tex in file[1]:
        get_texture_type(tex)
        get_tex_res(tex)

