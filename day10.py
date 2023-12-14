fl=open('codon.txt','r')
f=fl.readlines()
codon_dict={}
for i in range(len(f)):
    codon,animo=f[i].split()
    if len(codon)==3:
        codon_dict[codon]=animo
def transcript(sequence):
    am={"A":"U","T":"A","C":"G","G":"C"}
    rna=''
    for i in range(len(sequence)):
        rna+=am[sequence[i]]
    return rna
def translate(dna,condn_dict):
    rna=transcript(dna)
    start = "AUG"
    protein = ""
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if codon == start:
            protein += codon_dict[codon]
        elif codon_dict[codon] == "stop":
            break
        else:
            protein += codon_dict[codon]
    return protein
seq_dict={}
file = open('seq.fa','r')
name = ''
content = ''
f = file.readlines()
for l in f:
  l = l.strip('\n')
  if(l.startswith('>')):
    l = l.strip('>')
    name = l
  else:
    content = l
    seq_dict[name] = content
protein_dict = {}
for i in seq_dict:
  protein_dict[i] = translate(seq_dict[i])
print(protein_dict)