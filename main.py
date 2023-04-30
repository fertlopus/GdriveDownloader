from workers.download_worker import DownloadWorker
from queue import Queue
import getfilelistpy.getfilelist as gt
import time
import json
THREAD_POOL_SIZE = 1


def get_files(secrets):
    res = gt.GetFileList(resource=secrets)
    file_list = res['fileList'][0]
    return file_list


def main():
    with open('./secrets/google_secrets.json', 'r') as file:
        resources = json.load(file)
        file.close()

    start_time = time.monotonic()
    files = gt.getfilelist(resources)
    # add files to the queue
    queue = Queue()
    for item in files['files']:
        queue.put(item)
    for i in range(THREAD_POOL_SIZE):
        worker = DownloadWorker("Thread {}".format(i+1), queue)
        worker.daemon = True
        worker.start()
    queue.join()
    end_time = time.monotonic()
    print("Total Time for processing files: {}".format(end_time - start_time))
    return None


if __name__ == "__main__":
    main()
