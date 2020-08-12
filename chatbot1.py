prev_msgs = []

msg = input("> ")
while msg != "stop":
  highest_msg = False
  for prev_msg in prev_msgs:
    score = 0
    for word in prev_msg.split(" "):
      for current_word in msg.split(" "):
        if word == current_word:
          score = score + 1
    if highest_msg == False:
      if score > 0:
        highest_msg = (score, prev_msg)
    elif score > highest_msg[0]:
      highest_msg = (score, prev_msg)

  prev_msgs.append(msg)

  if highest_msg == False:
    print("I have no reply, but go on...")
  else:
    print(highest_msg[1])

  msg = input("> ")
