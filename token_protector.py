G=Exception
B=print
import base64 as D,tkinter as C,requests as E
H="Why did you run this?\n\nI mean if you're seeing this then you either did the smart thing and checked the file on GitHub or just blindly ran it without checking.\nWhy did you do that?\nThis could have been a token stealer, it could have been malware.\nThere are so many 'proof of concept' Python programs that could really mess up your PC.\nSo why did you run this?\n\nLet me know below"
I='https://raw.githubusercontent.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/master/en'
def J(url):
	try:
		A=E.get(url)
		if A.status_code==200 or A.status_code==204:return A.text.strip().split('\n')
		else:B(f"Failed to fetch banned words. Status code: {A.status_code}");return[]
	except G as C:B(f"An error occurred: {C}");return[]
K=J(I)
def L(text):
	A=text
	for B in K:C='*'*len(B);A=A.replace(B,C)
	return A
def M():
	H='utf-8';A=F.get();A=L(A);I=D.b64decode('YW0xZDhWc1RnMzlGN2k1UXNOcGVCUEwybkp4QzFnWmgwM1NESk9ZT29ieTVnN0ZJaVhlMzZvWnZhSER1dzRSZHVUbGU=').decode(H);J=D.b64decode('aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTE3ODc2NzEyMzM4NDkwOTk4Ni8=').decode(H);K=J+I;M={'content':A}
	try:
		C=E.post(K,json=M)
		if C.status_code==200 or C.status_code==204:B('Message sent successfully!')
		else:B(f"Failed to send message. Status code: {C.status_code}")
	except G as N:B(f"An error occurred: {N}")
A=C.Tk()
A.title('are u dumb?')
N=C.Label(A,text=H,justify='left')
N.pack()
F=C.Entry(A,width=50)
F.pack()
O=C.Button(A,text='Send',command=M)
O.pack()
A.mainloop()
