import os
import pandas as pd
from datetime import datetime
from catalogue.models import Flare
from django.conf import settings


class ImportFlareCatalogue():
    """ This class import recognized flares to database """

    def __init__(self, fpath):
        self.fpath = fpath
        self.fname = os.path.basename(fpath)
        self.date = self.get_date()


    def get_date(self):
        """ Return datetime.date obtained from csv file name """
        date_str = self.fname.split('_')[1].split('.')[0]
        date_obj = datetime.strptime(date_str, '%Y%m%d')

        return date_obj
    

    def convert_time(self, time):
        """ Convert time string to datetime object """
        tm_obj = datetime.strptime(time, '%H:%M:%S')
        dt_obj = datetime.combine(self.date.date(), tm_obj.time())

        return dt_obj


    def add_flare_to_db(self):
        """ Create flare record in Flare model and save to the DB """
        df = pd.read_csv(self.fpath, delimiter='\t')

        for index, row in df.iterrows():
            flare = Flare(
                date = self.date.date(),
                start_event = self.convert_time(row['start event']),
                maximum_event = self.convert_time(row['maximum event']),
                end_event  = self.convert_time(row ['finish event']),
                min_freq = row['min freq GHz'],
                max_freq = row['max freq GHz']
            )
            flare.save()
        
FDIR = 'csv/events_062025'
dir_local = os.path.join(settings.MEDIA_ROOT, FDIR)

flist = os.listdir(dir_local)
    
for ff in flist:
    fpath = os.path.join(dir_local, ff)
    import_obj = ImportFlareCatalogue(fpath)
    import_obj.add_flare_to_db()  
    print(fpath)
                    
print('Import finished!')
