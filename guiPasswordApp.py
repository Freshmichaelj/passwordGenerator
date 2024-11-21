from tkinter import *
from PIL import Image, ImageTk  # Import Image
import random as rn

wordOptions = ['hello', 'hey', 'no', 'bye', 'hello', 
               'nope', 'horse', 'purple', 'hat', 'run', 
               'bay', 'lifting', 'austin', 'detroit',
                'DND', 'diva', 'playstation', 'xbox', 
                'mom']
wordInt = rn.randint(0,len(wordOptions) - 1)

letterOptions = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
                 'u', 'v', 'w', 'x', 'y', 'z']
letterInt = rn.randint(0, len(letterOptions) - 1)


numberOptions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numberInt = rn.randint(0, len(numberOptions) - 1)


specialOptions = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                  '|', '\\', '-', '_', '+', '=', ']', '}', '{', '[',
                  '"', "'", ':', ';']
specialInt = rn.randint(0, len(specialOptions) - 1)


# Create the main window
root = Tk()
root.title("Password Generator")

# Set the window size
rootGeometry = root.geometry("500x300")

# Configure background color
root.config(bg='blue')

# Create buttons/labels
welcome_label = Label(
    root,
    text = "Welcome to your password generator\n"
         "If you'd like to make it more complicated,\n"
         "move the sliders to your wishes.",
    bg = 'blue',
    fg = 'white'
)
welcome_label.pack(pady=10)

# Add resized image to GUI
try:
    original_image = Image.open('/Users/diego/Desktop/Projects/PasswordGenerator/keyAndLock.png') # no image will appear, you have to put its file path.
    resized_image = original_image.resize((100, 100), Image.Resampling.LANCZOS)  # Resize to 100x100 pixels
    image = ImageTk.PhotoImage(resized_image)  # Convert to PhotoImage
    image_label = Label(root, image=image)
    image_label.pack(pady=10)
except Exception as e:
    print(f"Error: {e}")

# Add sliders for user to choose how many letters, words, and special characters
# try:
#     scaleWord = Scale(root, from_ = 0, to = len(wordOptions), orient=HORIZONTAL, label = "Words")
#     wordValue = scaleWord.get()
#     scaleWord.pack(pady = 5)

#     scaleLetter = Scale(root, from_ = 0, to = len(letterOptions), orient=HORIZONTAL, label = "Letters")
#     letterValue = scaleLetter.get()
#     scaleLetter.pack(pady = 5)


#     scaleSpecial = Scale(root, from_ = 0, to = len(specialOptions), orient=HORIZONTAL, label = "Special Characters")
#     specialValue = scaleSpecial.get()
#     scaleSpecial.pack(pady = 5)

# except NameError:
#     print("Error: Ensure wordOptions, letterOptions, and specialOptions are defined in passwordGenerator.")


def generatePassword():
    #create an empty list which is able to gain all words, letters, and specials characters. Capitalize randomizer as well.
    wordList = []
    letterList = []
    specialList = []
    numberList = []
    for i in range(wordInt):
        capitalizeWord = rn.randint(0,1)
        if capitalizeWord == 1:
            getWordLength = len(wordOptions[i])
            if getWordLength % 2 == 0:
                word = wordOptions[i].upper()
                wordList.append(word)

            else:
                word = wordOptions[i]
                wordList.append(word)
    for j in range(letterInt):
        capitalizeLetter = rn.randint(0,1)
        if capitalizeLetter == 1:
            letter = letterOptions[j].upper()
            letterList.append(letter)

        else:
            letter = letterOptions[j]
            letterList.append(letter)
    for h in range(specialInt):
        specialChar = specialOptions[h]
        specialList.append(specialChar)
    for k in range(numberInt):
        number = str(numberOptions[k])
        numberList.append(number)

    #merge all lists, shuffles them, and then merges all the shuffles so that you don't have any \n
    mergedLists = wordList + letterList + specialList + numberList
    rn.shuffle(mergedLists)
    password = ''.join(mergedLists)
    
    #creating a new window to generate once you generate password, using the same dimensions as rootGeometry
    passwordWindow = Toplevel(root)
    passwordWindow.title("Generated Password is here!")
    passwordWindow.geometry = rootGeometry

    #puts text on the new window, passwordLabel is taking info from the password we created and displaying it
    Label(passwordWindow, text = "Generated Password:", font = ("Arial", 14)).pack(pady = 10)
    passwordLabel = Label(passwordWindow, text = password, font = ("Arial", 12), wraplength = 350, justify = "center")
    passwordLabel.pack(pady = 10)

    #function allows us to copy the password on display
    def copyToClipboard():
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()

    #creating the button to copy
    Button(passwordWindow, text = "Copy Password", command = copyToClipboard, font = ("Arial", 12)).pack(pady = 5) 


generate_button = Button(root, text = "Generate Password", command = generatePassword, font = ('Arial', 12))
generate_button.pack(pady = 5)

#Adding the main function buttons
quitButton = Button(root, text = "Quit", command = root.destroy)
quitButton.pack(pady = 5)

# Run the application
root.mainloop()
