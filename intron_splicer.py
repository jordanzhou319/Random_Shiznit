#Splice based on intron locations

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
hookers = []
porn = []

for blue_waffle in range(0,va):
    blue = int(input('Beginning of intron ' + str(na) + ': '))
    penetration.append(blue-1)
    waffle = int(input('End of intron ' + str(na) + ': '))
    printers.append(waffle)
    na += 1

print('\n')

if va == 1:
    trump = mantooth[:penetration[0]] + mantooth[printers[0]:]
    hookers.append(len(trump))
    print('Exon: ' + str(trump))
    print('Exon Length: ' + str(len(trump)) + 'bp')
    print('\n')
    
    herpes = sum(hookers)
    chlamydia = (herpes/len(gi))
    print('Total coding length: ' + str(herpes) + 'bp')
    print('Percent coding: ' + str('{:.2%}'.format(chlamydia)))

else:
    penis = mantooth[:penetration[0]]
    hookers.append(len(penis))
    porn.append(penis)
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
        hookers.append(len(shit))
        porn.append(shit)
        
    fuck = mantooth[printers[-1]:]
    hookers.append(len(fuck))
    porn.append(fuck)
    print('Exon ' + str(pirate_hooker + 1) + ': ' + str(fuck))
    print('Exon Length: ' + str(len(fuck)) + 'bp')  
    print('\n')
    
    herpes = sum(hookers)
    chlamydia = (herpes/len(gi)) 
    print('Complete coding region:')
    print(*porn,sep='')
    print('Total coding length: ' + str(herpes) + 'bp')
    print('Percent coding: ' + str('{:.2%}'.format(chlamydia)))

#splice based on exon locations

va = int(input('Number of exons: '))
gi = input('DNA Sequence: ')

na = 1
stupid = 0
pirate_hooker = 1

whore_island = gi.replace(' ','')
mantooth = ''.join(i for i in whore_island if not i.isdigit())

penetration = []
printers = []
hookers = []
porn = []
anal = []

for blue_waffle in range(0,va):
    blue = int(input('Beginning of exon ' + str(na) + ': '))
    penetration.append(blue-1)
    waffle = int(input('End of exon ' + str(na) + ': '))
    printers.append(waffle-1)
    na += 1

print('\n')

if va == 1:
    fucker = mantooth[:penetration[0]]
    porn.append(fucker.lower())
    
    trump = mantooth[penetration[0] : printers[0]]
    porn.append(trump)
    hookers.append(len(trump))
    print('Exon: ' + str(trump))
    print('Exon Length: ' + str(len(trump)) + 'bp')
    print('\n')
    
    twat = mantooth[printers[-1]:]
    porn.append(twat.lower())
    
    print('Sequence including introns(lowercase):')
    print(*porn,sep='')
    herpes = sum(hookers)
    chlamydia = (herpes/len(gi))
    print('Total coding length: ' + str(herpes) + 'bp')
    print('Percent coding: ' + str('{:.2%}'.format(chlamydia)))

else:
    fucker = mantooth[:penetration[0]]
    porn.append(fucker.lower())
    
    for heroin_users in range(0,va):
        heroin = mantooth[penetration[stupid]:printers[stupid]]
        penetration.append(None)
        users = mantooth[printers[stupid]:penetration[stupid+1]]
        print('Exon ' + str(pirate_hooker) + ': ' + str(heroin))
        print('Exon Length: ' + str(len(heroin)) + 'bp')
        print('\n')
        stupid += 1
        pirate_hooker += 1
        hookers.append(len(heroin))
        porn.append(heroin)
        porn.append(users.lower())
        anal.append(heroin)

    herpes = sum(hookers)
    chlamydia = (herpes/len(gi)) 
    print('Complete coding region:')
    print(*anal,sep='')
    print('Sequence including introns(lowercase):')
    print(*porn,sep='')
    print('Total coding length: ' + str(herpes) + 'bp')
    print('Percent coding: ' + str('{:.2%}'.format(chlamydia)))
