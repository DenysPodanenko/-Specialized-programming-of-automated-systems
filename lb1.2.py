import math
import itertools

'''#Вивести на екран рисунки:
print("  *\n ***\n*****\n ***\n  *");
print("*****\n** **\n* * *\n** **\n*****");
print("  *******\n *       *\n*  Hello  *\n *       *\n  *******");
#Вивести на екран текст:
a = int(input());
print(f"{a} {a} {a}\n {a} {a}\n{a} {a} {a}");
print(f"{a}-------{a}\n|   {a}   |\n{a}-------{a}");
#Зобразити на екрані декартову систему координат у вигляді
print("       ^ y\n\n       |       x\n-------+-+----->\n       | 1\n       |")

#Обчислити площу трикутника 𝑆 за трьома сторонами 𝑎, 𝑏, 𝑐.
a = int(input());
b = int(input());
c = int(input());
p = ((a+b+c)/2);
S = math.sqrt(p*(p-a)*(p-b)*(p-c));
print(S);
#1.10. Знайти довжини всіх медіан, бісектрис і висот трикутника,якщо відомі три сторони 𝑎, 𝑏, 𝑐.
a = int(input());
b = int(input());
c = int(input());
ma = 0.5*math.sqrt(2*pow(b,2)+2*pow(c,2)-pow(a,2));
mb = 0.5*math.sqrt(2*pow(a,2)+2*pow(c,2)-pow(b,2));
mc = 0.5*math.sqrt(2*pow(a,2)+2*pow(b,2)-pow(c,2));
print(ma," ",mb," ",mc);
#1.11. Обчислити відстань від точки (𝑥0, 𝑦0) до: a) заданої точки (𝑥, 𝑦); b) заданої прямої 𝑎𝑥 + 𝑏𝑦 + 𝑐 = 0; c) точки перетину прямих 𝑥 + 𝑏𝑦 + 𝑐 = 0 і 𝑎𝑥 + 𝑦 + 𝑐 = 0, де 𝑎𝑏 ≠ 1.
    #A
xA=int(input());
yA=int(input());
xB=int(input());
yB=int(input());
AB=math.sqrt(pow((xB-xA),2)+pow((yB-yA),2));
print(AB);
    #B
x0=int(input());
y0=int(input());
a=int(input());
b=int(input());
c=int(input());
d = (abs(a*x0+b*y0+c))/(math.sqrt(pow(a,2)+pow(b,2)));
print(d);
    #C
x=int(input());
y=int(input());
c=int(input());
a=(-y-c)/x;
b=(-x-c)/y;
print(a," ",b);
#1.12. Знайти об'єм циліндра, якщо відомо його радіус основи та висоту.
r=int(input());
h=int(input());
V=math.pi*pow(r,2)*h;
print(V);
#1.13. Знайти об'єм конуса, якщо відомо його радіус основи та висоту.
r=int(input());
h=int(input());
V=(h/3)*math.pi*pow(r,2);
print(V);
#1.14. Знайти об'єм тора з внутрішнім радіусом r і зовнішнім радіусом R.
r=int(input());
R=int(input());
V=2*pow(math.pi,2)*R*pow(r,2);
print(V);
#1.15. Вважаючи, що Земля має форму сфери радіуса 𝑅 = 6350 км, знайти відстань до лінії горизонту від точки із заданою висотою ℎ над Землею.
R=6350;
h=float(input());
d=math.sqrt(2*R*h);
print(d);
#1.16. Без попередніх алгебраїчних перетворень обчислити значення арифметичних виразів:
#A
a=int(input());
b=int(input());
c=int(input());
y=(c+(a/(pow(a,2)+pow(b,2))))/(a+(b/(pow(b,2)+pow(c,2))));
print(y);
#B
y=1+(1/(2+(1/(3+(1/4)))));
print(y);
#1.17. Наближено визначити період обертання Землі навколо Сонця, використовуючи ланцюговий дріб
T=int(input());
for i in range(4):
    num=int(input())
    T=num+1/T;
print(T);
#1.18. Скласти програми для розв'язання рівнянь:
#A
b=int(input());
c=int(input());
x=(c-b)/(4.2343);
print(x);
#B
b=int(input());
d=int(input());
x=(-b)/(5.23);
y=(-d)/(-2.4);
print(x," ",y);
#C
a=int(input());
c=int(input());
b=int(input());
d=int(input());
x=(d-b)/(a-c);
print(x);
#Розв'язати квадратне рівняння 𝑎𝑥2 + 𝑏𝑥 + 𝑐 = 0, де коефіцієнти
a=int(input());
b=int(input());
c=int(input());
D=pow(b,2)-4*a*c;
x1=(-b+math.sqrt(D))/(2*a);
x2=(-b-math.sqrt(D))/(2*a);
print(x1," ",x2);
#Дано дійсне число x. Користуючись тільки операцією множення, отримати:
#A
x=int(input());
x2=x*x;
x4=x2*x2;
#B
x=int(input());
x2=x*x;
x4=x2*x2;
x6=x4*x2;
#C
x=int(input());
x2=x*x;
x4=x2*x2;
x8=x4*x4;
x9=x8*x;
#D
x=int(input());
x2=x*x;
x4=x2*x2;
x5=x4*x;
x10=x5*x5;
x15=x10*x5;
#E
x=int(input());
x2=x*x;
x4=x2*x2;
x8=x4*x4;
x16=x8*x8;
x24=x16*x8;
x28=x24*x4;
#F
x=int(input());
x2=x*x;
x4=x2*x2;
x8=x4*x4;
x16=x8*x8;
x32=x16*x16;
x64=x32*x32;
#Не використовуючи операцію піднесення до степеня, обчислити значення многочлена для введеного з клавіатури значення x за найменшу кількість арифметичних операцій:
#A
x=int(input());
x2=x*x;
x3=x2*x;
x4=x2*x2;
y=x4+x3+x2+x+1;
#B
x=int(input());
x2=x*x;
x4=x2*x2;
y=x4+2*x2+1;
#C
x=int(input());
x2=x*x;
x3=x2*x;
x4=x3*x;
x5=x4*x;
y=x5+5*x4+10*x3+10*x2+5*x+1;
#D
x=int(input());
x2=x*x;
x3=x2*x;
x9=x3*x3*x3;
y=x9+x3+1;
#E
x=int(input());
x2=x*x;
x3=x2*x;
x4=x2*x2;
y=16*x4+8*x3+4*x2+2*x+1;
#F
x=int(input());
x2=x*x;
x3=x2*x;
x5=x2*x3;
y=x5+x3+x;
#Скласти програму для обчислення значення многочлена від двох змінних для введеної з клавіатури пари чисел (𝑥, 𝑦):
x=int(input());
y=int(input());
#A
f=(pow(x,3)+3*pow(x,2)*y+3*x*pow(y,2)+pow(y,3));
#B
f=(pow(x,2)*pow(y,2)+pow(x,3)*pow(y,3)+pow(x,4)*pow(y,4));
#C
f=(x+y+pow(x,2)+pow(y,2)+pow(x,3)+pow(y,3)+pow(x,4)+pow(y,4));
#Скласти програму взаємного обміну значень цілих змінних x та y:
x=int(input());
y=int(input());
#A
tmp = x;
x=y;
y=tmp;
#B
x=x+y;
y=x-y;
x=x-y;
#1.24. Дано натуральне тризначне число. Знайти:
num=input();
#A
unit = num[2];
dozen=num[1];
hundered=num[0];
print(unit," ",dozen," ",hundered);
#B
print(num[::-1]);
#Дано натуральне тризначне число, у якому всі цифри різні. Знайти всі числа, утворені при перестановці цифр заданого числа.
num=input();
print(list(itertools.permutations(num)));
#Від тризначного числа x відняли його останню цифру. Після ділення результату на 10 до частки ліворуч дописали останню цифру числа 𝑥 та отримали число n. За заданим числом n знайти вихідне число x. Вважати, що 10 < 𝑛 < 999, а число десятків у 𝑛 не дорівнює нулю.
n = input();
x=n[2]+n[1]+n[0];
print(x);
#У тризначному числі x закреслено першу цифру. Якщо отримане число помножити на 10 і добуток додати до першої цифри числа x, то буде отримано число n. За заданим числом n, 1 < 𝑛 < 999 знайти число x.
n=input();
x=n[2]+n[0]+n[1];
print(x);
#Тіло починає рухатися без початкової швидкості з прискоренням 𝑎. Обчислити:
#A
a=int(input());
t=int(input());
S=(a*pow(t,2))/2
print(S);
#B
a=int(input());
v=int(input());
t=v/a;
print(t);'''
#Обчислити кінетичну енергію тіла масою 𝑚, що рухається зі швидкістю 𝑣 відносно поверхні Землі.
m=int(input());
v=int(input());
E=(m*pow(v,2))/2;
print(E);