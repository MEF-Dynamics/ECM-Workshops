import pyautogui as pg
import time
import pyperclip as pc
import colorama
import re as regex

def extract_word_list(input_file_path:str=None) -> list[str]:
    """
    Method, that extracts the words from the data.txt file.
    @Params:
        input_file_path : (str) : (default=None) : The path of the file to read.
    @Returns:
        words : (list of strings) : The list of words in the file.
    """

    if input_file_path is None: # Terminate the program if the input_file_path is None.
        raise ValueError(colorama.Fore.RED, "!!! The input_file_path cannot be None.", colorama.Fore.RESET)

    with open(input_file_path, "r", encoding="utf-8") as f: # Read file directly via memory
        classed = [] # A list to get the parts from data that includes our word patterns.
        words = [] # A list to sum up all the words in the file.
        for line in f: # Loop through the lines in the file.
            for string in line.split(): # Loop through the words in the line.
                if "class" in string: # If the word includes "class" in it, add it to the classed list.
                    classed.append(string) # Add the word to the classed list.
            print(colorama.Fore.GREEN, "*** Classing done.", colorama.Fore.RESET)
            pattern = r'>(\w+)<' # A regex pattern to get the words between the > and < signs.
            words_in_line = regex.findall(pattern, line) # Find all the words that match the pattern.
            words.extend(words_in_line) # Add the words to the words list.
            print(colorama.Fore.GREEN, "*** Words successfully extracted.", colorama.Fore.RESET)

    return words # Return the words list.

def execute_bot(word_list:list[str]=None) -> bool:
    """
    Method, that executes the bot.
    @Params:
        word_list : (list of strings) : (default=None) : The list of words to use in the bot.
    @Returns:
        status : (bool) : The status of the bot execution.
    """

    if word_list is None: # Terminate the program if the word_list is None.
        raise ValueError(colorama.Fore.RED, "!!! The word_list cannot be None.", colorama.Fore.RESET)

    print(colorama.Fore.YELLOW, ">>> Application starting, please leave the mouse pointer on entry point...", colorama.Fore.RESET)
    time.sleep(3) # Wait for 5 seconds for the user to leave the mouse pointer on the entry point.
    print(colorama.Fore.GREEN, "*** Application started.", colorama.Fore.RESET)

    input_entry_location = pg.position() # Get the position of the mouse pointer.

    pg.click(x=input_entry_location.x, y=input_entry_location.y, clicks=2, button="left") # Click on the entry point.
    
    for word in word_list: # Loop through the words in the word_list.

        pc.copy(word) # Copy the word to the clipboard.

        with pg.hold("ctrl"):
            with pg.hold("v"):
                pg.press("space")

        time.sleep(0.01)

    print(colorama.Fore.GREEN, "*** Application finished.", colorama.Fore.RESET)

if __name__ == "__main__":
    
    try :
        word_list = extract_word_list(input_file_path="data.txt") # Extract the words from the data.txt file.
        execute_bot(word_list=word_list) # Execute the bot.
    except Exception as e :
        print(e)
        exit()