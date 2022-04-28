import os


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

    def scan(self):
        self.check_extension(self.path)
        file_contents = self.scan_by_line(self.path)
        print(file_contents)
