
students = ['Ayesha Aslam', 'Dale Henion', 'Dipika Jayachander', 'Eman Metwally', 'Kathy Peticolas', 'Lindsay Soo', 'Lisette Dunham', 'Thomas Newlin', 'Victoria Rand', 'Luyao Zhang']

students.sort();

print(students);

html = ""

for student in students:
	name = student.split(" ")
#	print name
	pdf = ("http://miksa2.ils.unc.edu/chip/internship/files/presentations/pdf/"+name[0]+" "+name[1]+".pdf")
	jpg = ("http://miksa2.ils.unc.edu/chip/internship/files/presentations/thumbs/"+name[0]+" "+name[1]+".jpg")
	html += '<div class="listing"> \n \
	<div class="person">'+name[0]+' '+name[1]+'</div> \n \
	<div class="item"><a href="'+pdf+'" target="_blank"> \n \
	Poster: \n \
	<img alt="" src="'+jpg+'" /> \n \
	</a></div> \n \
	</div> \n \
';
file = open("output.html", "w")
file.write(html)
	
