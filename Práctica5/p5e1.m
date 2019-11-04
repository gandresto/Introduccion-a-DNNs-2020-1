net = newp([-1 1;-1 1; -1 1], [0 1]);
P = [1 1; -1 1; -1 -1]
T = [0 1]
net.IW{1, 1, 1} = [1 -1 -0.5]; % Inicializar pesos
net.b{1} = 1; % Inicializar sesgo
Y = net(P),  net.trainParam.epochs = 20; net = train(net,P,T); Y = net(P) % Entrenamiento de la red

Test = [1 0 1; -1 -1 0]'
a = sim(net, Test) % Evaluacion de la red