from playsound import playsound
print("No.of available songs:5")
print(" 1.Telugu❤️ ❤️ ❤️ ❤️ ❤️ \n 2.Hindi🔥🔥🔥🔥🔥\n3.English💓💓💓💓💓\n 4.Tamil💛💛💛💛💛\n 5.Favourite BGM 💘💘💘💘💘  ")
song=input("enter the music which you want to play:")
if "1" in song:
    playsound('C:\\Users\\sivaj\\Downloads\\Yedurangula Vaana - 18 Pages ! Telugu Song.mp3')
elif "2" in song:
    playsound('C:\\Users\\sivaj\\Downloads\\Tu Maan Meri Jaan - Maan Meri Jaan - King ! Hindi Song.mp3')
elif "3" in song:
    playsound('C:\\Users\\sivaj\\Downloads\\Taki Taki - DJ Snake ! English Song.mp3')
elif "4" in song:
    playsound('C:\\Users\\sivaj\\Downloads\\Kaadhal En Kaviye -.mp3')
else:
    '''print("When we get bored of these songs just enjoy the BGM All time Favourite💜💜💜💜")'''
    playsound('C:\\Users\\sivaj\\Downloads\\Vellake - Alekhya Harika ! Bgm.mp3')