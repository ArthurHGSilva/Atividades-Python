mamifero = str(input('É mamífero? '))


if mamifero == 'sim':
    quadru = str(input('É quadrúpede? '))
    if quadru == 'sim':
        car = str(input('É carnívoro? '))
        if car == 'sim':
            print('Leão')
        else:
            herb = str(input('É herbívoro? '))
            if herb == 'sim':
                print('Cavalo')
    else:
        bipe = str(input('É bípede? '))
        if bipe == 'sim':
            oni = str(input('É onívoro? '))
            if oni == 'sim':
                print('Homem')
            else:
                fru = str(input('É frutívoro? '))
                if fru == 'sim':
                    print('Macaco')
        else:
            voa = str(input('É voador? '))
            if voa == 'sim':
                print('Morcego')
            else:
                aqua = str(input('É aquático? '))
                if aqua == 'sim':
                    print('Baleia')

else:
    aves = str(input('É uma ave? '))
    if aves == 'sim':
        n_voador = str(input('Não voa? '))
        if n_voador == 'sim':
            trop = str(input('É uma ave tropical? '))
            if trop == 'sim':
                print('Avestruz')
            else:
                polar = str(input('É uma ave polar? '))
                if polar == 'sim':
                    print('Pinguim')
        nada = str(input('É uma ave nadadora? '))
        if nada == 'sim':
            print('Pato')
        else:
            rapi = str(input('É uma ave de rapina? '))
            if rapi == 'sim':
                print('Águia')
    else:
        reptil = str(input('É réptil? '))
        if reptil == 'sim':
            c_casco = str(input('Possui casco? '))
            if c_casco == 'sim':
                print('Tartaruga')
            else:
                carn = str(input('É carnívoro? '))
                if carn == 'sim':
                    print('Crocodilo')
                else:
                    s_patas = str(input('Não possui patas? '))
                    if s_patas == 'sim':
                        print('Cobra')
