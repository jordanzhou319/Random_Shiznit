va = int(input('Number of introns: '))
gi = input('DNA Sequence: ')

na = 1
fucking = 1
stupid = 0
pirate_hooker = 2

whore_island = gi.replace(' ','')
mantooth = ''.join(i for i in whore_island if not i.isdigit())

penetration = []
printers = []

for blue_waffle in range(0,va):
    blue = int(input('Beginning of intron ' + str(na) + ': '))
    penetration.append(blue-1)
    waffle = int(input('End of intron ' + str(na) + ': '))
    printers.append(waffle)
    na += 1

print('\n')

if va == 1:
    trump = mantooth[:penetration[0]] + mantooth[printers[0]:]
    print('Exon: ' + str(trump))
    print('Exon Length: ' + str(len(trump)) + 'bp')

else:
    penis = mantooth[:penetration[0]]
    print('Exon 1: ' + str(penis))
    print('Exon Length: ' + str(len(penis)) + 'bp')
    print('\n')
    
    for heroin_users in range(0,va-1):
        shit = mantooth[printers[stupid]:penetration[fucking]]
        print('Exon ' + str(pirate_hooker) + ': ' + str(shit))
        print('Exon Length: ' + str(len(shit)) + 'bp')
        print('\n')
        fucking += 1
        stupid += 1
        pirate_hooker += 1
        
    fuck = mantooth[printers[-1]:]
    print('Exon ' + str(pirate_hooker + 1) + ': ' + str(fuck))
    print('Exon Length: ' + str(len(fuck)) + 'bp')    
