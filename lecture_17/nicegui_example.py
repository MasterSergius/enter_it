import json
from nicegui import ui


class LanguageSwitcherApp:
    def __init__(self):
        self.current_language = "en"
        self.main_message_label: ui.label
        self.description_label: ui.label
        self.lang_switcher_label: ui.label
        self.lang_toggle: ui.toggle
        self.load_messages("en")

    def load_messages(self, lang: str):
        """
        Load messages from the language file
        """
        try:
            with open(f"{lang}.json", "r", encoding="utf-8") as f:
                self.messages = json.load(f)
        except FileNotFoundError:
            ui.notify(
                f"Language file '{
                    lang}.json' not found. Defaulting to English.",
                type="negative",
            )
        except json.JSONDecodeError:
            ui.notify(
                f"Error decoding JSON from '{
                    lang}.json'. Defaulting to English.",
                type="negative",
            )

    def update_ui_text(self, lang: str):
        """
        Updates the text of all relevant UI elements based on the current_language.
        """
        self.load_messages(lang)

        self.main_message_label.set_text(self.messages["main_message"])
        self.description_label.set_text(self.messages["description"])
        self.lang_switcher_label.set_text(
            self.messages["language_switcher_label"])

    def index_page(self):
        """
        Main page. Creates all elements with initial values.
        """
        with ui.column().classes("absolute-center items-center"):
            with ui.card().classes("w-full max-w-lg p-6 shadow-lg rounded-lg"):
                self.main_message_label = ui.label().classes(
                    "text-4xl font-bold text-center mb-4 text-blue-800"
                )

                self.description_label = ui.label().classes(
                    "text-lg text-gray-700 text-center mb-6"
                )

                self.lang_switcher_label = ui.label().classes(
                    "text-md font-semibold text-gray-600 mb-2"
                )

                self.lang_toggle = ui.toggle(
                    {
                        "en": self.messages["lang_en_button"],
                        "ua": self.messages["lang_ua_button"],
                    },
                    value=self.current_language,
                    on_change=lambda e: self.update_ui_text(e.value),
                ).props('toggle-color="primary" push')

        self.update_ui_text(self.current_language)


@ui.page("/")
def index_page():
    app_instance = LanguageSwitcherApp()
    app_instance.index_page()


ui.run()
