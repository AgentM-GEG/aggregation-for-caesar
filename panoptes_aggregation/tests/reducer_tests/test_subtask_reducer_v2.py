from panoptes_aggregation import reducers
from .base_test_class import ReducerTestNoProcessing

extracted_data = [
    {
        'classifier_version': '2.0',
        'frame0': {
            'T0_tool0_x': [0.0, 100.0],
            'T0_tool0_y': [0.0, 100.0],
            'T0_tool0_subtask0': [
                {'0': 1},
                {'1': 1}
            ],
            'T0_tool0_subtask1': [
                {'value': [
                    {'option-1': 1},
                    {'option-2': 1},
                    {'None': 1}
                ]},
                {'value': [
                    {'option-3': 1},
                    {'option-4': 1},
                    {'option-5': 1}
                ]}
            ],
            'T0_tool1_x': [500.0],
            'T0_tool1_y': [500.0],
            'T0_tool1_subtask0': [
                {'1': 1}
            ],
            'T0_tool1_subtask1': [
                {'value': [
                    {'option-3': 1},
                    {'option-4': 1},
                    {'option-5': 1}
                ]}
            ]
        }
    },
    {
        'classifier_version': '2.0',
        'frame0': {
            'T0_tool0_x': [0.0, 100.0],
            'T0_tool0_y': [0.0, 100.0],
            'T0_tool0_subtask0': [
                {'1': 1},
                {'1': 1}
            ],
            'T0_tool0_subtask1': [
                {'value': [
                    {'option-1': 1},
                    {'option-2': 1},
                    {'option-3': 1}
                ]},
                {'value': [
                    {'option-1': 1},
                    {'option-4': 1},
                    {'option-5': 1}
                ]}
            ],
            'T0_tool1_x': [500.0],
            'T0_tool1_y': [500.0],
            'T0_tool1_subtask0': [
                {'1': 1}
            ],
            'T0_tool1_subtask1': [
                {'value': [
                    {'option-1': 1},
                    {'option-3': 1},
                    {'option-5': 1}
                ]}
            ]
        }
    },
    {
        'classifier_version': '2.0',
        'frame0': {
            'T0_tool1_x': [500.0],
            'T0_tool1_y': [500.0],
            'T0_tool1_subtask0': [
                {'0': 1}
            ],
            'T0_tool1_subtask1': [
                {'value': [
                    {'option-1': 1},
                    {'option-3': 1},
                    {'option-5': 1}
                ]}
            ]
        }
    }
]

reduced_data = {
    'classifier_version': '2.0',
    'frame0': {
        'T0_tool0_point_x': [0.0, 100.0, 0.0, 100.0],
        'T0_tool0_point_y': [0.0, 100.0, 0.0, 100.0],
        'T0_tool0_cluster_labels': [0, 1, 0, 1],
        'T0_tool0_clusters_count': [2, 2],
        'T0_tool0_clusters_x': [0.0, 100.0],
        'T0_tool0_clusters_y': [0.0, 100.0],
        'T0_tool0_subtask0': [
            {'0': 1},
            {'1': 1},
            {'1': 1},
            {'1': 1}
        ],
        'T0_tool0_subtask1': [
            {'value': [
                {'option-1': 1},
                {'option-2': 1},
                {'None': 1}
            ]},
            {'value': [
                {'option-3': 1},
                {'option-4': 1},
                {'option-5': 1}
            ]},
            {'value': [
                {'option-1': 1},
                {'option-2': 1},
                {'option-3': 1}
            ]},
            {'value': [
                {'option-1': 1},
                {'option-4': 1},
                {'option-5': 1}
            ]}
        ],
        'T0_tool0_clusters_subtask0': [
            {'0': 1, '1': 1},
            {'1': 2}
        ],
        'T0_tool0_clusters_subtask1': [
            {'value': [
                {'option-1': 2},
                {'option-2': 2},
                {'None': 1, 'option-3': 1}
            ]},
            {'value': [
                {'option-3': 1, 'option-1': 1},
                {'option-4': 2},
                {'option-5': 2}
            ]}
        ],
        'T0_tool1_point_x': [500.0, 500.0, 500.0],
        'T0_tool1_point_y': [500.0, 500.0, 500.0],
        'T0_tool1_cluster_labels': [0, 0, 0],
        'T0_tool1_cluster_count': [3],
        'T0_tool1_cluster_x': [500.0],
        'T0_tool1_clusters_y': [500.0],
        'T0_tool1_subtask0': [
            {'1': 1},
            {'1': 1},
            {'0': 1}
        ],
        'T0_tool1_subtask1': [
            {'value': [
                {'option-3': 1},
                {'option-4': 1},
                {'option-5': 1}
            ]},
            {'value': [
                {'option-1': 1},
                {'option-3': 1},
                {'option-5': 1}
            ]},
            {'value': [
                {'option-1': 1},
                {'option-3': 1},
                {'option-5': 1}
            ]}
        ],
        'T0_tool1_clusters_subtask0': [
            {'0': 1, '1': 2}
        ],
        'T0_tool1_clusters_subtask1': [
            {'value': [
                {'option-1': 2, 'option-3': 1},
                {'option-3': 2, 'option-4': 1},
                {'option-5': 3}
            ]}
        ]
    }
}

TestSubtaskReducerV2 = ReducerTestNoProcessing(
    reducers.shape_reducer_dbscan,
    extracted_data,
    reduced_data,
    'Test subtask reducer with classifier v2 extracts',
    kwargs={
        'shape': 'point',
        'eps': 5,
        'min_samples': 2,
        'details': {
            'T0_tool0_subtask0': 'question_reducer',
            'T0_tool0_subtask1': 'dropdown_reducer',
            'T0_tool1_subtask0': 'question_reducer',
            'T0_tool1_subtask1': 'dropdown_reducer'
        }
    },
    test_name='TestSubtaskReducerV2'
)
