This script provides a menu-driven interface for various tasks.

1. Import necessary libraries and modules.
2. Define the function `whatapp_message()` for sending WhatsApp messages.
   a. `mssage_detail()`: Get message content, delay, and repeat count.
      i. Get message and validate it's a string.
      ii. Get delay in seconds and validate it's an integer.
      iii. Get repeat count and validate it's an integer.
      iv. Call `message_send()` with provided details.
   b. `message_send(message, delay, repeat)`: Send messages with delay.
      i. Wait for 2 minutes before sending messages.
      ii. Loop for the specified repeat count.
      iii. Write and send the message with the specified delay.
      iv. Return to the main menu.
   c. Call `mssage_detail()` to initiate the process.

3. Define the function `stop_watch()` for a simple stopwatch.
   a. Define functions for start, pause, and reset operations.
   b. Define `update()` to update time and label every second.
   c. Create a tkinter GUI for the stopwatch.
   d. Set up buttons for start, pause, reset, and quit.
   e. Start the stopwatch main loop.

4. Define the function `text_to_speach()` to convert text to speech.
   a. Define `language_data` mapping for language codes.
   b. Allow the user to select a language and input method.
   c. If input is from a file:
      i. Get file address and read its content.
      ii. Convert the content to speech and save as an audio file.
      iii. Play the audio file.
   d. If input is direct text:
      i. Get input text and convert to speech.
      ii. Save and play the audio file.

5. Define the function `wifi_password()` to fetch Wi-Fi passwords.
   a. Run netsh command to get Wi-Fi profile names.
   b. Loop through profile names and fetch associated passwords.
   c. Print profile name and password pairs.

6. Define the function `word_cloud()` to generate a word cloud.
   a. Get input text.
   b. Generate a word cloud and display using matplotlib.

7. Define the function `language_detector()` to detect text language.
   a. Define language data mapping.
   b. Allow the user to select text input method.
   c. If input is from a file, read file content.
   d. Detect language using `langdetect` library.

8. Define the function `instagram_info()` to fetch Instagram user information.
   a. Define functions `laoder()` and `fetcher()` for loading and fetching data.
   b. Get Instagram username and fetch user information.
   c. Print user details and download user's pictures.

9. Define the function `img_to_pdf()` to convert images to PDF.
   a. Define `images_to_pdf()` to create a PDF from selected images.
   b. Define `image_selection()` and `pdf_slelction()` for user selections.
   c. Create a tkinter GUI for selecting images and PDF name.
   d. Convert selected images to a PDF file.

10. Define the function `phone_info()` to fetch information about a phone number.
    a. Define functions `number_colletion()` and `info_printing()` for user interactions.
    b. Get a phone number with a country code.
    c. Print timezone, service provider, and country information.

11. Define the function `display_menu()` to show the main menu and get user choice.
12. Define the main program `main()` that loops through user interactions based on choices.
13. Run the main program only when the script is executed directly.

This script provides a versatile menu-driven interface for performing various tasks, from sending WhatsApp messages to converting images to PDF and more.
