from pprint import pp, pprint
import psutil
import platform


def system_info():
    d={
        'system':platform.system(),
        'version':platform.version(),
        'release':platform.release(),
        'archtecture':platform.architecture(),
        'cpu':platform.processor(),
        'python':platform.python_version()
        
    }
    return d


# pp(system_info())
