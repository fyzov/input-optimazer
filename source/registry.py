MOUSE = [
    ("Control Panel\\Mouse", "MouseSpeed", "0"),
    ("Control Panel\\Mouse", "MouseThreshold1", "0"),
    ("Control Panel\\Mouse", "MouseThreshold2", "0"),
]

MOUSE_DRIVER = [
    ("SYSTEM\\CurrentControlSet\\Services\\mouclass\\Parameters", "ConnectMultiplePorts", 1),
    ("SYSTEM\\CurrentControlSet\\Services\\mouhid\\Parameters", "MaximumPortsServiced", 20),
]

KEYBOARD = [
    ("Control Panel\\Accessibility\\Keyboard Response", "Flags", "0"),
    ("Control Panel\\Accessibility\\StickyKeys", "Flags", "0"),
]

POWER = [
    ("SYSTEM\\CurrentControlSet\\Enum\\HID", "AllowIdleIrpInSelectiveSuspend", 0),
    ("SYSTEM\\CurrentControlSet\\Enum\\HID", "SelectiveSuspendEnabled", 0),
    ("SYSTEM\\CurrentControlSet\\Services\\USB", "DisableSelectiveSuspend", 1),
    ("SYSTEM\\CurrentControlSet\\Services\\USBSTOR", "DisablePowerManagement", 1),
]

SERVICES = ["TabletInputService", "TouchKeyboardAndHandwritingPanelService", "WSearch"]
USB_SUSPEND = ['2a737441-1930-4402-8d77-b2bebba308a3', '48e6b7a6-50f5-4782-a5d4-53bb8f07e226']
