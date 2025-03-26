import os

os.environ["PYFMODEX_STUDIO_DLL_PATH"] = f"{os. getcwd()}/fmodstudio.dll"
# The other dll (fmod.dll) is not required to be on the path. However, and I have no clue why,
# both dll's MUST be on the project folder, otherwise the next line breaks.

import pyfmodex.studio
system = pyfmodex.studio.StudioSystem()
system.initialize()
# Boilerplate

bank = system.load_bank_file("Master.bank")
# Loads the events from the bank file
system.load_bank_file("Master.strings.bank")
# Allows those events to be identified by keys instead of their GUID or something

music_reference = system.get_event("event:/music")
# Creates an event reference by looking up "event:/music" in the Strings bank
music_instance = music_reference.create_instance()
# Creates an instance of the "event:/music" event
music_instance.start()
# You'll never guess what this line does

while True:
    system.update()
    # This is required to run every tick. Otherwise, the event gets stuck on the STARTING playback state
    # This can be verified with     print(f"playback state is {music_instance.playback_state}")