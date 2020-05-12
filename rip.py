# import python shell command
import os
playlist = "PLrLzMZ8AngYZixDVzkCgguvkwdhRdsNPF"
video = "videos"
music = "songs"
def mkdir(fname):
    print("checking if " + fname + " exists...")
    if not os.path.exists(fname):
        os.mkdir(fname)
        print("directory ", fname, " created...")
    else:
        print("directory ", fname, " already exists...")
mkdir(video)
mkdir(music)
cmd = "youtube-dl --no-check-certificate -f 'mp4' -i 'PLrLzMZ8AngYZixDVzkCgguvkwdhRdsNPF' -o '~/tuner/videos/%(title)s.%(ext)s' "
os.system(cmd)

#audioconvert -v convert ~/tuner/videos/ ~/tuner/songs/ -o .mp3
# read txt file of urls into a list
#txt = open('list.txt', 'r')
#urllist = txt.readlines()

#print("downloading :" + str(len(urllist)) + " files...")

# iterate through the list
#for url in urllist:
    # download the mp3 from url
#    cmd = "youtube-dl --no-check-certificate -f 'mp4' -i 'PLrLzMZ8AngYZixDVzkCgguvkwdhRdsNPF' -o '~/tuner/videos/%(title)s.%(ext)s' " + str(url)
#    os.system(cmd)
#https://www.youtube.com/playlist?list=PLrLzMZ8AngYZixDVzkCgguvkwdhRdsNPF 