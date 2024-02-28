"""
This module depicts a RACE CONDITION

Two threads attempt to write text into their own respective files. The goal is for
two output files to be created with their own unique text output

However due to timing issues only one output file is generated with varying text
"""

import threading
import time
import logging

class FileSaver:
    """
    Class to handle saving data to a file
    """
    def __init__(self):
        self.dest_file = "" #output location of file
    def save_data(self, dest_file, text, name):
        """
        Sets a new destination file and writes to it
        :param dest_file: str, filename for text to be written out to
        :param text: str, text to be written into file
        :param name: str, name of thread
        """
        logging.info("Thread %s setting destination file: %s", name, dest_file)
        self.dest_file = dest_file
        logging.info("Thread %s sleep", name)
        time.sleep(1)

        logging.info("Thread %s opening file", name)
        with open(self.dest_file, 'w') as opened_file:
            logging.info("Thread %s writing '%s' to %s", name, text, self.dest_file)
            opened_file.write(text)
        logging.info("Thread %s finishing save_data", name)



if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    file_saver = FileSaver()

    # Saving file data WITHOUT locks
    thread_1 = threading.Thread(target=file_saver.save_data, args=("output_1.txt", "Thread 1 was here", 1))
    thread_2 = threading.Thread(target=file_saver.save_data, args=("output_2.txt", "Thread 2 was here", 2))

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()