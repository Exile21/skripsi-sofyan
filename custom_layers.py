from tensorflow.keras import backend as K
from tensorflow.keras.layers import Layer

# Custom RBF layer
class RBFLayer(Layer):
    def __init__(self, units, gamma, **kwargs):
        super(RBFLayer, self).__init__(**kwargs)
        self.units = units
        self.gamma = K.cast_to_floatx(gamma)

    def get_config(self):
        config = super(RBFLayer, self).get_config()
        config.update({'units': self.units, 'gamma': self.gamma})
        return config

    def build(self, input_shape):
        self.mu = self.add_weight(name='mu',
                                  shape=(int(input_shape[1]), self.units),
                                  initializer='uniform',
                                  trainable=True)
        super(RBFLayer, self).build(input_shape)

    def call(self, inputs):
        diff = K.expand_dims(inputs) - self.mu
        l2 = K.sum(K.pow(diff, 2), axis=1)
        res = K.exp(-1 * self.gamma * l2)
        return res
    
    def compute_output_shape(self, input_shape):
        return (input_shape[0], self.units)