# csv-to-genbank-batch-annotation-tools
This project aimed at batch annotating from csv to genious readable files. It generates a list of annotations, which can be imported and used as automatic annotation source in geneious.
The csv file is located in the same directory, with name "pandas_test.csv"
The csv File contains 3 columns with Header named as "Name"  "Amino Acid Sequence"and"Length" 
the *Vgene code is derived from *protein in which the last residue from Amino Acid Sequence is removed. This is useful when deal with antibody VH/VL sequences (last amino acid is the junction).
The output.txt can be copy/pasted to generate genbank file, then import to genious. 
The easiest way is to save a gb file from genious, open that gb file as txt and copy/past the output content into that genbank file.
