Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\panderson1988\Desktop\Python\9-28 Notes (SAVE FOR THE LOVE OF GOD).py 
>>> 
 RESTART: C:\Users\panderson1988\Desktop\Python\9-28 Notes (SAVE FOR THE LOVE OF GOD).py 
>>> indexes('mississippi', 's')
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    indexes('mississippi', 's')
  File "C:\Users\panderson1988\Desktop\Python\9-28 Notes (SAVE FOR THE LOVE OF GOD).py", line 61, in indexes
    if word(index) == char:
TypeError: 'str' object is not callable
>>> 
 RESTART: C:\Users\panderson1988\Desktop\Python\9-28 Notes (SAVE FOR THE LOVE OF GOD).py 
>>> indexes('mississippi', 's')
[2, 3, 5, 6]
>>> lst_of_s = indexes('mississippi', 's')
>>> 
>>> 
 RESTART: C:\Users\panderson1988\Desktop\Python\9-28 Notes (SAVE FOR THE LOVE OF GOD).py 
>>> factorial(0)
1
>>> factorial(3)
6
>>> factorial(6)
720
>>> factorial(25)
15511210043330985984000000
>>> factorial (274)
36733598220785760101197668001508305208935557425488533969608495558907730794746205730904460603549444427934344148163836765439791065158049228160149161416274034654831598291704408530385394632800420883946896500159649542124436818314635253096698401080427052875616768530638234390264505609645466010121119335570768885165448913286697396892267622477064802891414367573068702043817353307162010453914271893318499792281921356338099648539114120311402041502806052900581870125154065449930541445325959200768000000000000000000000000000000000000000000000000000000000000000000
>>> 
 RESTART: C:\Users\panderson1988\Desktop\Python\9-28 Notes (SAVE FOR THE LOVE OF GOD).py 
>>> timesTables(2)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    timesTables(2)
TypeError: timesTables() takes 0 positional arguments but 1 was given
>>> timesTables()
times table for 2
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10

times table for 3
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15

times table for 4
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20

>>> 
=============================== RESTART: Shell ===============================
>>> t[0] [2]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    t[0] [2]
NameError: name 't' is not defined
>>> t = [[3,5,7], [0,2,1], [3,8,3]]
>>> t [0] [2]
7
>>> #Page 12
>>> m = [[3,5,7,9], [0,2,1,6], [3,8,3,1]]
>>> print2D(m)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print2D(m)
NameError: name 'print2D' is not defined
>>> #error occurred since I need to define it in a program
