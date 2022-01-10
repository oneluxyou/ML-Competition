args_resnet = {
    'epochs': 120,
    'optimizer_name': 'SGD',
    'optimizer_hyperparameters': {
        'lr': 1e-3,
        'momentum': 0.9,
        'weight_decay': 1e-4
    },
    'scheduler_name': 'CosineAnnealingLR',
    'scheduler_hyperparameters': {
        'T_max': 200
    },
    'batch_size': 256,
}
args_densenet = {
    'epochs': 1e-3,
    'optimizer_name': 'SGD',
    'optimizer_hyperparameters': {
        'lr': 0.1,
        'momentum': 0.9,
        'weight_decay': 1e-4
    },
    'scheduler_name': None,
    'batch_size': 256,
}