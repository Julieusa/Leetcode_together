syms x y
a = 1 + x^2 + y^2;
b = exp(x*y);
u = x*(1-x)*y*(1-y);
dux = diff(u,x);
duy = diff(u,y);
f = -(diff(a*dux,x) + diff(b*duy,y)) + u;
simplify(f)