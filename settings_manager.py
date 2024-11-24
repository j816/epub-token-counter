import json
import os
from pathlib import Path

class SettingsManager:
    def __init__(self):
        self.settings_file = Path.home() / '.epubtokens_settings.json'
        self.default_settings = {
            'input_folder': '',
            'output_folder': '',
            'token_count': '100000'
        }

    def load_settings(self):
        """Load settings from file, return defaults if file doesn't exist"""
        try:
            if self.settings_file.exists():
                with open(self.settings_file, 'r') as f:
                    return json.load(f)
            return self.default_settings
        except Exception:
            return self.default_settings

    def save_settings(self, settings):
        """Save settings to file"""
        try:
            with open(self.settings_file, 'w') as f:
                json.dump(settings, f)
        except Exception as e:
            print(f"Error saving settings: {e}") 