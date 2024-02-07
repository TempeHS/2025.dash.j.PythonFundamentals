import time


# this creates an function with an argument
def repeat_message_with_delay(message, delay):
    words = message.split()
    for word in words:
        print(word)
        time.sleep(delay)


# input your words
message = input("Enter your message: ")
delay = float(input("Enter delay between words (in seconds): "))
repeat_message_with_delay(message, delay)
