from typing import Optional
from storage import Storage

def init_translations(translations_dir: str):
    Storage.load(translations_dir)

def __(language: str, original: str, placeholders: Optional[dict[str, str]] = None) -> str:
    translation = Storage.get_translation_string(language, original)
    print(translation)
    if placeholders:
        for placeholder in placeholders:
            print(placeholder)
            translation = translation.replace("%" + placeholder + "%", placeholders[placeholder])

    return translation