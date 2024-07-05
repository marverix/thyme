
from time import sleep





def start():
    # Loop unless CTRL+C is pressed
    while True:
        try:
            locked = is_screen_locked()
            print(f"Screen is {'locked' if locked else 'unlocked'}")
            sleep(1)
        except KeyboardInterrupt:
            print("Exiting...")
            break


if __name__ == '__main__':
    start()
