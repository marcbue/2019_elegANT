from threading import Thread


def create_thread(func):
    """
    Creates and starts a thread for the given function
    :param func: function that should be executed in a thread
    :return: nothing
    """
    thread = Thread(target=func)
    thread.start()
