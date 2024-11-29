import os
import pandas as pd
from datetime import datetime
from catalogue.models import FlareList, Flare, TestFlare 
from django.conf import settings

FDIR = 'csv/events_122023/'
FDIR_IMG = 'img/png_events_122023/'


def import_catalogue():
    fdir_local = os.path.join(settings.MEDIA_ROOT, FDIR)
    fdir_img_local = os.path.join(settings.MEDIA_ROOT, FDIR_IMG)
    
    flist = os.listdir(fdir_local)
    flist.sort()

    flist_img = os.listdir(fdir_img_local)
    flist_img.sort()

    for ff, ff_img in zip(flist, flist_img):
        df = pd.read_csv(fdir_local+ff, delimiter='\t')
        
        dt_str = ff.split('_')[1].split('.')[0]
        dt = datetime.strptime(dt_str, '%Y%m%d')

        flare_list = FlareList(
            date = dt,
            num_flare = len(df),
            diagram = os.path.join(FDIR_IMG, ff_img),
            csv_file = os.path.join(FDIR, ff),
        )
        flare_list.save()
        read_csv(flare_list, fdir_local+ff)


def read_csv(dt, fpath_csv):
    df = pd.read_csv(fpath_csv, delimiter='\t')

    for index, row in df.iterrows():
        flare = Flare(
            date = dt,
            start_event = row['start event'],
            maximum_event = row['maximum event'],
            finish_event = row ['finish event'],
            min_freq = row['min freq GHz'],
            max_freq = row['max freq GHz']
        )

        flare.save()

import_catalogue()
print('CSV data has been loaded into the Django database.')
