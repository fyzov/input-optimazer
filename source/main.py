import ctypes
import subprocess as sp
import sys
import winreg as reg

import registry as cfg


def run_as_admin():
    if not ctypes.windll.shell32.IsUserAnAdmin():
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        sys.exit()


def reg_set(path, name, value, hive=reg.HKEY_CURRENT_USER):
    with reg.OpenKey(hive, path, 0, reg.KEY_SET_VALUE) as k:
        reg.SetValueEx(
            k, name, 0, reg.REG_DWORD if isinstance(value, int) else reg.REG_SZ, value
        )


def apply_settings(settings, hive=reg.HKEY_CURRENT_USER):
    return [reg_set(*s, hive) for s in settings]


def powercfg(value="0"):
    cmd = ["powercfg", "/setacvalueindex", "SCHEME_CURRENT", *cfg.USB_SUSPEND, value]
    sp.run(cmd, capture_output=True)
    sp.run(cmd[:2] + ["/setdcvalueindex"] + cmd[2:], capture_output=True)


def high_performance():
    scheme = (
        "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"
        if "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"
        in sp.run(["powercfg", "/list"], capture_output=True, text=True).stdout
        else "381b4222-f694-41f0-9685-ff5bb260df2e"
    )
    sp.run(["powercfg", "/setactive", scheme], capture_output=True)


def stop_services():
    return [
        sp.run(
            f'net stop "{s}" & sc config "{s}" start= disabled',
            shell=True,
            capture_output=True,
        )
        for s in cfg.SERVICES
    ]


def main():
    run_as_admin()
    print("Applying optimizations...")

    apply_settings(cfg.MOUSE)
    apply_settings(cfg.MOUSE_DRIVER, reg.HKEY_LOCAL_MACHINE)
    apply_settings(cfg.KEYBOARD)
    apply_settings(cfg.POWER, reg.HKEY_LOCAL_MACHINE)

    powercfg()
    high_performance()
    stop_services()

    print("Optimization complete")

    if input("Reboot? (y/N): ").lower() in ["y", "yes", "д", "да"]:
        sp.run(["shutdown", "/r", "/t", "3"])


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Cancelled")
