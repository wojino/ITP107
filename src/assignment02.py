import wave, struct
import math

def read_audio(filename):
    with wave.open(filename, 'rb') as r:
        return [ f[0] / 32768 for f in struct.iter_unpack('<h', r.readframes(r.getnframes())) ]

def write_audio(filename, audio):
    with wave.open(filename, 'wb') as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(48000)
        for f in audio:
            w.writeframes(struct.pack('<h', int(f * 32767)))

def amplification(audio, amp):
    new_audio = []
    for i in audio:
        tmp = i * amp
        if tmp > 1.0:
            tmp = 1.0
        elif tmp < -1.0:
            tmp = -1.0
        new_audio.append(tmp)

    return new_audio

def linear_interpolation(list, value):
    hi = math.floor(value) + 1
    lo = math.floor(value)
    result = (value - lo) * list[hi] + (hi - value) * list[lo]

    return result

def speed_up(audio, spd):
    new_length = int(len(audio) / spd)
    audio.append(0)

    new_audio = []
    for i in range(new_length):
        new_audio.append(linear_interpolation(audio, i * spd))

    return new_audio

amp = float(input('Type an Amplification Factor: '))
spd = float(input('Type a Speed Factor: '))

input_audio = read_audio('inp.wav')

output_audio = amplification(input_audio, amp)
output_audio = speed_up(output_audio, spd)

write_audio('out.wav', output_audio)
