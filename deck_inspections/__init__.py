__version__ = "0.0.1"


def _patch_app_route():
	"""Force Deck Inspections app tile to open the Deck Inspection list view."""
	import frappe.apps as apps_module

	_original_get_route = apps_module.get_route

	def _get_route(app, allowed_workspaces=None):
		if app and app.get("name") == "deck_inspections":
			# Route directly to Deck Inspection DocType list
			return "/app/deck-inspection"
		return _original_get_route(app, allowed_workspaces)

	apps_module.get_route = _get_route


_patch_app_route()
