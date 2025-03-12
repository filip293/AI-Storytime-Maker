import sys
import subprocess
import os
import re
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit,
    QHBoxLayout, QStackedWidget, QMainWindow, QListWidget, QListWidgetItem, QMessageBox
)
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt, QThread, pyqtSignal


class ScriptRunner(QThread):
    output_signal = pyqtSignal(str)
    error_signal = pyqtSignal(str)
    success_signal = pyqtSignal()
    progress_signal = pyqtSignal(int)

    def __init__(self, script_name):
        super().__init__()
        self.script_name = script_name

    def run(self):
        try:
            process = subprocess.Popen(
                [sys.executable, self.script_name],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                bufsize=1,  # Line buffering
                universal_newlines=True
            )

            tqdm_pattern = re.compile(r"(\d+)%\|(.+?)\| (\d+)/(\d+) .*")

            while True:
                line = process.stdout.readline()
                if not line and process.poll() is not None:
                    break

                tqdm_match = tqdm_pattern.search(line)
                if tqdm_match:
                    percentage = int(tqdm_match.group(1))
                    bar = tqdm_match.group(2)
                    progress_text = f"Progress: {percentage}% {bar}"
                    self.output_signal.emit(progress_text)
                    self.progress_signal.emit(percentage)
                else:
                    self.output_signal.emit(line.strip())

            for error_line in process.stderr:
                self.error_signal.emit(error_line.strip())

            process.wait()

            if process.returncode == 0:
                self.success_signal.emit()
            else:
                self.error_signal.emit(f"{self.script_name} encountered an error.")

        except Exception as e:
            self.error_signal.emit(str(e))


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Storytime Maker")
        self.setGeometry(100, 100, 900, 600)
        self.setStyleSheet("background-color: #222; color: white;")

        self.container = QWidget()
        self.setCentralWidget(self.container)

        layout = QHBoxLayout()
        self.container.setLayout(layout)

        # Menu layout
        self.menu = QListWidget()
        self.menu.setStyleSheet("background-color: #333; color: white; font-size: 16px;")
        self.menu.addItem(QListWidgetItem("🏠 Home"))
        self.menu.addItem(QListWidgetItem("▶ Run Scripts"))
        self.menu.addItem(QListWidgetItem("📖 Story Preview"))
        self.menu.currentRowChanged.connect(self.switch_page)

        self.pages = QStackedWidget()

        self.home_page = QWidget()
        self.run_scripts_page = QWidget()
        self.story_preview_page = QWidget()

        self.setup_home_page()
        self.setup_run_scripts_page()
        self.setup_story_preview_page()

        self.pages.addWidget(self.home_page)
        self.pages.addWidget(self.run_scripts_page)
        self.pages.addWidget(self.story_preview_page)

        layout.addWidget(self.menu, 1)
        layout.addWidget(self.pages, 4)

    def setup_home_page(self):
        layout = QVBoxLayout()
        label = QLabel("Welcome to AI Storytime Maker")
        label.setStyleSheet("font-size: 22px; font-weight: bold;")
        layout.addWidget(label)
        self.home_page.setLayout(layout)

    def setup_run_scripts_page(self):
        layout = QVBoxLayout()

        # Terminal-like output display
        self.terminal_output = QTextEdit()
        self.terminal_output.setReadOnly(True)
        self.terminal_output.setStyleSheet("background-color: #111; color: white; font-size: 14px;")

        # Buttons for each script
        self.story_button = QPushButton("Run Story Script")
        self.story_button.setStyleSheet("background-color: #2196F3; color: white; font-size: 16px;")
        self.story_button.clicked.connect(lambda: self.run_script("Story.py"))

        self.video_button = QPushButton("Run Video Script")
        self.video_button.setStyleSheet("background-color: #FF9800; color: white; font-size: 16px;")
        self.video_button.clicked.connect(lambda: self.run_script("Video.py"))

        self.autocaps_button = QPushButton("Run AutoCAPS Script")
        self.autocaps_button.setStyleSheet("background-color: #8BC34A; color: white; font-size: 16px;")
        self.autocaps_button.clicked.connect(lambda: self.run_script("AutoCAPS.py"))

        layout.addWidget(self.terminal_output)
        layout.addWidget(self.story_button)
        layout.addWidget(self.video_button)
        layout.addWidget(self.autocaps_button)
        self.run_scripts_page.setLayout(layout)

    def setup_story_preview_page(self):
        layout = QVBoxLayout()
        self.story_text = QTextEdit()
        self.story_text.setReadOnly(True)
        self.story_text.setStyleSheet("background-color: #111; color: white; font-size: 14px;")
        self.load_story_button = QPushButton("Load Story")
        self.load_story_button.setStyleSheet("background-color: #8BC34A; color: white; font-size: 16px;")
        self.load_story_button.clicked.connect(self.load_story)

        layout.addWidget(self.story_text)
        layout.addWidget(self.load_story_button)
        self.story_preview_page.setLayout(layout)

    def switch_page(self, index):
        self.pages.setCurrentIndex(index)

    def run_script(self, script_name):
        self.terminal_output.clear()  # Clear previous output
        self.terminal_output.append(f"Running {script_name}...")

        self.thread = ScriptRunner(script_name)
        self.thread.output_signal.connect(self.update_terminal_output)
        self.thread.error_signal.connect(self.show_error)
        self.thread.success_signal.connect(self.show_success)
        self.thread.progress_signal.connect(self.update_progress_bar)
        self.thread.start()

    def update_terminal_output(self, text):
        self.terminal_output.append(text)

    def update_progress_bar(self, value):
        self.terminal_output.append(f"Progress: {value}%")

    def show_error(self, text):
        self.terminal_output.append(f"Error: {text}")

    def show_success(self):
        self.terminal_output.append("Script completed successfully!")

    def load_story(self):
        if os.path.exists("story.txt"):
            with open("story.txt", "r", encoding="utf-8") as file:
                self.story_text.setPlainText(file.read())
        else:
            QMessageBox.warning(self, "Warning", "No story found.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec())
