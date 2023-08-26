import numpy as np

class Perceptron:
    """
    Implementación de un Perceptrón simple.

    Atributos:
    -----------
    W : numpy array
        Vector de pesos, incluido el término de sesgo.
    epochs : int
        Número máximo de épocas para el entrenamiento.
    lr : float
        Tasa de aprendizaje.

    Métodos:
    --------
    activation_fn(x: float) -> int:
        Función de activación de escalón unitario.

    predict(x: numpy array) -> int:
        Realiza una predicción con el perceptrón.

    fit(X: numpy array, d: numpy array):
        Entrena el perceptrón con un conjunto de datos.

    Ejemplo:
    --------
    >>> p = Perceptron(input_size=2, lr=0.01, epochs=300)
    >>> X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    >>> y = np.array([0, 0, 0, 1])
    >>> p.fit(X, y)
    >>> p.predict(np.array([1, 1]))
    1
    """
    def __init__(self, input_size, lr=1.0, epochs=100):
        self.W = np.zeros(input_size + 1)
        self.epochs = epochs
        self.lr = lr

    def activation_fn(self, x):
        """Función de activación de escalón unitario."""
        return 1 if x >= 0 else 0

    def predict(self, x):
        """Realiza una predicción con el perceptrón."""
        x = np.insert(x, 0, 1)
        z = self.W.T.dot(x)
        return self.activation_fn(z)

    def fit(self, X, d):
        """Entrena el perceptrón con un conjunto de datos."""
        for _ in range(self.epochs):
            for i in range(d.shape[0]):
                x = np.insert(X[i], 0, 1)
                y = self.predict(X[i])
                e = d[i] - y
                self.W = self.W + self.lr * e * x
