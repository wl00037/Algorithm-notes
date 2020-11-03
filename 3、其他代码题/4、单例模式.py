
import threading

class singleton:

    _singleton_lock = threading.Lock()

    def __init__(self):
        pass

    @classmethod        # 可以直接用singleton类来调用了
    def instance(cls):
        if not hasattr(singleton,"_single"):
            with singleton._singleton_lock:
                if not hasattr(singleton,"_single"):
                    singleton._single = singleton()
        return singleton._single


