import os
import re

class Scan:

    def __init__(self, path: str):
        self.path = path

    def check_extension(self, filepath):
        file_ext = self.split_filename(filepath)
        if file_ext[1] == ".py":
            return True
        else:
            print("File must have .py extension")
            raise SystemExit(1)

    def split_filename(self, filepath):
        filename = os.path.splitext(filepath)
        return filename

    def scan_by_line(self, filepath):
        try:
            file1 = open(filepath, 'r')
            lines = file1.readlines()
        except:
            print("Error: Error reading file")
            raise SystemExit(1)
        else:
            scanned_lines = []
            for line in lines:
                line = line.strip()
                if line.startswith("def ") or line.startswith("class "):
                    scanned_lines.append(line)
            return scanned_lines

    def trim_string(self, string):
        string = string[0]
        string = string[1:-1]
        return string

    def parse(self, file_lines):
        methods = []
        for line in file_lines:
            method_name = re.findall(r"\s.+\({1}", line)
            method_name = self.trim_string(method_name)
            methods.append(method_name)

            method_args = re.findall(r"\({1}.+\){1}", line)
            if method_args:
                method_args = trim_string(method_args)
                method_args = method_args.split(",")
                print(method_args)

    def scan(self):
        self.check_extension(self.path)
        file_contents = self.scan_by_line(self.path)
        self.parse(file_contents)
