from youtubesearchpython import VideosSearch
from pytube import YouTube
import os
from termcolor import colored, cprint

n=5 #Cantidad de videos tomados como muestra
def get_duration(video_data_duration):
    l = len(video_data_duration)
    i=0
    m=''
    s=''
    if ':' in video_data_duration:
        while video_data_duration[i]!=':':
            m+=video_data_duration[i]
            i+=1
        i+=1
        while i<l:
            s+=video_data_duration[i]
            i+=1
        return (int(m)*60+int(s))
    else:
        return int(video_data_duration)
def best_option(name,artist,results):
    n=len(results)
    i=0
    best=0
    found = (name in results[i]['title'].upper()) and (artist in results[i]['title'].upper()) and ("AUDIO" in results[i]['title'].upper())
    while (not found) and (i<n):
        title = results[i]['title'].upper()
        if (len(results[i]['duration'])<=4):
            duration = get_duration(results[i]['duration'])
            if (name in title) and (artist in title) and duration <get_duration(results[best]['duration']):
                best=i
            i+=1
            found = (name in results[i]['title'].upper()) and (artist in results[i]['title'].upper()) and ("AUDIO" in results[i]['title'].upper())
        else:
            i+=1
        return best
def downloader(path):
    name = input('Name of the song: ').upper()
    artist = input('Name of the artist: ').upper()
    full_name= name+' '+artist+' '+'AUDIO'
    cprint('Searching...',"light_cyan")
    search = VideosSearch(full_name,limit=n)
    r=search.result()['result']
    i = best_option(name,artist,r)
    selected=r[i]
    cprint('Getting link...',"light_cyan")
    link=selected.get('link')
    print("Downloading video:",link)
    cprint("Processing...","light_cyan")
    video = YouTube(link)
    audio = video.streams.get_by_itag(140)
    print("==================================")
    file_name= input("Saved File name: ")+".mp3"
    audio.download(path,file_name)

        

def main():
    quit = False
    cprint("            ■■    ■■  ■■■■■■■■      ■■■■■■■■  ■■■■■■■■       ■■   ■■  ■■■■■■■  ■■■■■■■","light_green")
    cprint("             ■■  ■■      ■■            ■■     ■■    ■■       ■■■ ■■■  ■■    ■       ■■","light_green") 
    cprint("              ■  ■       ■■            ■■     ■■    ■■       ■■ ■ ■■  ■■    ■     ■■■ ","light_green")
    cprint("               ■■        ■■            ■■     ■■    ■■       ■■ ■ ■■  ■■ ■ ▀       ■■","light_green")
    cprint("               ■■        ■■            ■■     ■■    ■■       ■■   ■■  ■■            ■■","light_green")
    cprint("               ■■        ■■            ■■     ■■■■■■■■       ■■   ■■  ■■       ■■■■■■■","light_green")
    cprint("                             ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■","red")
    cprint("                           ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■","red")
    cprint("                           ■ ■ ■ ■ ■ ■ ■ ■     ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■","red")
    cprint("                           ■ ■ ■ ■ ■ ■ ■ ■         ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■","red")
    cprint("                           ■ ■ ■ ■ ■ ■ ■ ■             ■ ■ ■ ■ ■ ■ ■ ■ ■","red")
    cprint("                           ■ ■ ■ ■ ■ ■ ■ ■               ■ ■ ■ ■ ■ ■ ■ ■","red")
    cprint("                           ■ ■ ■ ■ ■ ■ ■ ■             ■ ■ ■ ■ ■ ■ ■ ■ ■","red")
    cprint("                           ■ ■ ■ ■ ■ ■ ■ ■         ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■","red")
    cprint("                           ■ ■ ■ ■ ■ ■ ■ ■     ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■","red")
    cprint("                           ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■","red")
    cprint("                             ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ","red")
    path=input('Saving path: ')
    while not quit:
        os.system('cls')
        cprint("            ■■    ■■  ■■■■■■■■      ■■■■■■■■  ■■■■■■■■       ■■   ■■  ■■■■■■■  ■■■■■■■","light_green")
        cprint("             ■■  ■■      ■■            ■■     ■■    ■■       ■■■ ■■■  ■■    ■       ■■","light_green") 
        cprint("              ■  ■       ■■            ■■     ■■    ■■       ■■ ■ ■■  ■■    ■     ■■■ ","light_green")
        cprint("               ■■        ■■            ■■     ■■    ■■       ■■ ■ ■■  ■■ ■ ▀       ■■","light_green")
        cprint("               ■■        ■■            ■■     ■■    ■■       ■■   ■■  ■■            ■■","light_green")
        cprint("               ■■        ■■            ■■     ■■■■■■■■       ■■   ■■  ■■       ■■■■■■■","light_green")
        cprint("                             ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■","red")
        cprint("                           ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■","red")
        cprint("                           ■ ■ ■ ■ ■ ■ ■ ■     ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■","red")
        cprint("                           ■ ■ ■ ■ ■ ■ ■ ■         ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■","red")
        cprint("                           ■ ■ ■ ■ ■ ■ ■ ■             ■ ■ ■ ■ ■ ■ ■ ■ ■","red")
        cprint("                           ■ ■ ■ ■ ■ ■ ■ ■               ■ ■ ■ ■ ■ ■ ■ ■","red")
        cprint("                           ■ ■ ■ ■ ■ ■ ■ ■             ■ ■ ■ ■ ■ ■ ■ ■ ■","red")
        cprint("                           ■ ■ ■ ■ ■ ■ ■ ■         ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■","red")
        cprint("                           ■ ■ ■ ■ ■ ■ ■ ■     ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■","red")
        cprint("                           ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■","red")
        cprint("                             ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ","red")
        print()
        downloader(path)
        cprint("Su archivo se ha guardado en:"+path,"dark_grey")
        ans=input("Desea Realizar otra descarga? (S/N): ")
        while (ans!="S") and (ans!="N"):
            ans=input("(S/N): ")
        if ans=="N":
            quit=True
            print("Cerrando Programa...")
    os.system('cls')

main()