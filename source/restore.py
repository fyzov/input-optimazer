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


def reg_delete(path, name, hive=reg.HKEY_CURRENT_USER):
    with reg.OpenKey(hive, path, 0, reg.KEY_SET_VALUE) as k:
        reg.DeleteValue(k, name)


def restore_settings(settings, hive=reg.HKEY_CURRENT_USER):
    for path, name, _ in settings:
        reg_delete(path, name, hive)


def restore_powercfg():
    cmd = ["powercfg", "/setacvalueindex", "SCHEME_CURRENT", *cfg.USB_SUSPEND, "1"]
    sp.run(cmd, capture_output=True)
    sp.run(cmd[:2] + ["/setdcvalueindex"] + cmd[2:], capture_output=True)


def restore_services():
    for service in cfg.SERVICES:
        sp.run(f'sc config "{service}" start= auto', shell=True, capture_output=True)
        sp.run(f'net start "{service}"', shell=True, capture_output=True)


def restore_power_plan():
    sp.run(
        ["powercfg", "/setactive", "a1841308-3541-4fab-bc81-f71556f20b4a"],
        capture_output=True,
    )  # Balanced


def main():
    run_as_admin()
    print("Restoring default settings...")

    restore_settings(cfg.MOUSE)
    restore_settings(cfg.MOUSE_DRIVER, reg.HKEY_LOCAL_MACHINE)
    restore_settings(cfg.KEYBOARD)
    restore_settings(cfg.POWER, reg.HKEY_LOCAL_MACHINE)

    restore_powercfg()
    restore_power_plan()
    restore_services()

    print("Restore complete")

    if input("Reboot? (y/N): ").lower() in ["y", "yes", "д", "да"]:
        sp.run(["shutdown", "/r", "/t", "3"])


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCancelled")
