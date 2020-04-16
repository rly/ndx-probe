# -*- coding: utf-8 -*-

import os.path

from pynwb.spec import NWBNamespaceBuilder, export_spec, NWBGroupSpec, NWBAttributeSpec, NWBDatasetSpec, NWBDtypeSpec


def main():
    # these arguments were auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(
        doc='An extension to hold metadata about a multi-electrode probe.',
        name='ndx-probe',
        version='0.1.0',
        author=list(map(str.strip, 'Ryan Ly'.split(','))),
        contact=list(map(str.strip, 'rly@lbl.gov'.split(',')))
    )

    ns_builder.include_type('ElectrodeGroup', namespace='core')

    stereotrode = NWBGroupSpec(
        neurodata_type_def='Stereotrode',
        neurodata_type_inc='ElectrodeGroup',
        doc=('A subtype of ElectrodeGroup to include metadata about a single stereotrode (group of 2 closely spaced '
             'electrodes) on a shank of a probe.'),
        attributes=[
            NWBAttributeSpec(
                name='location',
                doc=('Location of the stereotrode in the brain (optional). Specify the area, layer, comments on '
                     'estimation of area/layer, etc. Use standard atlas names for anatomical regions when '
                     'possible.'),
                dtype='text',
                required=False
            )
        ]
    )

    tetrode = NWBGroupSpec(
        neurodata_type_def='Tetrode',
        neurodata_type_inc='ElectrodeGroup',
        doc=('A subtype of ElectrodeGroup to include metadata about a single tetrode (group of 4 closely spaced '
             'electrodes) on a shank of a probe.'),
        attributes=[
            NWBAttributeSpec(
                name='location',
                doc=('Location of the tetrode in the brain (optional). Specify the area, layer, comments on '
                     'estimation of area/layer, etc. Use standard atlas names for anatomical regions when '
                     'possible.'),
                dtype='text',
                required=False
            )
        ]
    )

    shank = NWBGroupSpec(
        neurodata_type_def='Shank',
        neurodata_type_inc='ElectrodeGroup',
        doc=('A subtype of ElectrodeGroup to include metadata about a single shank of a probe.')
    )

    entry_point_ap_dtype = NWBDtypeSpec(name='ap',
                                        dtype='float',
                                        doc='Anterior-Posterior coordinate, in mm.')
    entry_point_lr_dtype = NWBDtypeSpec(name='lr',
                                        dtype='float',
                                        doc='Left-Right coordinate, in mm.')
    entry_point_dv_dtype = NWBDtypeSpec(name='dv',
                                        dtype='float',
                                        doc='Dorsal-Ventral coordinate, in mm.')

    entry_point = NWBDatasetSpec(
        name='entry_point',
        doc='The coordinates of the entry point.',
        dtype=[entry_point_ap_dtype, entry_point_lr_dtype, entry_point_dv_dtype],  # compound dtype
        attributes=[
            NWBAttributeSpec(
                name='reference',
                doc=('Description of the reference atlas used for the coordinates, e.g., Allen Institute Common '
                     'Coordinate Framework v3, or stereotaxic coordinates with zero point at ear-bar zero.'),
                dtype='text'
            ),
            NWBAttributeSpec(
                name='unit',
                doc='Unit of measurement for the coordinates.',
                dtype='text',
                value='millimeters'
            )
        ],
        quantity='?'
    )

    angle_coronal_dtype = NWBDtypeSpec(
       name='coronal',
       dtype='float',
       doc='Coronal angle, in degrees'
    )
    angle_sagittal_dtype = NWBDtypeSpec(
        name='sagittal',
        dtype='float',
        doc='Sagittal angle, in degrees'
    )
    angle_axial_dtype = NWBDtypeSpec(
        name='axial',
        dtype='float',
        doc='Axial angle, in degrees'
    )

    angle = NWBDatasetSpec(
        name='angle',
        doc='The angle of the probe.',
        dtype=[angle_coronal_dtype, angle_sagittal_dtype, angle_axial_dtype],  # compound dtype
        attributes=[
            NWBAttributeSpec(
                name='reference',
                doc='Description of the reference frame used for the angles, e.g., which direction is angle zero.',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='unit',
                doc='Unit of measurement for the angles.',
                dtype='text',
                value='degrees'
            )
        ],
        quantity='?'
    )

    distance_advanced = NWBDatasetSpec(
        name='distance_advanced',
        doc='The distance that the probe was advanced from the surface of the brain, in mm.',
        dtype='float',
        attributes=[
            NWBAttributeSpec(
                name='unit',
                doc='Unit of measurement for the distance.',
                dtype='text',
                value='millimeters'
            )
        ],
        quantity='?'
    )

    probe = NWBGroupSpec(
        neurodata_type_def='Probe',
        neurodata_type_inc='Device',
        doc=('Metadata about a multi-electrode probe (or array), which contains one or many shanks. '
             'Each shank should be represented as an ElectrodeGroup. Sub-groupings within a shank '
             'should also be represented as ElectrodeGroups.'),
        attributes=[
            NWBAttributeSpec(
                name='description',
                doc='Description of the probe as free-form text.',
                dtype='text',
            ),
            NWBAttributeSpec(
                name='model',
                doc='Model name of the probe.',
                dtype='text',
            ),
            NWBAttributeSpec(
                name='manufacturer',
                doc='Manufacturer name of the probe.',
                dtype='text',
            ),
            NWBAttributeSpec(
                name='id',
                doc='Serial number or other unique identifier of the probe.',
                dtype='text',
                required=False
            ),
        ],
        datasets=[
            entry_point,
            angle,
            distance_advanced,
        ]
    )

    new_data_types = [stereotrode, tetrode, shank, probe]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    # usage: python create_extension_spec.py
    main()
