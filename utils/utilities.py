import tablib
import pyexcel as pe
from import_export import resources

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

	def _file_open(self):
		self.excel_file = pe.get_records(file_name=self.file_name)

	def _populate_dataset_header_from_obj(self):
		self.dataset.headers = [field.name for field in self.model._meta.fields]

	def data_parsing(self):
		for record in self.excel_file:
			data = []
			for index in self.dataset.headers:
				data.append(record[index])
			self.dataset.append(data)

	def import_data(self):
		self.data_parsing()
		model_resource = resources.modelresource_factory(model=self.model)()
		result = model_resource.import_data(self.dataset, dry_run=True)
		if not result.has_errors():
			result = model_resource.import_data(self.dataset, dry_run=False)