#-----------------------------------------------------------------WORKING--------------------------------------------------------------------------------

import tkinter as tk
from threading import Thread
from Gesture_Controller import GestureController

class GestureControllerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Gesture Controller")

        self.start_button = tk.Button(master, text="Start", command=self.start_gesture_controller)
        self.start_button.pack()

        # self.stop_button = tk.Button(master, text="Stop", command=self.stop_gesture_controller, state=tk.DISABLED)
        # self.stop_button.pack()

        self.gesture_controller = GestureController()
        self.gesture_controller_thread = None

    def start_gesture_controller(self):
        self.start_button.config(state=tk.DISABLED)
        # self.stop_button.config(state=tk.NORMAL)
        self.gesture_controller_thread = Thread(target=self.gesture_controller.start)
        self.gesture_controller_thread.start()

    # def stop_gesture_controller(self):
    #     self.start_button.config(state=tk.NORMAL)
    #     self.stop_button.config(state=tk.DISABLED)
    #     self.gesture_controller.gc_mode = 0
    #     if self.gesture_controller_thread is not None:
    #         self.gesture_controller_thread.join()

def main():
    root = tk.Tk()
    gui = GestureControllerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

