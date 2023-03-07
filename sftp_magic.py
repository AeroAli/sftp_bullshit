import json
import os
from datetime import datetime

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
        # print(sftp.getcwd())
        with sftp.cd("../saberinblue"):
            print(sftp.getcwd())
            for folder, fic_dict in files.items():
                print(folder)
                try:
                    sftp.mkdir(folder)
                    sftp.cwd(folder)
                except:
                    sftp.cwd(folder)
                directory_structure = sftp.listdir_attr()
                for value in fic_dict:
                    print(sftp.getcwd())
                    sftp.put(value)
                for attr in directory_structure:
                    print(attr.filename, attr)
                sftp.cwd("/home/saberinblue")
                print(sftp.getcwd())


def get_files():
    target_folder = "old/www.samgabrielvo.com/misc"
    target_string = ""
    wanted_folders = []
    user = ""
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
                    for i in wanted_folders:
                        if i == folder:
                            # print(file)
                            # print(file)
                            extension = short.split(".")[-1]
                            if extension not in ["mov", "rar", "zip", "wav", "mp4"]:
                                # print(short)
                                try:
                                    file_dict[
                                        f"/home/{user}/{file.split('old/www.')[1].split(folder)[0]}{folder}"].append(
                                        file)
                                except:
                                    file_dict[f"/home/{user}/{file.split('old/www.')[1].split(folder)[0]}{folder}"] = [
                                        file]
                            # if extension not in ext:
                            #     ext.append(extension)
                if target_string in file:
                    try:
                        file_dict[f"/home/{user}/samgabrielvo.com/misc/"].append(file)
                    except:
                        file_dict[f"/home/{user}/samgabrielvo.com/misc/"] = [file]
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
    files = {"/home/aeroali/test": ["sftp_magic.py"], "/home/aeroali/test2": ["sftp_magic.py"]}
    with pysftp.Connection(account["froops"]["host"], username=account["froops"]["username"],
                           password=account["froops"]["password"]) as sftp:
        # print(sftp.getcwd())

        with sftp.cd("../aeroali"):
            for folder, fic_dict in files.items():
                print(folder)
                try:
                    sftp.mkdir(folder)
                    sftp.cwd(folder)
                except:
                    sftp.cwd(folder)
                directory_structure = sftp.listdir_attr()
                for value in fic_dict:
                    print(sftp.getcwd())
                    sftp.put(value)
                    for attr in directory_structure:
                        print(attr.filename, attr)
                    sftp.cwd("../")
                    print(sftp.getcwd())


def structure():
    with open("out.txt", "r") as f:
        j = json.load(f)
        for k, v in j.items():
            for i in v:
                print(k, i)


if __name__ == "__main__":
    # get_files()
    sam_sftp()
    # froops_sftp()
    # structure()
