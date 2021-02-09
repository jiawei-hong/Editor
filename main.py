import tkinter as tk
from tkinter import filedialog


class Editor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x600')
        self.root.title('TXT - Editor')
        self.selectFile = tk.Button(
            self.root, text='選擇檔案', width=50, command=self.openFile)
        self.selectFile.pack(side='top')
        self.quitButton = tk.Button(
            self.root, text='退出', width=50, command=self.quit)
        self.quitButton.pack(side='bottom')
        self.root.mainloop()

    def openFile(self):
        self.filename = filedialog.askopenfilename()
        read = open(self.filename, 'r')
        self.text = tk.Text(self.root, width=30, height=30)
        self.text.pack()
        self.text.insert('insert', read.read())
        read.close()
        self.saveFileButton = tk.Button(
            self.root, text='保存檔案', width=50, command=self.saveFile)
        self.saveFileButton.pack(side='bottom')

    def saveFile(self):
        extension = self.filename.split('.')[-1]
        file = filedialog.asksaveasfile(mode='w', initialfile=self.filename)

        if file is None:
            return

        file.write(self.text.get(1.0, 'end'))
        file.close()
        self.quit()

    def quit(self):
        self.root.destroy()


if __name__ == '__main__':
    app = Editor()
