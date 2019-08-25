import librosa
import numpy
import IPython.display as ipd

# To be noted 20-60 Hertz is sub-bass class which is felt more than it is heard. It denotes the power of Music
# The 60-250 Hz range is the bass class. 90Hz to 200Hz is the most commonly used Bass range in music industry


# Bass Beat duration is generally very small still tell us the tie duration for which you want to create a continuous bass tone
def BassCreator() :
    bass_freq = input("Choose The Wave Frequency you want to Add =>")
    bass_duration = input("Enter The Duration For which You want to Create Continuous Bass Beat")
    bass_tone = librosa.core.tone(int(bass_freq), sr=22050 , duration = int(bass_duration), phi=None)
    return bass_tone

#Sometimes We want to add a certain kind of beat pattern like (bass, timepause, bass, time pause, bass)
def Bass_Beats() :
    bass_freq = input("Which frequency Bass you wanna Experience ?")
    bass_beat_freq = input("How much bass beats must there be in a single signal ?")
    bass_beat_time = input("Enter Time Duration For Which each bass tone in bass beat must last")
    bass_beat_relax = input("Relaxation time in in between bass beats")
    bass_beat = librosa.core.tone(int(bass_freq), sr=22050, length = 22050*float(bass_beat_time), phi=None)
    bass_relax = librosa.core.tone(0, sr=22050, length=22050*float(bass_beat_relax), phi=None)
    cycle = numpy.concatenate((bass_relax, bass_beat))
    for x in range(0,int(bass_beat_freq)) :
        bass_beat = numpy.concatenate((bass_beat, cycle))
    return bass_beat

def LoadSong() :
    songpath = input("Input The Path of the song that you want to Add Bass To: ")
    song, sr = librosa.load(songpath)
    return song

def GetTime() :
    print("Enter Time Followed In format of Minutes Followed by Seconds Where Bass Is to Be added = >")
    minutes = input("Minutes:")
    seconds = input("Seconds:")
    return int(minutes*60 + seconds)

def BassComponentGenerator() :
    pre_bass_zero_sound = librosa.core.tone(0, sr=22050, duration=GetTime(), phi=None)
    bass_sound = BassSelection()    #BassSelection function will return us with a variable which will contain a signal 
    the_song = LoadSong() 
    print(the_song)
    print(pre_bass_zero_sound)
    print(bass_sound)
    post_bass_length_count = len(the_song)-len(pre_bass_zero_sound)-len(bass_sound)
    post_bass_zero_sound = librosa.core.tone(0, sr=22050, length=post_bass_length_count, phi=None)
    new_bass_component_temp = numpy.concatenate((pre_bass_zero_sound,bass_sound))
    new_bass_component = numpy.concatenate((new_bass_component_temp,post_bass_zero_sound))
    return new_bass_component+the_song

def BassSelection() :
    print("MENU")
    print("Enter 1 for Simple Monotonic Bass")
    print("Enter 2 for Bass Beats")
    choice = int(input("Your Choice Is => "))
    x=0
    if choice==1 :
        x = BassCreator()
    elif choice == 2 :
        x = Bass_Beats()
    return x

    # Call BassComponentGenerator() call the main thing
    edit_song = BassComponentGenerator()
    ipd.Audio(edit_song, rate=22050)