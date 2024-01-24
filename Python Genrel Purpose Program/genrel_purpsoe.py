from langdetect import detect as d
from phonenumbers import carrier, geocoder, timezone
from wordcloud import WordCloud as cloud
from gtts import gTTS
from tkinter import filedialog,messagebox
from PIL import Image
from pygame import mixer
import time ,datetime ,pyautogui as p ,subprocess as sub ,instaloader as insta ,phonenumbers as ph ,matplotlib.pyplot as plt, tkinter as tk,os

def whatapp_message():
    def mssage_detail():
        message=input(str("what is the mesasge :"))
        while True:
            if isinstance(type(message),str):
                break
            else:
                print("enter string only")
                          
        delay=input(int(" delay between message in seconds:"))
        while True:
            if isinstance(type(delay),int):
                break
            else:
                print("enter intger only")

        repeat=input(int("how many times should it run:"))
        while True:
            if isinstance(type(repeat),int):
                break
            else:
                print("enter intger only")
            message_send(message,delay,repeat)
    def message_send(message,delay,repeat):
        print("There will be 2 minute  delay  open chat where the meagge will sent ")
        time.sleep(120)
        for i in range(repeat):
            p.write(message)
            time.sleep(delay)
            p.press("Enter")
            main()
    mssage_detail()

def stop_watch():
    timer_run=False
    hours, minutes, seconds = 0, 0, 0

    def start():
        global timer_run
        if not timer_run:
            update()
            timer_run = True

    # pause function
    def pause():
        global timer_run
        if timer_run:
            # cancel updating of time using after_cancel()
            stopwatch_label.after_cancel(time_update)
            timer_run = False

    # reset function
    def reset():
        global timer_run
        if timer_run:
            # cancel updating of time using after_cancel()
            stopwatch_label.after_cancel(time_update)
            timer_run = False
        # set variables back to zero
        global hours, minutes, seconds
        hours, minutes, seconds = 0, 0, 0
        # set label back to zero
        stopwatch_label.config(text='00:00:00')

    # update stopwatch function
    def update():
        # update seconds with (addition) compound assignment operator
        global hours, minutes, seconds
        seconds += 1
        if seconds == 60:
            minutes += 1
            seconds = 0
        if minutes == 60:
            hours += 1
            minutes = 0
        # format time to include leading zeros
        hours_string = f'{hours}' if hours > 9 else f'0{hours}'
        minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
        seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
        # update timer label after 1000 ms (1 second)
        stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
        # after each second (1000 milliseconds), call update function
        # use time_update variable to cancel or pause the time using after_cancel
        global time_update
        time_update = stopwatch_label.after(1000, update)


    stopwatch = tk.Tk()
    stopwatch.geometry('485x220')
    stopwatch.title('Stopwatch')
    stopwatch_label = tk.Label(text='00:00:00', font=('Arial', 80))
    stopwatch_label.pack()

    start_butt = tk.Button(text='start', height=5, width=7, font=('Arial', 20), command=start).pack(side=tk.LEFT)
    pause_button = tk.Button(text='pause', height=5, width=7, font=('Arial', 20), command=pause).pack(side=tk.LEFT)
    reset_button = tk.Button(text='reset', height=5, width=7, font=('Arial', 20), command=reset).pack(side=tk.LEFT)
    quit_button = tk.Button(text='quit', height=5, width=7, font=('Arial', 20), command=stopwatch.quit).pack(side=tk.LEFT)
    stopwatch.mainloop()

def text_to_speach():
    language_data = {
            'ar': 'Arabic', 'et': 'Armenian', 'art': 'Artificial Language',
            'sq': 'Albanian', 'bn': 'Bangla', 'bh': 'Bhojpuri',
            'bul': 'Bulgarian', 'cai': 'Central American Indian Language',
            'cze': 'Czech', 'dan': 'Danish', 'ger': 'German', 'eg': 'Egyptian', 'en': 'English',
            'fre': 'French', 'gon': 'Gondi', 'grc': 'Greek', 'gsw': 'Swiss German', 'hi': 'Hindi',
            'ind': 'Indonesian', 'ita': 'Italian', 'ja': 'Japanese', 'kn': 'Kannada',
            'kas': 'Kashmiri', 'geo': 'Georgian', 'kor': 'Korean', 'lat': 'Latin',
            'mar': 'Marathi', 'mni': 'Manipuri', 'mul': 'Multiple Languages', 'dut': 'Dutch',
            'te': 'Telugu', 'ta': 'Tamil', 'cy': 'Welsh'}
    print("Select a language:")
    for code, language in language_data.items():
        print(f"{code}: {language}")

    while True:

        selected_code = input("Enter the code of the language you want to select (or 'exit' to quit): ").strip().lower()

        if selected_code == 'exit':
            print("Exiting language selection.")
            break
        
        if selected_code in language_data:
            selected_language = language_data[selected_code]
            code=selected_code
            break
        else:
            print("Invalid language code. Please select a valid code.")
    print("enter 1 if u have txt file  or 2 if u have text ")
    while True:
        file_ans=input(":")
        if file_ans =="1":
            file_address = input(":")
            file_address = file_address.replace("\\", "/")  # Replace single backslashes with forward slashes
            file = open(file_address, "r")
            file = file.read().replace("\n", " ")
            audio = gTTS(text=file, lang=code, slow=False)
            audio.save("audio_output.mp3")
            os.system("start audio_output.mp3")
            break
        elif file_ans=="2":
            text=input("text:")
            audio = gTTS(text=text, lang=code, slow=False)
            audio.save("audio_output.mp3")
            os.system("start audio_output.mp3")
            break
        else:
            print("try again ")

def wifi_password():
    command_to_run = sub.check_output(['netsh', 'wlan', 'show', 'datas']).decode('utf-8').split('\n')
    ids = [i.split(":")[1][1:-1] for i in command_to_run if "All User data" in i]
    for i in ids:
        output = sub.check_output(['netsh', 'wlan', 'show', 'data', i, 'key=clear']).decode('utf-8').split('\n')
        output = [b.split(":")[1][1:-1] for b in output if "Key Content" in b]
        try:
            print ("{:<30}|  {:<}".format(i, output[0]))
        except IndexError:
            print ("{:<30}|  {:<}".format(i, ""))

    main()

def word_cloud():
    input_text=input("input :")
    wordcolud=cloud().generate(input_text)
    plt.imshow(wordcolud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def language_detector():
    codes={
    'ar': 'Arabic', 'et': 'Armenian', 'art': 'Artificial Langauge',
    'sq': 'Albanian','bn': 'Bangla', 'bh': 'Bhojpuri',
    'bul': 'Bulgarian', 'cai': 'Central American Indian Language',
    'cze': 'Caech', 'dan': 'Danish', 'ger': 'German', 'eg': 'Egyptian', 'en': 'English',
    'fre': 'french', 'gon': 'Gondi', 'grc': 'Greek', 'gsw': 'Swiss German', 'hi': 'Hindi',
    'ind': 'Indonesian', 'ita': 'Italian', 'ja': 'Japanese', 'kn': 'Kannada',
    'kas': 'Kashmiri', 'geo': 'Georgian', 'kor': 'Korean', 'lat': 'Latin',
    'mar': 'Marathi', 'mni': 'Manipuri', 'mul': 'Multiple Languages', 'dut': 'Dutch',
    'te': 'Telugu', 'ta': 'Tamil','cy':'Welsh'}

    print("Enter 1 if you have a txt file or 2 if you have text:")
    while True:
        file_ans = input(":")
        if file_ans == "1":
            file_address = input(":")
            file_address = file_address.replace("\\", "/")  # Replace single backslashes with forward slashes
            with open(file_address, "r", encoding="utf-8") as file:  # Use utf-8 encoding
                file_text = file.read().replace("\n", " ")
                print(d(file_text))
                break
        elif file_ans == "2":
            text = input("text:")
            print(d(text))
            break
        else:
            print("Try again")

def instagram_info():
    def laoder():
        loading_objeect=insta.instaloader()
        id=input("username:")
        fetcher(loading_objeect,id)

    def fetcher(loading_objeect,id):
        data=insta.data.from_username(loading_objeect.context,id)
        print("Username: ", data.username)
        print("Number of Posts Uploaded: ", data.mediacount)
        print(data.username+" is having " + str(data.followers)+' followers.')
        print(data.username+" is following " + str(data.followees)+' people')
        print("Bio: ", data.biography)
        insta.Instaloader().download_data(id,data_pic_only=True)
        main()

    laoder()

def img_to_pdf():

    def images_to_pdf(images, pdf_name):
        try:
            # create a new pdf file
            pdf = Image.open(images[0])
            pdf.save(pdf_name, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])
            messagebox.showinfo("Success", "Images have been successfully converted to PDF.")
        except Exception as e:
            messagebox.showerror("Error", "Failed to convert images to PDF.\nError: " + str(e))
    # function to select images
    def image_selection():
        images = filedialog.askopenfilenames(title="Select Images", filetypes=(("Image files", "*.jpg;*.jpeg;*.png"),("All files", "*.*")), initialdir = "C:/")
        return images
    # function to select pdf name and path
    def pdf_slelction():
        pdf = filedialog.asksaveasfilename(title="Save PDF As", defaultextension=".pdf", initialdir = "C:/", filetypes=(("PDF files", "*.pdf"),("All files", "*.*")))
        return pdf
    # create GUI



    root = tk.Tk()
    root.title(" Images to PDF")
    image_selection_btn = tk.Button(root, text="Select Images", command=image_selection)
    pdf_slelction_btn = tk.Button(root, text="Select PDF", command=pdf_slelction)
    convert_btn = tk.Button(root, text="Convert", command=lambda: images_to_pdf(image_selection(), pdf_slelction()))
    image_selection_btn.pack()
    pdf_slelction_btn.pack()
    convert_btn.pack()
    root.mainloop()

def phone_info():
    def number_colletion():
        number=input("Number with correct country  code:")
        parsed_number =ph.parse(number)
        info_printing(parsed_number)
    def info_printing(parsed_number):
        if ph.is_valid_number(parsed_number):
            print('Phone Number belongs to region :',timezone.time_zones_for_number(parsed_number))
            print('Service Provider : ',carrier.name_for_number(parsed_number,"en"))
            print('Phone number belongs to country : ',geocoder.description_for_number(parsed_number,"en"))
            main()
        else:
            print("Please enter valid mobile number")
            number_colletion()

    number_colletion()
       
def display_menu():
    print("Select an option:")
    print("1. Send WhatsApp message")
    print("2. Start stopwatch")
    print("3. Convert text to speech")
    print("4. Fetch Wi-Fi password")
    print("5. Generate word cloud")
    print("6. Detect language")
    print("7. Fetch Instagram information")
    print("8. Convert image to PDF")
    print("9. Fetch phone information")
    print("0. Exit")

    choice = input("Enter the number of your choice: ")
    return choice


def main():
    while True:
        choice = display_menu()

        if choice == '1':
            whatapp_message()
        elif choice == '2':
            stop_watch()
        elif choice == '3':
            text_to_speach()
        elif choice == '4':
            wifi_password()
        elif choice == '5':
            word_cloud()
        elif choice == '6':
            language_detector()
        elif choice == '7':
            instagram_info()
        elif choice == '8':
            img_to_pdf()
        elif choice == '9':
            phone_info()
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid number.")

if __name__ == "__main__":
    main()