# Input Optimizer 🚀

**Windows utility for reducing input lag by optimizing mouse, keyboard, and system settings.**

## Features

* 🖱️ **Mouse Optimization** - Disables acceleration, improves polling
* ⌨️ **Keyboard Optimization** - Minimizes input lag
* ⚡ **Power Management** - Disables USB selective suspend
* 🎯 **System Tuneup** - High-performance power plan, disable background services

## Restore

`python restore.py`
**Restores default Windows settings.**

## Requirements

* Windows 10/11
* Python 3.6
* Administrator rights

## Registry Modifications

* **Mouse:** Disables acceleration (MouseSpeed=0, MouseThreshold=0)
* **Keyboard:** Disables special functions (FilterKeys, StickyKeys)
* **Power:** Disables USB/HID selective suspend
* **Drivers:** Increases mouse port limits

## System Changes

* **Power Scheme:** Sets the high-performance scheme
* **Services:** Disables tablet input, touch keyboard, and Windows search
* **USB:** Disables selective suspend via powercfg

## Files

* `main.py` - Main optimization script
* `restore.py` - Settings restore script
* `registry_config.py` - Configure all registry settings

## Security
* Requires administrator privileges (automatic UAC prompt)
* System files are not modified
* All changes are reversible via restore.py
* Uses standard Windows APIs

## Notes

* A reboot is required for full effect
* Gaming mouse software may override Some settings
* Some antivirus programs may flag registry changes
