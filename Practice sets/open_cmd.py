import os

def open_cmd():
    try:
        os.system("start cmd")  # This will open CMD in a new window
        print("CMD should now be open.")
    except Exception as e:
        print(f"Failed to open CMD: {e}")

if __name__ == "__main__":
    open_cmd()





