import json
import os
from datetime import datetime
import json

import pysftp

account = {
    "froops": {
        "host": "",
        "username": "",
        "password": ""
    },
    "sam": {
        "host": "",
        "username": "",
        "password": ""
    }
}


def sam_sftp():
    files = get_files()
    with pysftp.Connection(account["sam"]["host"], username=account["sam"]["username"],
                           password=account["sam"]["password"]) as sftp:
        user = account["sam"]["username"]
        # print(sftp.getcwd())
        with sftp.cd(f"/home/{user}"):
            print(sftp.getcwd())
            for folder, fic_dict in files.items():
                print(folder)
                try:
                    sftp.mkdir(folder)
                    sftp.cwd(folder)
                except:
                    sftp.cwd(folder)
                for value in fic_dict:
                    remote_file = f"{folder}/{value.split('/')[-1]}"
                    local_size = os.stat(value).st_size
                    print(f"{value.split('/')[-1]}")
                    try:
                        remote_size = sftp.stat(remote_file).st_size
                        # print(f"{value.split('/')[-1]}:\n\tlocal size: {local_size}:\n\tremote size: {remote_size}")
                        if remote_size != local_size:
                            sftp.put(value)
                    except:
                        # print(f"{value.split('/')[-1]}:\n\tlocal size: {local_size}")
                        sftp.put(value)
                    # print(sftp.getcwd())
                directory_structure = sftp.listdir_attr()
                for attr in directory_structure:
                    print(attr.filename, attr)
                sftp.cwd(f"/home/{user}")
                print(sftp.getcwd())


def get_files():
    user = ""
    target_folder = ""
    target_string = ""
    wanted_folders = []
    wanted_folder = []
    print(os.getcwd())
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    file_dict = {}
    ext = []
    try:
        current = os.getcwd()
        tar = os.path.abspath(os.path.join(current, target_folder))
        for (dirpath, dirnames, filenames) in os.walk(tar):
            for file in filenames:
                file = os.path.join(dirpath, file)
                short = file.split("/misc/")[1]
                # print(type(short))
                folder = str(short).split("/")
                folder = folder[0]
                # print(type(folder))

                if len(folder) > 1:
                    # print(folder[0])
                    for i in wanted_folder:
                        if i == folder:
                            try:
                                file_dict[f"/home/{user}/{file.split('old/www.')[1].split(folder)[0]}{folder}"].append(file)
                            except:
                                file_dict[f"/home/{user}/{file.split('old/www.')[1].split(folder)[0]}{folder}"] = [file]

                    for i in wanted_folders:
                        if i == folder:
                            # print(file)
                            # print(file)
                            extension = short.split(".")[-1]
                            if extension not in ["mov", "rar", "zip", "wav", "mp4"]:
                                # print(short)
                                try:
                                    file_dict[f"/home/{user}/{file.split('old/www.')[1].split(folder)[0]}{folder}"].append(file)
                                except:
                                    file_dict[f"/home/{user}/{file.split('old/www.')[1].split(folder)[0]}{folder}"] = [file]
                            # if extension not in ext:
                            #     ext.append(extension)
                if target_string in file:
                    try:
                        file_dict[f"/home/{target_folder.split('old/www.')[-1]}"].append(file)
                    except:
                        file_dict[f"/home/{target_folder.split('old/www.')[-1]}"] = [file]
        # for file in files:
        #     print(file)
        # print(ext)
        # print(file_dict)
        with open("out.txt", "w") as j:
            json.dump(file_dict, j, indent=4)
    except OSError as Er:
        print(Er)
    return file_dict


def froops_sftp():
    files = {"/home/aeroali/test": ["test.txt"], "/home/aeroali/test2": ["test.txt"]}
    with pysftp.Connection(account["froops"]["host"], username=account["froops"]["username"],
                           password=account["froops"]["password"]) as sftp:
        user = account["froops"]["username"]
        # print(sftp.getcwd())
        with sftp.cd(f"/home/{user}"):
            for folder, fic_dict in files.items():
                print(folder)
                try:
                    sftp.mkdir(folder)
                    sftp.cwd(folder)
                except:
                    sftp.cwd(folder)
                for value in fic_dict:
                    remote_file = f"{folder}/{value.split('/')[-1]}"
                    local_size = os.stat(value).st_size
                    try:
                        remote_size = sftp.stat(remote_file).st_size
                        print(local_size, remote_size)
                        if remote_size != local_size:
                            sftp.put(value)
                    except:
                        print(local_size)
                        sftp.put(value)
                    # print(sftp.getcwd())
                    directory_structure = sftp.listdir_attr()
                    for attr in directory_structure:
                        print(attr.filename, attr)
                    sftp.cwd(f"/home/{user}")
                    print(sftp.getcwd())


def structure():
    with open("out.txt", "r") as f:
        j = json.load(f)
        for k, v in j.items():
            for i in v:
                print(k, i)


if __name__ == "__main__":
    sam_sftp()
    # froops_sftp()
    # get_files()
    # structure()
