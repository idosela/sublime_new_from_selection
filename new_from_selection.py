"""A Sublime Text package that creates a new file from the current selection."""

import sublime, sublime_plugin
from os.path import basename

class NewFromSelection(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view

        # Generate the output file name from the current file name + "snippet"
        output_filename = list(os.path.splitext(basename(view.file_name())))
        output_filename.insert(1, " snippet")

        # Concatenate the current selections into a single string.
        selected_text = ""
        for region in view.sel():
          selected_text = selected_text + view.substr(region)

        # Create the new file.
        output_view = view.window().new_file()
        output_view.set_name("".join(output_filename))
        output_view.insert(edit, 0, selected_text)

    def is_enabled(self):
        return not self.view.sel()[0].empty()

    def description(self):
        return "Creates a new file from the current selection."
