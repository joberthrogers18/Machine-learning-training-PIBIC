# Import the AudioSegment class for processing audio and the 
# split_on_silence function for separating out silent chunks.
from pydub import AudioSegment
from pydub.silence import split_on_silence

# Define a function to normalize a chunk to a target amplitude.
def match_target_amplitude(aChunk, target_dBFS):
    ''' Normalize given audio chunk '''
    change_in_dBFS = target_dBFS - aChunk.dBFS
    return aChunk.apply_gain(change_in_dBFS)

# Load your audio.
song = AudioSegment.from_ogg("teste.ogg")

# Split track where the silence is 2 seconds or more and get chunks using 
# the imported function.
chunks = split_on_silence(
    # Use the loaded audio.
    song,

    # split on silences longer than 1000ms (1 sec)
    min_silence_len=150,

    # anything under -16 dBFS is considered silence
    silence_thresh=-16, 

    # keep 200 ms of leading/trailing silence
    keep_silence=50
)

# now recombine the chunks so that the parts are at least 90 sec long
target_length = 
output_chunks = [chunks[0]]
for chunk in chunks[1:]:
    if len(output_chunks[-1]) < target_length:
        output_chunks[-1] += chunk
    else:
        # if the last output chunk is longer than the target length,
        # we can start a new one
        output_chunks.append(chunk)


# Process each chunk with your parameters
for i, chunk in enumerate(output_chunks):

    # Normalize the entire chunk.
    #normalized_chunk = match_target_amplitude(chunk, -20.0)

    # Export the audio chunk with new bitrate.
    print("Exporting chunk{0}.mp3.".format(i))
    chunk.export(
        "./audios/chunk{0}.mp3".format(i),
        bitrate = "192k",
        format = "mp3"
    )