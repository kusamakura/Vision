# Vision Alt PCB

A PCB for the [Vision keyboard by SatT Keyboards](https://github.com/satt99/Vision) with alternative layout options.

## Notable changes

- R2 2U Backspace
- Left bottom row: from 2U-1U to 1U-2U, add 3U
- Right bottom row: remove 1U-1.75U, add 2.75U
- Nudge P position 0.125 mm to the left

## Layout

![Layout](./layout.png)

## How to use

Use the gerbers, BOM, and CPL files in the [JLCPCB production files folder](./JLCPCB/production_files/). **Set the PCB thickness to 1.2 mm when ordering**; otherwise your PCB will not work with the case.

Prototypes pending to check if this works.

The source files were originally in KiCAD 5, converted to KiCAD 6, then modified.
JLC production output was generated with the [JLC Fabrication Toolkit plugin](https://github.com/bennymeg/JLC-Plugin-for-KiCad).

## Disclaimer

Maintainers and contributors are not liable if you end up with a non-functional PCB. Order at your own risk. Support will not be provided but pull requests will be reviewed and possibly accepted.

## Todo

- [x] Finalize layout changes
- [x] Order prototypes
- [ ] Confirm prototypes
- [ ] Order plates
- [ ] Write firmware

