# from open_alchemy import init_json

# init_json('openapi.json',models_filename='models.py')

from pathlib import Path
from tempfile import TemporaryDirectory
from datamodel_code_generator import InputFileType, generate

with open('./api/model/openapi.json','r', encoding='utf-8') as f:
    json_schema = f.read()

with TemporaryDirectory() as temporary_directory_name:
    temporary_directory = Path(temporary_directory_name)
    output = Path(temporary_directory / 'model.py')
    generate(
        json_schema,
        input_file_type=InputFileType.JsonSchema,
        input_filename="example.json",
        output=output,
    )
    model: str = output.read_text()
print(model)

# from pyswagger import App

# # file URI
# app = App.create('api\model\openapi.json')

