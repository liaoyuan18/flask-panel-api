from pprint import pp, pprint
import psutil
import platform


def system_info():
    d = {
        'system': platform.system(),
        'version': platform.version(),
        'release': platform.release(),
        'archtecture': platform.architecture(),
        'cpu': platform.processor(),
        'python': platform.python_version()
    }
    return d


def ram_info():
    m = psutil.virtual_memory()
    sm=psutil.swap_memory()
    d = {
        'used':m.used,
        'free':m.free,
        'total':m.total,
        'percent':m.percent,
        'swap':{
            'total':sm.total,
            'used':sm.used,
            'free':sm.free,
            'percent':sm.percent
        }
    }
    return d

# pp(system_info())
