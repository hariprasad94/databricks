import pipdeptree
import json

pkgs = pipdeptree.get_installed_distributions()
dist_index = pipdeptree.build_dist_index(pkgs)
tree = pipdeptree.construct_tree(dist_index)
json_tree = json.loads(pipdeptree.render_json_tree(tree, indent=0))
print(json_tree)
print([package for package in json_tree if package['package_name'] == 'tornado'][0])