import pandas as pd
#this will remove the last residue of a sequence (junction), corrects the sequence length for annotations.
df = pd.read_csv("pandas_test.csv", usecols=['Name', 'Length','Amino Acid Sequence'])
result = df.to_dict(orient='records')
for row in result:
	name = row ["Name"]
	len = row ["Length"]
	seq = row ["Amino Acid Sequence"]
	print("LOCUS       "+ name+ "          "+str(len-1)+ " aa            linear   UNA 16-APR-2020")
	print("DEFINITION  .")
	print("ACCESSION   urn.local...5w-bt622qe")
	print("VERSION     urn.local...5w-bt622qe")
	print("KEYWORDS    .")
	print("SOURCE      ")
	print("  ORGANISM  .")
	print("COMMENT     ##Imported_From-START##")
	print("            Path     :: C:\\Users\\lzhou\\Geneious 2019.1 Data\\temp\\22")
	print("            Filename :: Clipboard Contents 3")
	print("            ##Imported_From-END##")
	print("FEATURES             Location/Qualifiers")
	print("     misc_feature    1.."+str(len-1))
	print("          /created_by=\"lzhou\"")
	print("          /label=\""+name+"\"")
	print("ORIGIN")      
	print("        1 "+seq[:-1])
	print("//")