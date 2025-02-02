import json
from pathlib import Path

CONFIG_PATH = Path("D:\\Work\\TargetingTool\\config\\accounts_config.json")

def create_default_config():
    default_config = {
        "accounts": {
            "account1": {
                "apps": ["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"],
                "urls": ["https://google.com"]
            }
        }
    }
    with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
        json.dump(default_config, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    if not CONFIG_PATH.exists():
        create_default_config()
        print("Конфиг создан!")
    else:
        print("Конфиг уже существует.")
    input("Нажмите Enter...")
