import subprocess
import os

def get_volume_info():
    try:
        # Run the pamixer command to get volume information
        result = subprocess.run(['pamixer', '--get-volume'], capture_output=True, text=True, check=True)

        # Extract the volume information from the command output
        volume_info = result.stdout.strip()

        return volume_info
    except subprocess.CalledProcessError as e:
        # Handle any errors that occurred during the command execution
        print(f"Error: {e}")
        return None

# Get volume
volume = get_volume_info()
icon = os.path.expanduser('~/.local/share/icons/fontawesome/volume.svg ')

os.system("dunstify -a 'volume' -r 9993 -u low -h int:value:"+volume +" -i " + icon + volume + "% -t 1500 && play /usr/share/sounds/freedesktop/stereo/audio-volume-change.oga")
