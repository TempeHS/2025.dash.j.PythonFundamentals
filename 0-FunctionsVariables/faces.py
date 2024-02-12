# ask the user for their input
message = input(" write some emoji stuff, ")

message = (
    message.replace(":)", "🙂")
    .replace(":(", "🙁")
    .replace("⸨◺_◿⸩", "😡")
    .replace("chicken", "🐔")
)

print(message)
