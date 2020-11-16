# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashGrid(Component):
    """A DashGrid component.
GridComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks.
- label (string; required): A label that will be printed when this component is rendered.
- value (string; optional): The value displayed in the input."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, label=Component.REQUIRED, value=Component.UNDEFINED, className=Component.UNDEFINED, items=Component.UNDEFINED, cols=Component.UNDEFINED, rowHeight=Component.UNDEFINED, onLayoutChange=Component.UNDEFINED, verticalCompact=Component.UNDEFINED, preventCollision=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'label', 'value']
        self._type = 'DashGrid'
        self._namespace = 'dash_grid'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'label', 'value']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['label']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DashGrid, self).__init__(**args)
