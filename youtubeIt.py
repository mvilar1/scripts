import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:]) + '+'
else:
    address = pyperclip.paste()



webbrowser.open("https://www.youtube.com/results?search_query=" + address)
