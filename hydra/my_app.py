from omegaconf import DictConfig, OmegaConf
import hydra
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import logging
from hydra.utils import instantiate


@hydra.main(version_base=None, config_path="conf", config_name="config")
def my_app(cfg: DictConfig) -> None:
    log = instantiate(cfg.logging)
    # print(OmegaConf.to_yaml(cfg))
    log.info("Info level message")
    log.debug("Debug level message")

    # Create a PyTorch neural network model
    class SimpleNet(nn.Module):
        def __init__(self):
            super(SimpleNet, self).__init__()
            self.fc = nn.Linear(784, 10)

        def forward(self, x):
            x = x.view(x.size(0), -1)
            x = self.fc(x)
            return x

    model = SimpleNet()

    learning_rate=0.001
    batch_size=64
    num_epochs=2
    # Define loss and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    # Load and preprocess the dataset (MNIST as an example)
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
    train_dataset = torchvision.datasets.MNIST(root='./data', train=True, transform=transform, download=True)
    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

    for epoch in range(num_epochs):
        for i, (images, labels) in enumerate(train_loader):
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()


    print("\nexperiment run finished")

if __name__ == "__main__":
    my_app()