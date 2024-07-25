class bugLogger:
    def __init__(self):
        self.bugs = []

    def log_bug(self, bug_description):
        self.bugs.append(bug_description)

    def save_to_file(self, file_path = "bugs_report.txt"):
        with open(file_path, 'w') as file:
            for bug in self.bugs:
                file.write(f"{bug}\n")