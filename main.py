import tkinter as tk
import cv2
from PIL import Image, ImageTk
from dotenv import load_dotenv
import os

class RTSPPlayer:
    def __init__(self, master, rtsp_urls, names):
        self.master = master
        self.rtsp_urls = rtsp_urls
        self.current_stream = 0
        self.names = names

        # Create a label to display the video stream
        self.label = tk.Label(master)
        self.label.pack()

        # Set up the video capture
        self.cap = cv2.VideoCapture(rtsp_urls[self.current_stream])
        self.show_frame()

        # Create a frame for buttons
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(side=tk.BOTTOM, pady=10)

        # Create buttons for each stream
        self.buttons = []
        for i, url in enumerate(rtsp_urls):
            # print(f"Creating button for stream {i} with name {self.names[i]}")
            button = tk.Button(self.button_frame, text=f"{self.names[i]}", command=lambda i=i: self.switch_stream_button(i))
            button.pack(side=tk.LEFT, padx=5)
            self.buttons.append(button)

        # Highlight the initially selected button
        self.highlight_selected_button()

    def show_frame(self):
        ret, frame = self.cap.read()
        if ret:
            # Resize the frame to 960x540
            frame = cv2.resize(frame, (1280, 720))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = ImageTk.PhotoImage(Image.fromarray(frame))
            self.label.config(image=img)
            self.label.image = img
            self.master.after(10, self.show_frame)
        else:
            print("Error: Could not read frame.")
            self.master.after(1000, self.show_frame)

    def switch_stream_button(self, stream_index):
        # Switch to the selected stream by button click
        self.current_stream = stream_index
        # Update the video capture with the new stream
        self.cap = cv2.VideoCapture(self.rtsp_urls[self.current_stream])
        # Highlight the selected button
        self.highlight_selected_button()

    def highlight_selected_button(self):
        # Reset background color for all buttons
        for button in self.buttons:
            button.configure(bg='lightgray')
        # Highlight the selected button
        self.buttons[self.current_stream].configure(bg='lightgreen')

if __name__ == "__main__":
    load_dotenv()
    # Access variables
    names = os.getenv("NAMES").split(',')
    rtsp_urls = os.getenv("RTSP_URLS").split(',')

    # Calculate INDEX dynamically based on the number of elements in the NAMES list
    index = list(range(1, len(names) + 1))


    # verify if the size of NAMES and RTSP_URLS are the same
    if len(names) != len(rtsp_urls):
        raise Exception("The size of NAMES and RTSP_URLS are different.")
    
    if len(rtsp_urls) < 1:
        raise Exception("You need to set at least one RTSP_URL.")
    

    root = tk.Tk()
    root.title("RTSP Stream Switcher")

    player = RTSPPlayer(root, rtsp_urls, names)

    # Exit the application when the close button is clicked
    root.protocol("WM_DELETE_WINDOW", root.destroy)

    root.mainloop()
