import jsonschema
from jsonschema.validators import Draft7Validator
import simplejson as json
import os

if __name__ == '__main__':
    with open("schemas/definition.schema.json", 'r') as f:
        data = f.read()
        definition = json.loads(data)

    with open("schemas/trained_model.schema.json", 'r') as f:
        data = f.read()
        trained_model = json.loads(data)

    with open("schemas/input.schema.json", 'r') as f:
        data = f.read()
        input = json.loads(data)

    with open("schemas/preprocessing.schema.json", 'r') as f:
        data = f.read()
        preprocessing = json.loads(data)

    store = {
        "https://raw.githubusercontent.com/elastic/ml_json_schemas/master/schemas/definition.schema.json": definition,
        "https://raw.githubusercontent.com/elastic/ml_json_schemas/master/schemas/trained_model.schema.json": trained_model,
        "https://raw.githubusercontent.com/elastic/ml_json_schemas/master/schemas/input.schema.json": input,
        "https://raw.githubusercontent.com/elastic/ml_json_schemas/master/schemas/preprocessing.schema.json": preprocessing

    }

    full_path = os.path.join(os.path.dirname(__file__), "schemas")
    resolver = jsonschema.RefResolver(base_uri='file:' + full_path, referrer=None, store=store)
    validator = Draft7Validator(schema=definition, resolver=resolver)
    validator.check_schema(definition)
    validator.check_schema(input)
    validator.check_schema(preprocessing)
    validator.check_schema(trained_model)

    with open("example.json", "r") as f:
        example_data = f.read()
    example = json.loads(example_data)

    validator.validate(example, definition)
