# World-Replacer

Documentation for the Word Replacement GUI Application
Overview:

This Python program creates a simple graphical user interface (GUI) using tkinter where users can enter a text in one text box, specify the word they want to replace, and specify the new word to replace it with. The program then updates the text by replacing the specified word with the new word and displays the modified text.
Main Components:

    replace_word function: Takes the original text, the old word to be replaced, and the new word as inputs, and returns the modified text with the old word replaced by the new one.
    replace_and_update function: Handles the logic for retrieving the user input, calling the replace_word function, and updating the text box with the result.
    Tkinter GUI: Contains the text box for input, labels for instructions and results, and buttons to trigger the word replacement.

Explanation of Code:

    replace_word Function:
        Parameters:
            text: The original text where the word replacement is to be done.
            old_word: The word that should be replaced.
            new_word: The word that will replace the old_word.
        Working:
            The text is split into lines using split('\n').
            Each line is split into words using split().
            The program iterates over each word in each line. If the word matches the old_word, it replaces it with new_word.
            The modified lines are then joined back together and returned as the modified text.

    replace_and_update Function:
        Steps:
            Retrieves the input from the user (old word and new word) from the entry widgets.
            If both the old word and new word are provided:
                Gets the text from the text box.
                Calls the replace_word function to process the text.
                Updates the text box with the modified text.
                Displays the new word in a label to indicate which word was replaced.
                Clears the entry fields for a better user experience.
            If either the old or new word is missing, displays an error message in the label.

    Tkinter GUI Layout:
        Instruction Label: A label at the top of the window that explains the purpose of the application.
        Textbox: A multi-line text box for the user to input the text that will be processed.
        Scrollbars: Vertical and horizontal scrollbars are added to the text box to allow scrolling through large texts.
        Input Fields:
            input_old_word: Entry widget for the user to input the word they want to replace.
            input_new_word: Entry widget for the user to input the new word to replace the old one.
        Update Button: A button that triggers the replace_and_update function when clicked.
        Result Label: A label that displays the word that was replaced, or an error message if the input is incomplete.

Features:

    Text Replacement: The program can replace a specified word in the text with a new word.
    Clear UI: The program clears the input fields after a replacement is done to make it easier for users to perform additional replacements.
    Scrollbars: Handles large text input and makes it easier for users to navigate the text using vertical and horizontal scrollbars.
    User Guidance: Instructions are displayed at the top, guiding users on how to use the app.
