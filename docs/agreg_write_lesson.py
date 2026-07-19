src = open('nom_lecons.txt','r')
output = open('output.txt','w')
for l in src.readlines():

	output.write("<li> <a href='../docs/lecons_agreg/" + l[:3] + ".pdf' target='_blank'> " + l[:-1] + " </a></li>\n")

output.close()
src.close()
