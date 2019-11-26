# -*- coding: utf-8 -*-

import os.path

from pynwb.spec import NWBNamespaceBuilder, export_spec, NWBGroupSpec, NWBAttributeSpec, NWBDatasetSpec, NWBDtypeSpec
from pynwb.spec import NWBLinkSpec


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
    ns_builder.include_type('DynamicTableRegion', namespace='hdmf.common')

    tetrode = NWBGroupSpec(
        neurodata_type_def='Tetrode',
        neurodata_type_inc='ElectrodeGroup',
        doc=('A subtype of ElectrodeGroup to include metadata about a single tetrode (group of 4 closely spaced '
             'electrodes) on a shank of a probe.'),
        attributes=[
            NWBAttributeSpec(
                name='location',
                doc=('Location of the tetrode in the brain.'),
                dtype='text',
                required=False
            )
        ],
        datasets=[
            NWBDatasetSpec(
                name='electrodes',
                neurodata_type_inc='DynamicTableRegion',
                doc='Pointer to the rows of the electrodes table corresponding to the electrodes of this tetrode.',
            )
        ]
    )

    shank = NWBGroupSpec(
        neurodata_type_def='Shank',
        neurodata_type_inc='ElectrodeGroup',
        doc=('A subtype of ElectrodeGroup to include metadata about a single shank of a probe.'),
        datasets=[
            NWBDatasetSpec(
                name='electrodes',
                neurodata_type_inc='DynamicTableRegion',
                doc='Pointer to the rows of the electrodes table corresponding to the electrodes of this shank.',
            )
        ],
        links=[
            NWBLinkSpec(target_type='Tetrode',
                        doc='The individual tetrode groups that are part of this shank.',
                        quantity='*')
        ]
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
        dtype=[entry_point_ap_dtype, entry_point_lr_dtype, entry_point_dv_dtype],
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
        dtype=[angle_coronal_dtype, angle_sagittal_dtype, angle_axial_dtype],
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
                dtype='float',
                value='millimeters'
            )
        ],
        quantity='?'
    )

    probe = NWBGroupSpec(
        neurodata_type_def='Probe',
        neurodata_type_inc='ElectrodeGroup',
        doc=('A subtype of ElectrodeGroup to include metadata about a multi-electrode probe.'),
        attributes=[
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
        ],
        datasets=[
            entry_point,
            angle,
            distance_advanced,
            NWBDatasetSpec(
                name='electrodes',
                neurodata_type_inc='DynamicTableRegion',
                doc='Pointer to the rows of the electrodes table corresponding to the electrodes of this probe.',
            )
        ],
        links=[
            NWBLinkSpec(target_type='Shank',
                        doc=('The individual tetrode groups that are part of this shank. Not necessary if there is '
                             'only one shank on the probe'),
                        quantity='*'),
            NWBLinkSpec(target_type='Tetrode',
                        doc='The individual tetrode groups that are part of this shank.',
                        quantity='*')
        ]
    )

    new_data_types = [tetrode, shank, probe]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    # usage: python create_extension_spec.py
    main()
