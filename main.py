import tkinter
t = tkinter.Tk()
t.title("Button coordinate")
#instructions
T = tkinter.Text(t, height=10, width=40)
T.place(x=10,y=950)
T.insert(tkinter.END,"Instructions:\n1.The display will appear after pressing\nthe buttons\n2.Input should be in the form xxxx+xxxx ex.0020+0035\n3.Maximum input is upto 4 digits\ni.e 9999")
#prints final output
def printf(ans):
	T = tkinter.Text(t, height=2, width=30)
	T.place(x=170,y=300)
	T.insert(tkinter.END,ans)
#performs main arithmetic operation	
def main(var1,var2,op):	
	if int(op)==1 :
		d1=int(var1)+int(var2)
		e1=int(d1)
		printf(e1)
	elif int(op)==2 :
		d2=int(var1)-int(var2)
		e2=int(d2)
		printf(e2)
	elif int(op)==3 :
		d3=int(var1)*int(var2)
		e3=int(d3)
		printf(e3)
	elif int(op)==4 :
		d4=int(var1)/int(var2)
		e4=int(d4)
		printf(e4)
	else :
		print('')
#takes numeric input	
def pros(x1):
	v1=T.get("1.0","1.4")
	v2=T.get("1.5","end-1c")
	main(v1,v2,x1)
#identify operation
def calc(iin):
	global b1
	global rs
	global rs1
	global rs2
	global rs3
	b1=iin
	rs=b1.find('+')
	rs1=b1.find('-')
	rs2=b1.find('×')
	rs3=b1.find('÷')
	if rs != -1 and rs1== -1 and rs2== -1 and rs3== -1:				
		pros(1)
	if rs == -1 and rs1!= -1 and rs2== -1 and rs3== -1:				
		pros(2)
	if rs == -1 and rs1== -1 and rs2!= -1 and rs3== -1:				
		pros(3)
	if rs == -1 and rs1== -1 and rs2== -1 and rs3!= -1:		
		pros(4)
#screen reader logic
def input():		
	in1=T.get("1.0",'end-1c')
	calc(in1)	
#input display logic
count=0
def dis(h):
	global count
	global a1
	global a2
	global a3
	global a4
	global a5
	global a6
	global a7
	global a8
	global a9
	global T
	count=count+1		
	if count==1:
		a1=h
		T = tkinter.Text(t, height=2, width=30)
		T.place(x=170,y=300)
		T.insert(tkinter.END,str(a1))
	if count==2:
		a2=h
		T = tkinter.Text(t, height=2, width=30)
		T.place(x=170,y=300)
		T.insert(tkinter.END,str(a1)+str(a2))
	if count==3:
		a3=h
		T = tkinter.Text(t, height=2, width=30)
		T.place(x=170,y=300)
		T.insert(tkinter.END,str(a1)+str(a2)+str(a3))
	if count==4:
		a4=h
		T = tkinter.Text(t, height=2, width=30)
		T.place(x=170,y=300)
		T.insert(tkinter.END,str(a1)+str(a2)+str(a3)+str(a4))
		
	if count==5:
		a5=h
		T = tkinter.Text(t, height=2, width=30)
		T.place(x=170,y=300)
		ab=str(a1)+str(a2)+str(a3)+str(a4)+str(a5)
		T.insert(tkinter.END,ab)
	if count==6:
		a6=h
		T = tkinter.Text(t, height=2, width=30)
		T.place(x=170,y=300)
		T.insert(tkinter.END,str(a1)+str(a2)+str(a3)+str(a4)+str(a5)+str(a6))
	if count==7:
		a7=h
		T = tkinter.Text(t, height=2, width=30)
		T.place(x=170,y=300)
		T.insert(tkinter.END,str(a1)+str(a2)+str(a3)+str(a4)+str(a5)+str(a6)+str(a7))
	if count==8:
		a8=h
		T = tkinter.Text(t, height=2, width=30)
		T.place(x=170,y=300)
		T.insert(tkinter.END,str(a1)+str(a2)+str(a3)+str(a4)+str(a5)+str(a6)+str(a7)+str(a8))
	if count==9:
		a9=h
		T = tkinter.Text(t, height=2, width=30)
		T.place(x=170,y=300)
		T.insert(tkinter.END,str(a1)+str(a2)+str(a3)+str(a4)+str(a5)+str(a6)+str(a7)+str(a8)+str(a9))		
	else:
		print('')
#input buttons
but1 = tkinter.Button(t, text="1",height=0,width=2,command=lambda:dis(1))
but1.place(x=50,y=1600)
but2 = tkinter.Button(t, text="2",height=0,width=2,command=lambda:dis(2))
but2.place(x=270,y=1600)
but3 = tkinter.Button(t, text="3",height=0,width=2,command=lambda:dis(3))
but3.place(x=490,y=1600)
but4 = tkinter.Button(t, text="4",height=0,width=2,command=lambda:dis(4))
but4.place(x=50,y=1750)
but5 = tkinter.Button(t, text="5",height=0,width=2,command=lambda:dis(5))
but5.place(x=270,y=1750)
but6 = tkinter.Button(t, text="6",height=0,width=2,command=lambda:dis(6))
but6.place(x=490,y=1750)
but7 = tkinter.Button(t, text="7",height=0,width=2,command=lambda:dis(7))
but7.place(x=50,y=1900)
but8 = tkinter.Button(t, text="8",height=0,width=2,command=lambda:dis(8))
but8.place(x=270,y=1900)
but9 = tkinter.Button(t, text="9",height=0,width=2,command=lambda:dis(9))
but9.place(x=490,y=1900)
butad = tkinter.Button(t, text="+",height=0,width=2,command=lambda:dis('+'))
butad.place(x=710,y=1600)
butsb = tkinter.Button(t, text="-",height=0,width=2,command=lambda:dis('-'))
butsb.place(x=710,y=1750)
butm = tkinter.Button(t, text="×",height=0,width=2,command=lambda:dis('×'))
butm.place(x=930,y=1600)
butd = tkinter.Button(t, text="÷",height=0,width=2,command=lambda:dis('÷'))
butd.place(x=930,y=1750)
but0 = tkinter.Button(t, text="0",height=0,width=2,command=lambda:dis(0))
but0.place(x=710,y=1900)
bute = tkinter.Button(t, text="=",height=0,width=2,command=input)
bute.place(x=930,y=1900)
buten= tkinter.Button(t, text="Exit",height=0,width=10,command=t.destroy)
buten.place(x=710,y=1450)	
t.mainloop()