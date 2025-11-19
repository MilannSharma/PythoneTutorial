import pyttsx3

# Initialize engine
engine = pyttsx3.init()

# Set Rate
rate = engine.getProperty('rate')
print("Current Rate:", rate)
engine.setProperty('rate', 125)

# Set Volume
volume = engine.getProperty('volume')
print("Current Volume:", volume)
engine.setProperty('volume', 1.0)

# Set Voice (Female if available)
voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)
else:
    print("Female voice not found, using default.")

# Queue all speech before running
engine.say("Hey Milan, I am ready to code")
engine.runAndWait()
engine.say("ok then start codeing")

# Run all queued speech
engine.runAndWait()

# Save to file (done after previous run finishes)
engine.save_to_file('Hello World', 'test.mp3')