import os
import pandas as pd
from datetime import datetime
from catalogue.models import Flare
from django.conf import settings

FNAME = 'targets/tags_srh_06_2025.csv'
FPATH = os.path.join(settings.MEDIA_ROOT, FNAME)


def get_datetime_filter(fname):
    """ Extracts a datetime object from a CSV data for use in DB filter """
    date_str = fname[10:-5]
    date_obj = datetime.strptime(date_str, '%Y%m%dT%H_%M_%S')

    return date_obj


def update_tag():
    """ Updates the tag obtained by CNN model in the table Flare """
    df = pd.read_csv(FPATH)
    
    for idx, row in df.iterrows():
        date_obj = get_datetime_filter(row['filename'])
        print(date_obj)
        Flare.objects.filter(date=date_obj.date(), start_event=date_obj).update(tag=row['tag'])
    
update_tag()
print('Tag update finished.')
