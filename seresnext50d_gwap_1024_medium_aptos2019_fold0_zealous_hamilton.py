hyperparameters = {
    "seed": 42,
    #   "fast": false,
    #   "mixup": false,
    #   "balance": false,
    #   "balance_datasets": false,
    #   "swa": false,
    #   "show": false,
    #   "use_idrid": false,
    #   "use_messidor": false,
    #   "use_aptos2015": false,
    # "use_aptos2019": "",
    # "verbose": "",
    #   "coarse": false,
    "accumulation-steps": 1,
    "data-dir": "/opt/ml/input/data",
    "model": "seresnext50d_gwap",
    "batch-size": 64,
    "epochs": 200,
    "early-stopping": 10,
    # "fold": [
    #     0,
    #     1,
    #     2,
    #     3
    # ],
    #   "freeze_encoder": false,
    "learning-rate": 0.0003,
    # "criterion_reg": [
    #     "mse"
    # ],
    #   "criterion_ord": null,
    # "criterion_cls": [
    #     "focal_kappa"
    # ],
    "l-1": 0.0002,
    # "l-2": 0,
    "optimizer": "AdamW",
    #   "preprocessing": null,
    #   "checkpoint": null,
    #   "workers": 64,
    "augmentations": "medium",
    #   "tta": null,
    #   "transfer": null,
    #   "fp16": true,
    "scheduler": "multistep",
    "size": 1024,
    "weight-decay": 0.0001,
    #   "weight_decay_step": null,
    "dropout": 0.4,
    # "warmup": 0,
    #   "experiment": null
}
