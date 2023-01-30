import platform
import subprocess
from datetime import datetime
from pathlib import Path
from tkinter import DISABLED, END, NORMAL, Button, Text, Tk
from zipfile import ZipFile


def main():
    root = Window()
    root.mainloop()


class Window(Tk):
    def __init__(self):
        super().__init__()

        self.title("Gather logs")

        self.text_box = Text(self, width=50, height=10)
        self.text_box.config(state=DISABLED)
        self.text_box.pack()

        self.button = Button(self, text="Run", command=self.handle_run)
        self.button.pack()

    def handle_run(self):
        commands = {
            "System Profile": ["system_profiler", "-detailLevel", "full"],
        }

        self.button.config(state=DISABLED)
        self.update()

        with Archive() as zip_file:
            for name, command in commands.items():
                self.push_text(f"Running {name}...")

                try:
                    result = subprocess.check_output(command)
                except subprocess.CalledProcessError:
                    self.push_text(f"Failed to run {name}.")
                    continue

                zip_file.writestr("system_profile.txt", result)

                self.push_text(f"Finished {name}.")

        self.button.config(state=NORMAL)
        self.update()

    def push_text(self, text):
        if not text.endswith("\n"):
            text += "\n"

        self.text_box.config(state=NORMAL)
        self.text_box.insert(END, text)
        self.text_box.config(state=DISABLED)
        self.update()


class Archive(ZipFile):
    def __init__(self, *args, **kwargs):
        now = datetime.now()
        filename = f"Gather_{now.date()}_{now.time():%H%M%S}_{platform.node()}.zip"
        filename = filename.replace(".local", "")
        path = Path.home() / "Desktop" / filename

        super().__init__(file=path, mode="x", *args, **kwargs)


if __name__ == "__main__":
    main()
