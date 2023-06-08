print("Welcome To Satta Number Maker\n")
p1 = input("Enter The Previous Ander Haruf :\n")
p2 = input("Enter The Previous Bhahar Haruf :\n")
t1= input("Please Enter The Trend  [1-DIGIT] For " +  p1[0] +" :\n")
t2 = input("Please Enter The Trend  [1-DiIGIT] For " +  p2[0] +" :\n")
print("Thanks For Your Time❤️")
print("Here's Your Numbers❤️")

a = int(p1)
b = int(p1)
c = int(p2)
d = int(p2)
if int(t1) == 1:
	a1 = a+1+20
	a2 = a+6+20
	a3 = a-1+20
	a4 = a-6+20
	a5 = str(a1)
	a6 = str(a2)
	a7 = str(a3)
	a8 = str(a4)
	print(a5[1], a6[1], a7[1], a8[1])
elif int(t1) ==2:
	b1 = str(b+2+20)
	b2 = str(b+7+20)
	b3 = str(b-2+20)
	b4 = str(b-7+20)
	print(b1[1], b2[1], b3[1], b4[1])
else:
	print('You Have Put The Wrong trend No. It has to be 1 or 2 For "Ander Haruf" ')

if int(t2) ==1:
	c1 = c+1+20
	c2 = c+6+20
	c3 = c-1+20
	c4 = c-6+20
	c5 = str(c1)
	c6 = str(c2)
	c7 = str(c3)
	c8 = str(c4)
	print(c5[1], c6[1], c7[1], c8[1])

elif int(t2) ==2:
	d1 = str(d+2+20)
	d2 = str(d+7+20)
	d3 = str(d-2+20)
	d4 = str(d-7+20)
	print(d1[1], d2[1], d3[1], d4[1])
else:
	print('You Have Put The Wrong trend No. It has to be 1 or 2 For "Bahar Haruf" ')

if int(t1) ==1 and int(t2)== 1:
	a1 = a+1+20
	a2 = a+6+20
	a3 = a-1+20
	a4 = a-6+20
	a5 = str(a1)
	a6 = str(a2)
	a7 = str(a3)
	a8 = str(a4)
	c1 = c+1+20
	c2 = c+6+20
	c3 = c-1+20
	c4 = c-6+20
	c5 = str(c1)
	c6 = str(c2)
	c7 = str(c3)
	c8 = str(c4)
	x = str(a+5+20)
	y = str(c + 5 +20)
	p1 = str(p1)
	p2 = str(p2)
	print(a5[1]+c5[1],a5[1]+c6[1],a5[1]+c7[1],a5[1]+c8[1]+"\n"+a6[1]+c5[1],a6[1]+c6[1],a6[1]+c7[1],a6[1]+c8[1]+"\n"+a7[1]+c5[1],a7[1]+c6[1],a7[1]+c7[1],a7[1]+c8[1]+"\n"+a8[1]+c5[1],a8[1]+c6[1],a8[1]+c7[1],a8[1]+c8[1]+"\n"+ "\n" + p1+c5[1],p1+c6[1],p1+c7[1],p1+c8[1]+"\n"+a5[1]+p2,a6[1]+p2,a7[1]+p2,a8[1]+p2+"\n"+p1+p2,x[1]+y[1])
elif int(t1) ==1 and int(t2) ==2:
	a1 = a+1+20
	a2 = a+6+20
	a3 = a-1+20
	a4 = a-6+20
	a5 = str(a1)
	a6 = str(a2)
	a7 = str(a3)
	a8 = str(a4)
	d1 = str(d+2+20)
	d2 = str(d+7+20)
	d3 = str(d-2+20)
	d4 = str(d-7+20)
	x = str(a+5+20)
	y = str(d + 5 +20)
	p1 = str(p1)
	p2 = str(p2)
	print(a5[1]+d1[1],a5[1]+d2[1],a5[1]+d3[1],a5[1]+d4[1]+"\n"+a6[1]+d1[1],a6[1]+d2[1],a6[1]+d3[1],a6[1]+d4[1]+"\n"+a7[1]+d1[1],a7[1]+d2[1],a7[1]+d3[1],a7[1]+d4[1]+"\n"+a8[1]+d1[1],a8[1]+d2[1],a8[1]+d3[1],a8[1]+d4[1]+"\n"+ "\n" + p1+d1[1],p1+d2[1],p1+d3[1],p1+d4[1]+"\n"+a5[1]+p2,a6[1]+p2,a7[1]+p2,a8[1]+p2+"\n"+p1+p2,x[1]+y[1])

elif int(t1) ==2 and int(t2) ==1:
	b1 = str(b+2+20)
	b2 = str(b+7+20)
	b3 = str(b-2+20)
	b4 = str(b-7+20)
	c1 = c+1+20
	c2 = c+6+20
	c3 = c-1+20
	c4 = c-6+20
	c5 = str(c1)
	c6 = str(c2)
	c7 = str(c3)
	c8 = str(c4)
	x = str(b+5+20)
	y = str(c + 5 +20)
	p1 = str(p1)
	p2 = str(p2)
	print(b1[1]+c5[1],b1[1]+c6[1],b1[1]+c7[1],b1[1]+c8[1]+"\n"+b2[1]+c5[1],b2[1]+c6[1],b2[1]+c7[1],b2[1]+c8[1]+"\n"+b3[1]+c5[1],b3[1]+c6[1],b3[1]+c7[1],b3[1]+c8[1]+"\n"+b4[1]+c5[1],b4[1]+c6[1],b4[1]+c7[1],b4[1]+c8[1]+"\n"+ "\n" + p1+c5[1],p1+c6[1],p1+c7[1],p1+c8[1]+"\n"+b1[1]+p2,b2[1]+p2,b3[1]+p2,b4[1]+p2+"\n"+p1+p2,x[1]+y[1])
	
elif int(t1) == 2 and int (t2)==2:
	b1 = str(b+2+20)
	b2 = str(b+7+20)
	b3 = str(b-2+20)
	b4 = str(b-7+20)
	d1 = str(d+2+20)
	d2 = str(d+7+20)
	d3 = str(d-2+20)
	d4 = str(d-7+20)
	x = str(b+5+20)
	y = str(d+ 5 +20)
	p1 = str(p1)
	p2 = str(p2)
	print(b1[1]+d1[1],b1[1]+d2[1],b1[1]+d3[1],b1[1]+d4[1]+"\n"+b2[1]+d1[1],b2[1]+d2[1],b2[1]+d3[1],b2[1]+d4[1]+"\n"+b3[1]+d1[1],b3[1]+d2[1],b3[1]+d3[1],b3[1]+d4[1]+"\n"+b4[1]+d1[1],b4[1]+d2[1],b4[1]+d3[1],b4[1]+d4[1]+"\n"+ "\n" + p1+d1[1],p1+d2[1],p1+d3[1],p1+d4[1]+"\n"+b1[1]+p2,b2[1]+p2,b3[1]+p2,b4[1]+p2+"\n"+p1+p2,x[1]+y[1])


print("THANKS FOR USING OUR SERVICE ❤️❤️")
	
	
	
	
	
	

	
	
	
	
	
	
	


	
	
