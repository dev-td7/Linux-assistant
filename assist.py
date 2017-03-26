import os
name = raw_input("\nWhat should I call you? ---> ")
print "\nWelcome "+name+"! Tell me what you want."
cmd = ""
while "" in cmd:
	print "\n"
	cmd = raw_input("> ")
	cmd = cmd.lower()

	if cmd.startswith("launch") or cmd.startswith("open"): 

		where = cmd.find("h")
		if(cmd.startswith("open")): where = cmd.find("n")
		if(where == len(cmd)-1): continue
		what = cmd[ where + 1 : len(cmd) ]
		prefix = "DISPLAY=:0.0 google-chrome "

		if "somaiya mail" in what: out = os.system(prefix+"mail.somaiya.edu &")
		elif what in "mail": out = os.system(prefix+"mail.google.com &")
		elif "onedrive" in what: out = os.system(prefix+"onedrive.live.com &")
		elif "gdrive" in what or "drive" in what: out = os.system(prefix+"drive.google.com &")
		elif "maps" in what : out = os.system(prefix+"maps.google.com &")
		elif "images" in what: out = os.system(prefix+"images.google.com &")
		elif "classroom" in what: out = os.system(prefix+"classroom.google.com &")
		elif "chrome" in what:
			where = what.find("e")
			if where != len(what)-1:
				opt = what[where+1:len(what)]
				if "incognito" in opt or "private" in opt:
					out = os.system(prefix + "--incognito &")

			else: out  = os.system(prefix)
		elif "opera" in what:
			where = what.find("a")
			if where != len(what)-1:
				opt = what[where+1:len(what)]
				if "incognito" in opt or "private" in opt:
					out = os.system("DISPLAY=:0.0 opera --private &")
				else:
					out = os.system("opera "+opt+" &")
		
			else: out = os.system("DISPLAY=:0.0 opera &")
		elif "text editor" in what: out = os.system("DISPLAY=0.0 gedit &")
		elif "editor" in what: out = os.system("DISPLAY=0.0 gedit &")
		elif "system settings" in what or "settings" in what: out = os.system("unity-control-center &")
		else: out = os.system(prefix+what+".com &")

	elif "how to quit?" in cmd:
		print "Just type bye/quit/stop/exit and I will go.. Exiting.."
		break
	elif "hi" in cmd or "hey" in cmd or "hello" in cmd:
		print "Hi "+name+"! How are you?"
		ans = raw_input("\t> ")
		ans = ans.lower()
		if "bye" in  ans or "exit" in ans or "quit" in ans or "stop" in ans:
			print "Bye..!"
			break;
		else: print "\toh!"
	elif "how are you" in cmd or "how about you" in cmd:
		print "I am great!"
	elif "who are you" in cmd or "about" in cmd:
		print """I am a seemingly intelligent assistant built to execute commands to ease your task of opening websites and some supported applications.
			\nSay thanks to Tejas Dastane"""
	elif "bye" in  cmd or "exit" in cmd or "quit" in cmd or "stop" in cmd:
		print "Bye..!"
		break		
	elif "scholar" in cmd:
		where = cmd.find("r")
		what = cmd[where+1:len(cmd)]
		what = what.replace(' ','%20')
		url = "https://scholar.google.co.in/scholar?hl=en&q="+what+"&#"
		out = os.system("DISPLAY=:0.0 google-chrome "+url+" &")
	elif "help me" in cmd or "i need help" in cmd:
		print """I am programmed for these commands:
open: I can open 'editor', 'google chrome', 'opera', 'settings' or any other website for you. 
help/google/search: Google anything!
scholar: Search google scholar!
Also I can respond to 'Hi', 'How are you' and 'about'.

To stop me, use 'stop','quit','bye' or 'exit' or ask me 'how to quit?'

Try these now....\n"""
	elif "help" in cmd or "google" in cmd or "search" in cmd:
		where = cmd.find("p")
		if("google" in cmd): where = cmd.find("e")
		if("search" in cmd): where = cmd.find("h")
		what = cmd[where+1:len(cmd)]
		what = what.replace(' ','%20')
		url = "www.google.co.in/?gws_rd=ssl#q="+what+"&#"
		out = os.system("DISPLAY=:0.0 google-chrome "+url+" &")
	elif "ps" in cmd:
		print "Don't worry, I won't tell anyone :P"
	elif "i want you" in cmd:
		print "You have me already ;)"
	elif "tejas dastane" in cmd or "who created you" in cmd or "who is tejas" in cmd or "tejas" in cmd:
		print "Tejas Dastane is my creator.... :D"
	elif "" in cmd: pass
	else: print "I don't know what to do :( Maybe I will be programmed later to do so.."



