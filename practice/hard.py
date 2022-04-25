# 查看電腦記憶體
import psutil as ps
import os

info = ps.virtual_memory()
total = (info.total) / 1024 / 1024 / 1024
print(u'總記憶體:', "{:.2f}".format(total), 'GB')
# print(u'記憶體使用:', ps.Process(os.getpid()).memory_info().rss)
print(u'記憶體使用:', "{:.2f}".format((info.used) / 1024 / 1024 / 1024), 'GB')
print(u'記憶體占比:', info.percent, '%')

# print(ps.virtual_memory())

# 查看電腦cpu
cpu_percent = ps.cpu_percent(interval=1, percpu=True)
print("cpu_percent:", cpu_percent)
cpu_freq = ps.cpu_freq()
print("cpu_freq:", cpu_freq)
