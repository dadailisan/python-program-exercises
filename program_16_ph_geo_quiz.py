#Philippines Cities - Capital

import random

kabisera = {'Ilocos Norte':'Laoag City', 'Ilocos Sur':'Vigan City',
            'La Union':'San Fernando City', 'Pangasinan':'Lingayen',
            'Aurora':'Baler', 'Bataan':'Balanga City', 'Bulacan':'Malolos',
            'Pampanga':'San Fernando City', 'Nueva Ecija':'Palayan City',
            'Tarlac':'Tarlac City', 'Zambales':'Iba', 'Batangas':'Batangas City',
            'Cavite':'Trece Martirez City', 'Laguna':'Santa Cruz',
            'Quezon':'Lucena City', 'Rizal':'Antipolo City',
            'Marinduque':'Boac', 'Occidental Mindoro':'Mamburao',
            'Oriental Mindoro':'Calapan City', 'Palawan':'Puerto Princesa City',
            'Romblon':'Romblon', 'Albay':'Legazpi City', 'Camarines Norte':'Daet',
            'Camarines Sur':'Pili', 'Catanduanes':'Virac', 'Masbate':'Masbate City',
            'Sorsogon':'Sorsogon City', 'Aklan':'Kalibo', 'Antique':'San Jose',
            'Capiz':'Roxas City', 'Guimaras':'Jordan', 'Iloilo':'Iloilo City',
            'Negros Occidental':'Bacolod City', 'Bohol':'Tagbilaran City',
            'Cebu':'Cebu City', 'Negros Oriental':'Dumaguete City',
            'Siquijor':'Siquijor', 'Biliran':'Naval', 'Eastern Samar':'Borongan City',
            'Leyte':'Tacloban City', 'Northern Samar':'Catarman',
            'Southern Leyte':'Maasin City', 'Western Samar':'Catbalogan City',
            'Zamboanga Del Norte':'Dipolog City', 'Zamboanga Del Sur':'Pagadian City',
            'Zamboanga Sibugay':'Ipil', 'Bukidnon':'Malaybalay City',
            'Camiguin':'Mambajao', 'Lanao Del Norte':'Tubod',
            'Misamis Occidental':'Oroquieta City', 'Misamis Oriental':'Cagayan de Oro City',
            'Compostela Valley':'Nabunturan', 'Davao Del Norte':'Tagum City',
            'Davao Del Sur':'Digos City', 'Davao Oriental': 'City of Mati',
            'North Cotabato':'Kidapawan City', 'Sarangani':'Koronadal City',
            'Sultan Kudarat':'Isulan', 'Agusan Del Norte':'Cabadbaran City',
            'Agusan Del Sur':'Prosperidad', 'Dinagat Islands':'San Jose',
            'Surigao Del Norte':'Surigao City', 'Surigao Del Sur':'Tandag City',
            'Basilan':'Basilan', 'Lanao Del Sur':'Marawi City',
            'Maguindanao':'Shariff Aguak(Maganoy)', 'Shariff Kabunsuan':'Datu Odin Sinsuat',
            'Sulu':'Jolo', 'Tawi-Tawi':'Panglima Sugala(Balimbing)',
            'Abra':'Bangued', 'Apayao':'Kabugao', 'Benguet':'La Trinidad',
            'Ifugao':'Lagawe', 'Kalinga':'Tabuk', 'Mt. Province':'Bontoc'}

lugar = list(kabisera.keys())
random.shuffle(lugar)
tama = 0
for tanong_bilang in range(len(kabisera)):
    tamang_sagot = kabisera[lugar[tanong_bilang]]
    maling_sagot = list(kabisera.values())
    del maling_sagot[maling_sagot.index(tamang_sagot)]
    maling_sagot = random.sample(maling_sagot, 3)
    pagpipilian = maling_sagot + [tamang_sagot]
    random.shuffle(pagpipilian)
    print('%s. Ano ang kabisera ng %s?\n' %(tanong_bilang + 1, lugar[tanong_bilang]))
    for i in range(4):
        print('%s. %s\n' %('ABCD'[i], pagpipilian[i]))
        print('')

    print('Pumili ng tamang sagot:(wag maglagay ng sagot kung ayawan na!)')
    sagot = input()
    if sagot == 'ABCD'[pagpipilian.index(tamang_sagot)]:
        print('\nMAY TAMA KA!!!\n\n')
        tama = tama + 1
    if sagot == '':
        print('\nMARAMING SALAMAT!\n\n')
        print('ikaw ay nakakuha ng ' + str(tama) + ' tamang sagot sa ' + str(tanong_bilang) + ' tanong.')
        break
    if sagot != 'ABCD'[pagpipilian.index(tamang_sagot)]:
        print('\nMALI KA!!!\n\n')
