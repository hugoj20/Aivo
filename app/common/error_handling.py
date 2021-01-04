class AppErrorBaseClass(Exception):
    pass

class ObjectNotFound(AppErrorBaseClass):
    pass

class IntegretyValueError(AppErrorBaseClass):
    pass