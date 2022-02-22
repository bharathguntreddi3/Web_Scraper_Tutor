import urllib.request       # import the urllib.request library to download the content of the links

f = open('file_name.txt')   #file_name is the file where you copy all the extracted links or the destination of the located links

i = 1
for line in f:
    urllib.request.urlretrieve(line,f"D:/repo/scrap/sample_images/img_set/{i}.jpg")     #assign a folder where you want to store all the extracted images or the content with with each img name enclosed within {i}.jpg
    i+=1

