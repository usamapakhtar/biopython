from Bio.Seq import Seq

#Generating the new sequences
dna_sequence= Seq("ATTGCATAC")
rna_sequence= Seq("AUUGCAUAC")
protein_sequence= Seq("MKLMH")

#Accesing the sequences
print("DNA Sequence:", dna_sequence)
print("RNA Sequence:", rna_sequence)
print("Protein Sequence:", protein_sequence)

print("______________________________")

#Length of the sequences
print("length of DNA sequence:", len(dna_sequence))
print("length of RNA sequence:", len(rna_sequence))
print("length of Protein sequence:", len(protein_sequence))

print("______________________________")



#Concatinating/Adding two sequences
seq1= Seq("ATCT")
seq2= Seq("AACTT")
seq3= seq1+seq2
print(seq3)

print("______________________________")

#Changing case of the sequence
example_seq= Seq("ATCggt")
print(example_seq.upper())
print(example_seq.lower())

print("______________________________")

#Transcription from DNA to RNA
print("DNA Sequence:", dna_sequence)
transcribed_seq= dna_sequence.transcribe()
print("Transcribed sequence:", transcribed_seq)

print("______________________________")

#Translation from RNA to Proteins
print(transcribed_seq)
translated_sequence= transcribed_seq.translate()
print(translated_sequence)

print("______________________________")

#Reverse Complement
print(dna_sequence)
rev_complement= dna_sequence.reverse_complement()
print(rev_complement)

print("______________________________")

#Reverse Complement RNA
print(dna_sequence)
rev_compl_rna= dna_sequence.reverse_complement_rna()
print(rev_compl_rna)

print("______________________________")

#sequence slicing
sequence_subset = dna_sequence[2:5]
print(sequence_subset)

#Nucleotide base count
base_count= dna_sequence.count("AT")
print(base_count)

#Finding a specific nucleotide base/base pair/ base sequence
nuleotide_base= rna_sequence.find("UGC")
print(nucleotide_base)


