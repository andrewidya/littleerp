import pyexcel as pe
import tablib
from import_export import resources

from django.db.models import get_app


app_list = []


class Importer(object):
    dataset = tablib.Dataset()
    model = None
    file_name = None
    excel_file = None

    def __init__(self, model=None, file_name=None):
        self.model = model
        self.file_name = file_name
        self._file_open()
        self._populate_dataset_header_from_obj()
        self._data_parsing()

    def _file_open(self):
        self.excel_file = pe.get_records(file_name=self.file_name)

    def _populate_dataset_header_from_obj(self):
        self.dataset.headers = [field.name for field in self.model._meta.fields]

    def _data_parsing(self):
        for record in self.excel_file:
            data = []
            for index in self.dataset.headers:
                data.append(record[index])
            self.dataset.append(data)

    def import_data(self):
        model_resource = resources.modelresource_factory(model=self.model)()
        result = model_resource.import_data(self.dataset, dry_run=True)
        if not result.has_errors():
            result = model_resource.import_data(self.dataset, dry_run=False)


def site_register(*args):
    for app in args:
        app_list.append(get_app(app))


def Terbilang(x):
    satuan = [
        '',
        'Satu',
        'Dua',
        'Tiga',
        'Empat',
        'Lima',
        'Enam',
        'Tujuh',
        'Delapan',
        'Sembilan',
        'Sepuluh',
        'Sebelas'
    ]
    n = int(x)
    if n == 0:
        Hasil = ''
    elif n >= 0 and n <= 11:
        Hasil = ' ' + satuan[n]
    elif n >= 12 and n <= 19:
        Hasil = Terbilang(n % 10) + ' Belas'
    elif n >= 20 and n <= 99:
        Hasil = Terbilang(n / 10) + ' Puluh' + Terbilang(n % 10)
    elif n >= 100 and n <= 199:
        Hasil = ' Seratus' + Terbilang(n - 100)
    elif n >= 200 and n <= 999:
        Hasil = Terbilang(n / 100) + ' Ratus' + Terbilang(n % 100)
    elif n >= 1000 and n <= 1999:
        Hasil = ' Seribu' + Terbilang(n - 1000)
    elif n >= 2000 and n <= 999999:
        Hasil = Terbilang(n / 1000) + ' Ribu' + Terbilang(n % 1000)
    elif n >= 1000000 and n <= 999999999:
        Hasil = Terbilang(n / 1000000) + ' Juta' + Terbilang(n % 1000000)
    else:
        Hasil = Terbilang(n / 1000000000) + ' Milyar' + Terbilang(n % 100000000)
    return Hasil
