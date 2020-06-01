import pp
from pp.add_pins import add_pins
from ubc.layers import LAYER


@pp.autoname
def bend90(radius=10, width=0.5):
    c = pp.c.bend_circular(
        radius=radius,
        width=width,
        layer=LAYER.WG,
        layers_cladding=[LAYER.DEVREC],
        cladding_offset=1,
    )
    labels = [
        f"Lumerical_INTERCONNECT_library=Design kits/EBeam",
        f"Lumerical_INTERCONNECT_component=ebeam_bend_1550",
        f"Spice_param:radius={radius:.3f}u wg_width={width:.3f}u",
    ]

    for i, text in enumerate(labels):
        c.add(pp.c.label(text=text, position=(c.x, c.y + i * 0.1), layer=LAYER.DEVREC))
    add_pins(c, layer=LAYER.PORT)
    return c


if __name__ == "__main__":
    c = bend90()
    pp.show(c)
