import pywhatkit

print("--- Send automatic WhatsApp ---")
print("")

wsp_number = input("Enter the WhatsApp number (ex: +56912345678): ")

wsp_message = input("Write the message to send: ")

time = input("Enter the exact time the message was sent (ex: 17:34): ").split(":")

hour = int(time[0])
minute = int(time[1])

print("")
print("Sending the message {} to the number {} at {}:{}.".format(wsp_message, wsp_number, hour, minute))
print("")

pywhatkit.sendwhatmsg(wsp_number, wsp_message, hour, minute, 5, False, True)





