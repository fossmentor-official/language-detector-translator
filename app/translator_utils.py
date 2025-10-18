# --------------------------------------------------------------
# 🌐 translator_utils.py
# --------------------------------------------------------------
# This module provides a utility function `translate_text` that
# attempts to translate text using multiple translation APIs:
# 1️⃣ Google Translator (online)
# 2️⃣ LibreTranslate (online and open-source)
# 3️⃣ Argos Translate (offline)
# 4️⃣ MyMemory Translator (backup online service)
#
# The function automatically falls back to the next service if
# one fails, ensuring translation is attempted even without Internet.
# --------------------------------------------------------------

# Import multiple translation libraries
from googletrans import Translator as GoogleTranslator        # Google Translate API (unofficial)
from libretranslatepy import LibreTranslateAPI                # LibreTranslate open API client
import argostranslate.package, argostranslate.translate       # Offline translation (Argos Translate)
from translate import Translator as MyMemoryTranslator        # MyMemory translation service


def translate_text(text, target_lang="en"):
    """
    Attempts to translate the given text into the specified target language
    using multiple translation engines (Google → Libre → Argos → MyMemory).

    Args:
        text (str): The text to be translated.
        target_lang (str): Target language code (default: 'en').

    Returns:
        tuple: (translated_text, translators_used or errors)
            - translated_text: The translated output if successful, else None.
            - translators_used: List of successful translator(s).
              OR
              errors: List of all error messages if all engines fail.
    """

    # Keep track of which translators were successfully used
    translators_used = []

    # Store the translation result
    translated_text = None

    # Collect any error messages for debugging
    errors = []

    # --------------------------------------------------------------
    # 1️⃣ Attempt Translation using Google Translator
    # --------------------------------------------------------------
    try:
        gt = GoogleTranslator()  # Initialize Google Translator
        translated_text = gt.translate(text, dest=target_lang).text  # Perform translation
        translators_used.append("Google Translator")
        return translated_text, translators_used  # Return if successful
    except Exception as e:
        errors.append(f"Google Translator failed: {e}")

    # --------------------------------------------------------------
    # 2️⃣ Attempt Translation using LibreTranslate
    # --------------------------------------------------------------
    if not translated_text:  # Proceed only if previous attempt failed
        try:
            lt = LibreTranslateAPI("https://libretranslate.com/")  # Connect to public Libre API
            translated_text = lt.translate(text, source="auto", target=target_lang)
            translators_used.append("LibreTranslate")
            return translated_text, translators_used
        except Exception as e:
            errors.append(f"LibreTranslate failed: {e}")

    # --------------------------------------------------------------
    # 3️⃣ Attempt Translation using Argos Translate (Offline)
    # --------------------------------------------------------------
    # Argos is helpful when the device is offline or APIs fail.
    if not translated_text:
        try:
            # Ensure translation packages are up-to-date
            argostranslate.package.update_package_index()

            # Perform offline translation (requires installed language packs)
            translated_text = argostranslate.translate.translate(text, "en", target_lang)
            translators_used.append("Argos Translate (Offline)")
            return translated_text, translators_used
        except Exception as e:
            errors.append(f"Argos Translate failed: {e}")

    # --------------------------------------------------------------
    # 4️⃣ Attempt Translation using MyMemory Translator
    # --------------------------------------------------------------
    # This acts as a final fallback translator.
    if not translated_text:
        try:
            my_translator = MyMemoryTranslator(to_lang=target_lang)
            translated_text = my_translator.translate(text)
            translators_used.append("MyMemory Translator")
            return translated_text, translators_used
        except Exception as e:
            errors.append(f"MyMemory Translator failed: {e}")

    # --------------------------------------------------------------
    # 🧩 If all translation engines fail, return error details
    # --------------------------------------------------------------
    return None, errors
