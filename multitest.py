try:
    from tkinter import ttk
    import tkinter as tk              # Python 2
    # import ttk
    import queue as queue
except ImportError:
    import tkinter as tk              # Python 3
    import tkinter.ttk as ttk
    import queue

import multiprocessing as mp
import time


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.minsize(width=400, height=25)

        self.label = tk.Label(self, text='Waiting for "work"')
        self.label.pack(expand=True, fill='both')

        self.progressbar = ttk.Progressbar(self, orient='horizontal', value=0, maximum=3, mode='determinate')
        self.progressbar.pack(fill='x')

        self.button = tk.Button(self, text='Start', command=self.start_work)
        self.button.pack(fill='x')

        self.queue = mp.Queue()
        self.process = None

    def start_work(self):
        self.process = mp.Process(target=work, args=(self.queue,))
        self.button.configure(state='disabled')
        self.process.start()
        self.periodic_call()

    def periodic_call(self):
        #   check a queue once
        self.check_queue()

        #   if exit code is None - process is on the run and we should re-schedule check
        if self.process.exitcode is None:
            self.after(100, self.periodic_call)
        #   things are executed
        else:
            self.process.join()
            self.button.configure(state='normal')
            self.label.configure(text='Waiting for "work"')
            self.progressbar.configure(value=0)

    def check_queue(self):
        #   common check of the queue
        while self.queue.qsize():
            try:
                self.label.configure(text=self.queue.get(0))
                self.progressbar.configure(value=self.progressbar['value'] + 1)
            except queue.Empty:
                pass


def work(working_queue):
    for type_of_work in ['Combobulationg Discombobulator', 'Pointing towards space',
                         'Calculating Ultimate Answer']:
        working_queue.put(type_of_work)
        time.sleep(1.5)


if __name__ == '__main__':
    app = App()
    app.mainloop()