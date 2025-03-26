import torch
import torch.nn as nn

class RBM(nn.Module):
    def __init__(self, num_visible, num_hidden):
        super(RBM, self).__init__()
        self.num_visible = num_visible
        self.num_hidden = num_hidden
        self.weights = nn.Parameter(torch.randn(num_hidden, num_visible))
        self.bias_visible = nn.Parameter(torch.randn(num_visible))
        self.bias_hidden = nn.Parameter(torch.randn(num_hidden))

    def sample_hidden(self, visible_probabilities):
        hidden_activations = torch.sigmoid(torch.matmul(visible_probabilities, self.weights.t()) + self.bias_hidden)
        hidden_samples = torch.bernoulli(hidden_activations)
        return hidden_samples

    def sample_visible(self, hidden_probabilities):
        visible_activations = torch.sigmoid(torch.matmul(hidden_probabilities, self.weights) + self.bias_visible)
        visible_samples = torch.bernoulli(visible_activations)
        return visible_samples

    def free_energy(self, visible):
        energy = -torch.matmul(visible, self.bias_visible)
        energy -= torch.sum(torch.log(1 + torch.exp(torch.matmul(visible, self.weights.t()) + self.bias_hidden)), dim=1)
        return energy.mean()

# Creación de una RBM con 5 neuronas visibles y 3 neuronas ocultas
rbm = RBM(5, 3)

# Generación de un lote de datos de entrada
batch_size = 10
datos_entrada = torch.rand(batch_size, 5)

# Muestreo de la capa oculta
capa_oculta = rbm.sample_hidden(datos_entrada)

# Muestreo de la capa visible reconstruida
capa_visible_reconstruida = rbm.sample_visible(capa_oculta)

# Cálculo de la energía libre del sistema
energia_libre = rbm.free_energy(datos_entrada)
print("Energia libre del sistema:", energia_libre.item())
