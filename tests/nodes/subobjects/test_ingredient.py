import json

from util import strip_uid_from_dict

import cript


def test_json(complex_ingredient_node, complex_ingredient_dict):
    i = complex_ingredient_node
    i_dict = json.loads(i.json)
    assert strip_uid_from_dict(i_dict) == strip_uid_from_dict(complex_ingredient_dict)
    i2 = cript.load_nodes_from_json(i.json)
    assert strip_uid_from_dict(json.loads(i.json)) == strip_uid_from_dict(json.loads(i2.json))


def test_getter_setter(complex_ingredient_node, complex_quantity_node, simple_material_node):
    i2 = complex_ingredient_node
    q2 = complex_quantity_node
    i2.set_material(simple_material_node, [complex_quantity_node])
    assert i2.material is simple_material_node
    assert i2.quantities[-1] is q2

    i2.keyword = "monomer"
    assert i2.keyword == "monomer"