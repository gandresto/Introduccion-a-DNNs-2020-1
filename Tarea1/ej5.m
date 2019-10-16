clear, clc
x1 = [0 0 1 1];
y1 = [0 1 1 -1];

x2 = [3 4 4 4 4];
y2 = [0 1 3 -1 -2];

x3 = [0 0 -1 -1 -2];
y3 = [-2 -3 -2 -3 -2];

M = zeros(3, 2);
M(1,:) = [mean(x1) mean(y1)];
M(2,:) = [mean(x2) mean(y2)];
M(3,:) = [mean(x3) mean(y3)];

S = zeros(3,2,2);
S(1,:,:) = cov(x1, y1);
S(2,:,:) = cov(x2, y2);
S(3,:,:) = cov(x3, y3);

Det = zeros(3,1);
Inv = zeros(3,2,2);

for i = 1:3 
    temp = reshape(S(i,:,:), 2, 2);
    Det(i) = det(temp);
    Inv(i,:,:) = inv(temp);
end

test = [2 2]
valores1 = zeros(3,1);
for i = 1:3
    valores1(i) = -log(Det(i))-(test-M(i))*reshape(Inv(i,:,:), 2, 2)*(test-M(i))';
end
[valormax1, clase1] = max(valores1)

test = [-1 -2]
valores2 = zeros(3,1);
for i = 1:3
    valores2(i) = -log(Det(i))-(test-M(i))*reshape(Inv(i,:,:), 2, 2)*(test-M(i))';
end
[valormax2, clase2] = max(valores2)