from threading import Thread


def create_thread(func, args):
    """
    Creates and starts a thread for the given function
    :param func: function that should be executed in a thread
    :param args: keywords passed to tge function
    :return: nothing
    """
    thread = Thread(target=func, args=args)
    thread.start()
