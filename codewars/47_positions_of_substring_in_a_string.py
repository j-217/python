import re


def get_pos(base, strng, query):
    pattern_query = re.compile(r'{}.*?\n'.format(query))
    if re.search(pattern_query, base) is None:
        return "This query name does not exist in given Base"
    else:
        substring = re.search(pattern_query, base).group().split()[-1]
        convert_dict = {'R': '[G|A]', 'Y': '[C|T]', 'M': '[A|C]', 'K': '[G|T]', 'S': '[G|C]', 'W': '[A|T]', \
                        'B': '[C|G|T]', 'D': '[A|G|T]', 'H': '[A|C|T]', 'V': '[A|C|G]', 'N': '[A|C|G|T]'}
        for index, letter in enumerate(substring):
            if letter in convert_dict.keys():
                substring = substring.replace(letter, convert_dict[letter])
        pattern_substring = re.compile(r'{}'.format(substring))
        find_iter = re.finditer(pattern_substring, strng.upper())
        find_lst = [x.span()[0] + 1 for x in find_iter]
        if find_lst:
            return ' '.join(str(f) for f in find_lst)
        else:
            return "{} is not in given string".format(query)


Base = """Version xxxx                                             

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= 
Partial Database   
http://... 
Copyright (c) All rights reserved. 
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= 

<>

AaaI (XmaIII)                     CGGCCG 
AacI (BamHI)                      GGATCC 
AaeI (BamHI)                      GGATCC 
AagI (ClaI)                       ATCGAT 
AaqI (ApaLI)                      GTGCAC 
AarI                              NNNNNNNNGCAGGTG 
AatI (StuI)                       AGGCCT 
AatII                             GACGTC 
AauI (Bsp1407I)                   TGTACA 
AbaI (BclI)                       TGATCA 
AbeI (BbvCI)                      CCTCAGC 
AbrI (XhoI)                       CTCGAG 
AcaI (AsuII)                      TTCGAA 
AcaII (BamHI)                     GGATCC 
AcaIII (MstI)                     TGCGCA 
AcaIV (HaeIII)                    GGCC 
AccI                              GTMKAC 
AccII (FnuDII)                    CGCG 
AccIII (BspMII)                   TCCGGA 
Acc16I (MstI)                     TGCGCA 
Acc36I (BspMI)                    ACCTGCNNNN 
Acc38I (EcoRII)                   CCWGG 
Acc65I (KpnI)                     GGTACC 
Acc113I (ScaI)                    AGTACT 
AccB1I (HgiCI)                    GGYRCC 
AccB2I (HaeII)                    RGCGCY 
AccB7I (PflMI)                    CCANNNNNTGG 
AccBSI (BsrBI)                    CCGCTC 
AccEBI (BamHI)                    GGATCC 
AceI (TseI)                       GCWGC 
AceII (NheI)                      GCTAGC 
AceIII                            CAGCTCNNNNNNN 
AciI                              CCGC 
AclI                              AACGTT 
AclNI (SpeI)                      ACTAGT 
AclWI (BinI)                      GGATCNNNN"""

data="agatggcggcgctgaggggtcttgggggctctaggccggccacctactgg\
tttgcagcggagacgacgcatggggcctgcgcaataggagtacgctgcct\
gggaggcgtgactagaagcggaagtagttgtgggcgcctttgcaaccgcc\
tgggacgccgccgagtggtctgtgcaggttcgcgggtcgctggcgggggt\
cgtgagggagtgcgccgggagcggagatatggagggagatggttcagacc\
cagagcctccagatgccggggaggacagcaagtccgagaatggggagaat\
gcgcccatctactgcatctgccgcaaaccggacatcaactgcttcatgat\
cgggtgtgacaactgcaatgagtggttccatggggactgcatccggatca\
ctgagaagatggccaaggccatccgggagtggtactgtcgggagtgcaga\
gagaaagaccccaagctagagattcgctatcggcacaagaagtcacggga\
gcgggatggcaatgagcgggacagcagtgagccccgggatgagggtggag\
ggcgcaagaggcctgtccctgatccagacctgcagcgccgggcagggtca\
gggacaggggttggggccatgcttgctcggggctctgcttcgccccacaa\
atcctctccgcagcccttggtggccacacccagccagcatcaccagcagc\
agcagcagcagatcaaacggtcagcccgcatgtgtggtgagtgtgaggca\
tgtcggcgcactgaggactgtggtcactgtgatttctgtcgggacatgaa\
gaagttcgggggccccaacaagatccggcagaagtgccggctgcgccagt\
gccagctgcgggcccgggaatcgtacaagtacttcccttcctcgctctca\
ccagtgacgccctcagagtccctgccaaggccccgccggccactgcccac\
ccaacagcagccacagccatcacagaagttagggcgcatccgtgaagatg\
agggggcagtggcgtcatcaacagtcaaggagcctcctgaggctacagcc\
acacctgagccactctcagatgaggaccta"

s = "GCAGCaGCAGCgatggcggcgctgaggggtcttgggggctctaggccggccacctactgg"
q = 'AaeI'
# q = "AceI"
get_pos(Base, s, q)
