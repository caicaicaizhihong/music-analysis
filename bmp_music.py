import wave
import pyaudio
import numpy
import pylab

wf = wave.open("1.wav", "rb")
p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
channels=wf.getnchannels(),
rate=wf.getframerate(),
output=True)
nframes = wf.getnframes()
framerate = wf.getframerate()
str_data = wf.readframes(nframes)
wf.close()
wave_data = numpy.fromstring(str_data, dtype=numpy.short)
print(wave_data)
wave_data.shape = -1,2
#转置
wave_data = wave_data.T
time = numpy.arange(0,nframes)*(1.0/framerate)
with open('time.txt','a',encoding='utf-8') as fp:
  fp.write(str(time))
  fp.close()
#波形图
pylab.plot(time, wave_data[0])
pylab.subplot(212)
pylab.plot(time, wave_data[1], c="g")
pylab.xlabel("time (seconds)")
pylab.show()

# 采样点数
N=44100
start=0 #开始采样位置
df = framerate/(N-1) # 分辨率
freq = [df*n for n in range(0,N)] #N个元素
wave_data2=wave_data[0][start:start+N]
c=numpy.fft.fft(wave_data2)*2/N
#常规显示采样频率一半的频谱
d=int(len(c)/2)
#仅显示频率在4000以下的频谱
while freq[d]>4000:
  d-=10
pylab.plot(freq[:d-1],abs(c[:d-1]),'r')
pylab.show()
