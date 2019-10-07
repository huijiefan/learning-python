fish_record = 'ABC5,ABD8,ABF7,ABG2,ABH6,ABI1'
step = 3
print(len(fish_record))
record_len = len(fish_record)
i = 0
while i < record_len:
    if fish_record[i:i+step] == 'ABI':
        if int(fish_record[i+step]) % 2 == 0:
            print("找到乌龟了，是%d只，偶数" % (int(fish_record[i+step])))
        else:
            print("找到乌龟了，是%d只，奇数" % (int(fish_record[i+step])))
    i += 5
