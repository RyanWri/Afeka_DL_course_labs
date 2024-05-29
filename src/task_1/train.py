"""
    Apply a simple neural network to this dataset, in order to perform classification. (You can
    use the `tensorflowlib.py` program from Moodle). Describe the results of different
    measures: accuracy, precision, recall, F1, sensitivity, and specificity.
"""

import tensorflow as tf

model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dense(10),
    ]
)
model.compile(
    optimizer=tf.keras.optimizers.Adam(0.001),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=[tf.keras.metrics.SparseCategoricalAccuracy()],
)

model.fit(
    ds_train,
    epochs=6,
    validation_data=ds_test,
)
