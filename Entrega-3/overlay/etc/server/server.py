from flask import Flask, render_template, request
import subprocess
import threading
import time
app = Flask(__name__)
aovivo = False
# Render the HTML form
@app.route('/')
def index():
    return render_template('index.html', result='')

# Handle form submission
@app.route('/', methods=['POST'])
def submit_text():
    user_text = request.form['user_text']
    # Run a program with the user's input
    global aovivo

    if (user_text == "live" and aovivo == False):
        aovivo = True
        start_thread()
        result = "Live started"
    elif (user_text == "live" and aovivo == True):
        aovivo = False
        result = "Live stopped"
    else :
        result = run_program(user_text)
    
    if (result == "1"):
        print("The led is On")
        result = "The led is On"
    elif (result == "0"):
        print("The led is Off")
        result = "The led is Off"
    elif (result == "ligou"):
        result = "Turn on command sent"
    elif (result == "desligou"):
        result = "Turn off command sent"
    if (aovivo == True):
        result = "Live started"
    elif (aovivo == False):
        result = "Live stopped"
    # Render the result page
    return render_template('index.html', result=result)
# Set desired options
resolution = "1920x1080"  # 1080p resolution
jpeg_quality = "95"  # JPEG image quality (0-100)
delay = "1"  # Delay in seconds before capture
skip_frames = "10"  # Skip frames to allow camera to stabilize

# Function to run a program
def run_program(input_text):
    # Replace this with your own program or command
    # Here, we'll just print the input text
    # make it run server_light(ELF  ) and return the output
    output = subprocess.check_output(['./etc/server/server_light', input_text])

    output2 = subprocess.check_output([
            '/usr/bin/fswebcam',
            '-r', resolution,
            '--jpeg', jpeg_quality,
            '-D', delay,
            '-S', skip_frames,
            '/etc/server/static/image.jpeg'
        ])
    return output.decode('utf-8').strip()
def init_live():
    global aovivo
    # create a thread to run the live
    
    while aovivo:
        output = subprocess.check_output([
                '/usr/bin/fswebcam',
                '-r', resolution,
                '--jpeg', jpeg_quality,
                '-D', delay,
                '-S', skip_frames,
                '/etc/server/static/image.jpeg'
            ])
        time.sleep(2)
    
    return output.decode('utf-8').strip()



def start_thread():
    background_thread = threading.Thread(target=init_live)
    background_thread.daemon = True
    background_thread.start()
    return "started"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)