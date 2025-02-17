import pathlib
from typing import Tuple
import inspect
from ubcpdk import cells

filepath = pathlib.Path(__file__).parent.absolute() / "components.rst"

skip = {
    "LIBRARY",
    "circuit_names",
    "component_factory",
    "component_names",
    "container_names",
    "component_names_test_ports",
    "component_names_skip_test",
    "component_names_skip_test_ports",
    "dataclasses",
    "library",
    "waveguide_template",
}

skip_plot: Tuple[str, ...] = ("add_fiber_array_siepic",)
skip_settings: Tuple[str, ...] = ("flatten", "safe_cell_names")


with open(filepath, "w+") as f:
    f.write(
        """

Here are the components available in the PDK


Components
=============================
"""
    )

    for name in sorted(cells.keys()):
        if name in skip or name.startswith("_"):
            continue
        print(name)
        sig = inspect.signature(cells[name])
        kwargs = ", ".join(
            [
                f"{p}={repr(sig.parameters[p].default)}"
                for p in sig.parameters
                if isinstance(sig.parameters[p].default, (int, float, str, tuple))
                and p not in skip_settings
            ]
        )
        if name in skip_plot:
            f.write(
                f"""

{name}
----------------------------------------------------

.. autofunction:: ubcpdk.components.{name}

"""
            )
        else:
            f.write(
                f"""

{name}
----------------------------------------------------

.. autofunction:: ubcpdk.components.{name}

.. plot::
  :include-source:

  import ubcpdk

  c = ubcpdk.PDK.get_component("{name}", {kwargs})
  c.plot()

"""
            )
