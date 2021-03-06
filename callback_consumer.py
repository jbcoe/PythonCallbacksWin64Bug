from ctypes import *
import platform

class Padding(Structure):
    _fields_ = [("_kind_id", c_int), ("xdata", c_int), ("data", c_void_p * 3)]

CallbackType = CFUNCTYPE(c_int, Padding, py_object)

if platform.system() == "Windows":
    library_path = "./callback_consumer.dll"
elif platform.system() == "Darwin":
    library_path = "./libcallback_consumer.dylib"
else:
    library_path = "./libcallback_consumer.so"

lib = cdll.LoadLibrary(library_path)

method_list = [
    ("callback_consumer_invoke", [CallbackType, Padding, py_object], None)
]

# library loading and method registrations
# based on clang python bindings approach


def register_method(lib, item):
    func = getattr(lib, item[0])

    if len(item) >= 2:
        func.argtypes = item[1]

    if len(item) >= 3:
        func.restype = item[2]


for m in method_list:
    register_method(lib, m)


def invoke(f, py_args):
    lib.callback_consumer_invoke(f, Padding(), py_args)
