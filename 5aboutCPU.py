import psutil

cpu = psutil.cpu_freq() #cpu 속도
cpu_current_gpz = round(cpu.current / 1000, 2)
print(f'cpu속도 : {cpu_current_gpz}')
cpu_core = psutil.cpu_count(logical = False) #물리코어 수
print(f'cpu 코어 ": {cpu_core}')

memory = psutil.virtual_memory() #메모리 정보
memory_total = round(memory.total / 1024**3)

disk = psutil.disk_partitions() #디스크 정보
for p in disk :
  print(p.mountpoint, p.fstype, end=' ')
  du = psutil.disk_usage(p.mountpoint)
  disk_total = round(du.total/1024**3)
  print(f'disk크기 : {disk_total}GB')


count = 0
while True : 
  cpu_p = psutil.cpu_percent(interval=1)
  print(f'cpu사용량 : {cpu_p}%')

  memory_avail = round(memory.available/1024**3,1)
  print(f'메모리: {memory_total}GB, 사용가능한 메모리 : {memory_avail}GB')

  net = psutil.net_io_counters() #데이터를 통해 보내고 받은 데이터량
  sent = round(net.bytes_sent/1024**2,1)
  recv = round(net.bytes_recv/1024**2,1)
  print(f'보내기: {sent}MB, 받기: {recv}MB')

  count += 1
  if count >=10 :
    break


# print(f'''cpu : {cpu}
# cpu_core : {cpu_core}
# memory : {memory}
# disk : {disk}
# net : {net}
# ''')
