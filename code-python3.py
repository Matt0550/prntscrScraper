#Credits to 'nazarpechka' for helping out with this code

import string, random, os, sys, _thread, httplib2, time, glob
# from PIL import Image

if len(sys.argv) < 2:
    sys.exit("\033[37mUsage: python3 " + sys.argv[0] + " (Number of threads)")
THREAD_AMOUNT = int(sys.argv[1])

print ("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=\nThis script is for educational purposes only! Use on your own responsibility!\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
input("Press ENTER if you have read and accept that you are fully responsible for using this script!\n")

INVALID = [0, 503, 5082, 4939, 4940, 4941, 12003, 5556, 5818]

def scrape_pictures(thread):
    while True:
        #url = 'http://img.prntscr.com/img?url=http://i.imgur.com/'
        url = 'http://i.imgur.com/'
        length = random.choice((5, 6))
        if length == 5:
            url += ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
        else:
            url += ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(3))
            url += ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(3))
            url += '.jpg'
            # print (url)
            directory = './output/'
            filename = url.rsplit('/', 1)[-1]

            file_path = os.path.join(directory, filename)
            if not os.path.isdir(directory):
                os.mkdir(directory)

            # print (filename)

            h = httplib2.Http(directory+'.cache' + thread)
            response, content = h.request(url)
            out = open(file_path, 'wb')
            out.write(content)
            out.close()

            file_size = os.path.getsize(file_path)
            if file_size in INVALID:
                print("[-] Invalid: " + url)
                os.remove(file_path)
            else:
                count = len(glob.glob1(directory,"*.jpg"))
                print(str(count) + ". [+] Valid: " + url)

for thread in range(1, THREAD_AMOUNT + 1):
    thread = str(thread)
    try:
        _thread.start_new_thread(scrape_pictures, (thread,))
    except:
        print('Error starting thread ' + thread)
print('Succesfully started ' + thread + ' threads.')

while True:
    time.sleep(1)
    
