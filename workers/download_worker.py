from threading import Thread
import gdown


class DownloadWorker(Thread):
    def __init__(self, name, queue):
        Thread.__init__(self)
        self.name = name
        self.queue = queue

    def run(self) -> None:
        while True:
            item_one = self.queue.get()
            try:
                gdown.download(item_one['webContentLink'], './files/{}'.format(item_one['name']), quiet=False)
            finally:
                self.queue.task_done()

