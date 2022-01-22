# UBC PDK 0.0.6

UBC SiEPIC Ebeam PDK from [edx course](https://www.edx.org/course/silicon-photonics-design-fabrication-and-data-ana)

## Installation for users

You can install directly from pip `pip install ubc`

pip also lets you install a specific version `pip install ubc==0.0.7`

and update to the latest version with `pip install ubc --upgrade`

## Installation for developers

Run `make install` in a terminal. If you are on Windows, open an anaconda prompt terminal and type:

```
git clone https://github.com/gdsfactory/ubc.git
cd ubc
pip install -r requirements.txt --upgrade
pip install -r requirements_dev.txt --upgrade
pip install pre-commit
pre-commit install
python install_tech.py
```

## Acks

UBC pdk top contributors:

- Lukas Chrostowski (UBC professor): creator of the course and maintainer of the PDK cells
- Joaquin Matres (Google): maintainer of gdsfactory
- Alex Tait (Queens University): maintainer of lygadgets

Open source heroes:

- Matthias Köfferlein (Germany): for Klayout
- Lucas Heitzmann (University of Campinas, Brazil): for gdspy
- Adam McCaughan (NIST): for phidl
- Alex Tait (Queens University): for lytest
- Thomas Ferreira de Lima (NEC): for `pip install klayout`


Links:

- [UBC docs](https://gdsfactory.github.io/ubc/) and [repo](https://github.com/gdsfactory/ubc)
- [edx course](https://www.edx.org/course/silicon-photonics-design-fabrication-and-data-ana)
- [siepic Ebeam PDK](https://github.com/lukasc-ubc/SiEPIC_EBeam_PDK)
- [gdsfactory](https://gdsfactory.github.io/gdsfactory/)
- [awesome photonics list](https://github.com/joamatab/awesome_photonics)
