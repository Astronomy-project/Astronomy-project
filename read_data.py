import pandas as pd

#!Lee el csv
def data(file='variable_stars_database-small.csv'):
    data = pd.read_csv(file, delimiter=",")
    return data

#!Crea un dict donde key es el id de la estrella y value un dict con su información donde cada llave es una variable
def filtered_data(data):
    size = (data.shape)[0]
    stars = {}
    for i in range(0,size):
        info = {}
        id = data.iloc[i]['id']
        for variable in data.columns:
            if variable != 'id' and variable != 'ruwe;;;;;':
                info[variable] = data.iloc[i][variable]
            elif variable == 'ruwe;;;;;':
                ruwe = data.iloc[i][variable]
                if len(ruwe) > 5:
                    info['ruwe'] = float((str(data.iloc[i][variable]))[:-5])
                else:
                    info['ruwe'] = 'nan'
            elif variable != 'id':
                info[variable] = data.iloc[i][variable]
        stars[id] = info
    return stars

#!Retorna un dict de listas con los id de las estrellas previamente clasificadas en la base de datos
def previous_classified(data):
    rotational, delta_scuti, cepheid, mira, eclipsing_binary, irregular, semi_irregular, uncertain, lyrae, coronae_borealis, cataclysmic, flare, other_rotational, pulsating_white_dwarf, other = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
    for i in data.keys():
        type = data[i]['variable_type']
        id = data[i]['id']
        if type == 'ROT':
            rotational.append(id)
        elif type in ['DSCT', 'HADS']:
            delta_scuti.append(id)
        elif type in ['CWA','CWB','DCEP','DCEPS','RVA']:
            cepheid.append(id)
        elif type == 'M':
            mira.append(id)
        elif type in ['EA', 'EB', 'EW', 'ELL']:
            eclipsing_binary.append(id)
        elif type in ['YSO', 'L', 'GCAS']:
            irregular.append(id)
        elif type in ['SR', 'SRD', 'LSP']:
            semi_irregular.append(id)
        elif type in ['GCAS:', 'ROT:', 'SR:', 'VAR:', 'RRAB:', 'DSCT:', 'M:']:
            uncertain.append(id)
        elif type in ['RRAB', 'RRC', 'RRD']:
            lyrae.append(id)
        elif type in ['RCB', 'RCB:', 'DYPer']:
            coronae_borealis.append(id)
        elif type in ['CV', 'CV+E', 'CV:', 'UG', 'UGER', 'UGSS', 'UGSU', 'UGSU+E', 'UGSU:', 'UGWZ', 'UGZ', 'AM', 'AM+E', 'AM:', 'DQ', 'DQ:']:
            cataclysmic.append(id)
        elif type in ['UV', 'UV:']:
            flare.append(id)
        elif type in ['SXARI', 'SXARI:', 'HB', 'R']:
            other_rotational.append(id)
        elif type in ['ZZ', 'ZZ:', 'ZZA', 'ZZB', 'ZZLep', 'ZZO']:
            pulsating_white_dwarf.append(id)
        else:
            other.append(id)
    classified = {'rotational':rotational,
                  'delta_scuti':delta_scuti,
                  'cepheid':cepheid,
                  'mira':mira,
                  'eclipsing_binary':eclipsing_binary,
                  'irregular':irregular,
                  'semi_irregular':semi_irregular,
                  'uncertain':uncertain,
                  'lyrae':lyrae,
                  'coronae_borealis':coronae_borealis,
                  'cataclysmic':cataclysmic,
                  'flare':flare,
                  'other_rotational':other_rotational,
                  'pulsating_white_dwarf':pulsating_white_dwarf,
                  'other':other
                  }
    return classified

#!Función que retorna la información de una estrella dado un id
def search_by_id(id,data):
    star = None
    for id in data.keys():
        if data[id]['id'] == str(id):
            star = data[id]
    return star