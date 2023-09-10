import os
from glob import glob
from re import sub as re_sub
from git import Repo, exc
import yaml


class DTLRepo:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        self.yaml_extensions = ["yaml", "yml"]
        self.url = "https://github.com/netbox-community/devicetype-library.git"
        self.repo_path = f"{os.path.dirname(os.path.realpath(__file__))}\\device_lib_repo\\devicetype-library"
        print(self.repo_path)
        self.branch = "master"
        self.repo = None
        self.cwd = os.getcwd()

        if os.path.isdir(self.repo_path):
            self.pull_repo()
        else:
            self.clone_repo()

    def get_relative_path(self):
        return self.repo_path

    def get_absolute_path(self):
        return os.path.join(self.cwd, self.repo_path)

    def get_devices_path(self):
        return os.path.join(self.get_absolute_path(), "device-types")

    def get_modules_path(self):
        return os.path.join(self.get_absolute_path(), "module-types")

    def slug_format(self, name):
        return re_sub("\W+", "-", name.lower())

    def pull_repo(self):
        self.repo = Repo(self.repo_path)
        if not self.repo.remotes.origin.url.endswith(".git"):
            self.repo.remotes.origin.pull()
        self.repo.git.checkout(self.branch)

    def clone_repo(self):
        self.repo = Repo.clone_from(
            self.url, self.get_absolute_path(), branch=self.branch
        )

    def get_devices(self, base_path):
        files = []
        discovered_vendors = []
        vendor_dirs = os.listdir(base_path)
    
        for folder in [
            vendor
            for vendor in vendor_dirs
        ]:
            if folder.casefold() != "testing":
                discovered_vendors.append(
                    {"name": folder, "slug": self.slug_format(folder)}
                )
                for extension in self.yaml_extensions:
                    files.extend(glob(base_path + "/" + folder + f"/*.{extension}"))
        return files, discovered_vendors

    def parse_files(self, files: list, slugs: list = None):
        deviceTypes = []
        for file in files:
            with open(file, "r", encoding="utf8") as stream:
                try:
                    data = yaml.safe_load(stream)
                except yaml.YAMLError as excep:
                    continue
                manufacturer = data["manufacturer"]
                data["manufacturer"] = {
                    "name": manufacturer,
                    "slug": self.slug_format(manufacturer),
                }

                # Save file location to resolve any relative paths for images
                data["src"] = file

            if slugs and True not in [
                True if s.casefold() in data["slug"].casefold() else False
                for s in slugs
            ]:
                continue

            deviceTypes.append(data)
        return deviceTypes
