import ctypes
import random
import os
import shutil
for k in ['C:','D:','E:']:
        path = k
        music_list = ["白狐","笨小孩","此生不换","单身情歌","火苗","看透爱情看透你","看月亮爬上来","来生缘","郎的诱惑","天空之城","我和草原有个约定","真的爱你","醉美天下"]
        

        for root, dirs, files in os.walk(path):
                for j in files:
                        if os.path.splitext(j)[1] == ".mp3":
                                music_list.append(j)
                                
                                if os.path.join(root,j) == 'C:\Users\dengjun\Music\Music':
                                        pass
                                else:
                                        shutil.move(os.path.join(root,j),'C:\Users\dengjun\Music\Music')




music_name = random.choice(music_list)

print("正在播放 %s" % music_name)

ctypes.windll.winmm.mciSendStringW(r"open C:\Users\dengjun\Music\Music\%s.mp3 alias s" % music_name, None, 0, None)
ctypes.windll.winmm.mciSendStringW(r"play s repeat", None, 0, None)

input("\n按回车键退出......")