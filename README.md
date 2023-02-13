# Теория вероятностей и математическая статистика (семинары)

## Домашние Задания

### Урок 1. Расчет вероятности случайных событий

1. Из колоды в 52 карты извлекаются случайным образом 4 карты.
   a) Найти вероятность того, что все карты – крести.
   б) Найти вероятность, что среди 4-х карт окажется хотя бы один
   туз.

DZ1/DZ1_1.py

2. На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9.
   Код содержит три цифры, которые нужно нажать одновременно.
   Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?

DZ1/DZ1_2.py

3. В ящике имеется 15 деталей, из которых 9 окрашены.
   Рабочий случайным образом извлекает 3 детали.
   Какова вероятность того, что все извлеченные детали окрашены?

DZ1/DZ1_3.py

4.  В лотерее 100 билетов.
    Из них 2 выигрышных.
    Какова вероятность того, что 2 приобретенных билета окажутся
    выигрышными?

DZ1/DZ1_4.py

### Урок 2. Дискретные распределения вероятностей

1. Вероятность того, что стрелок попадет в мишень, выстрелив
   один раз, равна 0.8. Стрелок выстрелил 100 раз.
   Найдите вероятность того, что стрелок попадет в цель ровно 85
   раз.

DZ2/DZ2_1.py

2. Вероятность того, что лампочка перегорит в течение первого
   дня эксплуатации, равна 0.0004. В жилом комплексе после ремонта
   в один день включили 5000 новых лампочек. Какова вероятность,
   что ни одна из них не перегорит в первый день?
   Какова вероятность, что перегорят ровно две?

DZ2/DZ2_2.py

3. Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

DZ2/DZ2_3.py

4. В первом ящике находится 10 мячей, из которых 7 - белые. Во
   втором ящике - 11 мячей, из которых 9 белых.
   Из каждого ящика вытаскивают случайным образом по два мяча.
   Какова вероятность того, что все мячи белые?
   Какова вероятность того, что ровно два мяча белые?
   Какова вероятность того, что хотя бы один мяч белый?

DZ2/DZ2_4.py

### Урок 3. EDA (exploratory data analysis) или Разведочный анализ

1. Даны значения зарплат из выборки выпускников: 100, 80, 75,
   77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
   Посчитать (желательно без использования статистических методов
   наподобие std, var, mean) среднее арифметическое, среднее
   квадратичное отклонение, смещенную и несмещенную оценки
   дисперсий для данной выборки.

DZ3/DZ3_1.py

2. В первом ящике находится 8 мячей, из которых 5 - белые.
   Во втором ящике - 12 мячей, из которых 5 белых. Из первого
   ящика вытаскивают случайным образом два мяча, из второго - 4.
   Какова вероятность того, что 3 мяча белые?

DZ3/DZ3_2.py

3. На соревновании по биатлону один из трех спортсменов
   стреляет и попадает в мишень. Вероятность попадания для первого
   спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6.
   Найти вероятность того, что выстрел произведен:
   a). первым спортсменом
   б). вторым спортсменом
   в). третьим спортсменом.

DZ3/DZ3_3.py

4. В университет на факультеты A и B поступило равное
   количество студентов, а на факультет C студентов поступило
   столько же, сколько на A и B вместе.
   Вероятность того, что студент факультета A сдаст первую сессию,
   равна 0.8.
   Для студента факультета B эта вероятность равна 0.7, а для
   студента факультета C - 0.9. Студент сдал первую сессию.
   Какова вероятность, что он учится:
   a). на факультете A
   б). на факультете B
   в). на факультете C

DZ3/DZ3_4.py

5. Устройство состоит из трех деталей. Для первой детали
   вероятность выйти из строя в первый месяц равна 0.1, для второй - 0.2, для третьей - 0.25.
   Какова вероятность того, что в первый месяц выйдут из строя:
   а). все детали
   б). только две детали
   в). хотя бы одна деталь
   г). от одной до двух деталей?

DZ3/DZ3_5.py

### Урок 4. Непрерывная случайная величина

1. Случайная непрерывная величина A имеет равномерное распределение на промежутке (200, 800].
   Найдите ее среднее значение и дисперсию.

DZ4/DZ4_1.py

2. О случайной непрерывной равномерно распределенной величине B
   известно, что ее дисперсия равна 0.2.
   Можно ли найти правую границу величины B и ее среднее значение
   зная, что левая граница равна 0.5?
   Если да, найдите ее.

DZ4/DZ4_2.py

3. Непрерывная случайная величина X распределена нормально и
   задана плотностью распределения
   f(x) = (1 / (4\_ sqrt(2pi)))\_exp((-(x+2)\*\*2) / 32)
   Найдите:
   а). M(X)
   б). D(X)
   в). std(X) (среднее квадратичное отклонение)

DZ4/DZ4_3.py

4. Рост взрослого населения города X имеет нормальное распределение.
   Причем, средний рост равен 174 см, а среднее квадратичное
   отклонение равно 8 см.
   Какова вероятность того, что случайным образом выбранный
   взрослый человек имеет рост:
   а). больше 182 см
   б). больше 190 см
   в). от 166 см до 190 см
   г). от 166 см до 182 см
   д). от 158 см до 190 см
   е). не выше 150 см или не ниже 190 см
   ё). не выше 150 см или не ниже 198 см
   ж). ниже 166 см.

DZ4/DZ4_4.py

5. На сколько сигм (средних квадратичных отклонений)
   отклоняется рост человека, равный 190 см, от математического
   ожидания роста в популяции, в которой
   M(X) = 178 см и D(X) = 25 кв.см?

DZ4/DZ4_5.py

### Урок 5. Тестирование гипотез

1. Когда используется критерий Стьюдента, а когда Z –критерий?

   Задачи 2, 3 решать вручную.

2. Проведите тест гипотезы.
   Утверждается, что шарики для подшипников, изготовленные автоматическим станком,
   имеют средний диаметр 17 мм.
   Используя односторонний критерий с α=0,05, проверить эту
   гипотезу, если в выборке из n=100 шариков средний диаметр
   оказался равным 17.5 мм, а дисперсия известна и равна 4 кв.мм.

DZ5/DZ5_2.ipynb

3. Проведите тест гипотезы. Продавец утверждает, что средний вес пачки печенья составляет 200 г.
   Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет:
   202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
   Известно, что их веса распределены нормально.
   Верно ли утверждение продавца, если учитывать, что доверительная вероятность равна 99%?
   _Провести двусторонний тест_

   Задачу 4 решать с помощью функции.

4. Есть ли статистически значимые различия в росте дочерей и матерей?
   Рост матерей 172, 177, 158, 170, 178,175, 164, 160, 169
   Рост взрослых дочерей: 173, 175, 162, 174, 175, 168, 155, 170, 160

DZ5/DZ5.ipynb

### Урок 6. Сравнение долей. Построение доверительного интервала

1. Известно, что генеральная совокупность распределена нормально
   со средним квадратическим отклонением, равным 16.
   Найти доверительный интервал для оценки математического ожидания a с надежностью 0.95,
   если выборочная средняя M = 80, а объем выборки n = 256.

2. В результате 10 независимых измерений некоторой величины X, выполненных с одинаковой точностью,
   получены опытные данные:
   6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
   Предполагая, что результаты измерений подчинены нормальному закону распределения вероятностей,
   оценить истинное значение величины X при помощи доверительного интервала, покрывающего это
   значение с доверительной вероятностью 0,95.

3. Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
   Рост матерей 178, 165, 165, 173, 168, 155, 160, 164, 178, 175
   Используя эти данные построить 95% доверительный интервал для разности среднего роста родителей и детей.

DZ6/DZ6.ipynb

#### Урок 7. Непараметрические тесты

_1-4 задачи решать с помощью функций, 5ю вручную_
_Выбрать тест и проверить, есть ли различия между выборками:_

1. Даны две независимые выборки. Не соблюдается условие нормальности  
   x1 380,420, 290  
   y1 140,360,200,900  
   Сделайте вывод по результатам, полученным с помощью функции

2. Исследовалось влияние препарата на уровень давления пациентов. Сначала измерялось давление до приема препарата, потом через 10 минут и через 30 минут. Есть ли статистически значимые различия?  
   1е измерение до приема препарата: 150, 160, 165, 145, 155  
   2е измерение через 10 минут: 140, 155, 150, 130, 135  
   3е измерение через 30 минут: 130, 130, 120, 130, 125

3. Сравните 1 и 2 е измерения, предполагая, что 3го измерения через 30 минут не было.
4. Даны 3 группы учеников плавания.  
   В 1 группе время на дистанцию 50 м составляют:  
   56, 60, 62, 55, 71, 67, 59, 58, 64, 67  
   Вторая группа:  
   57, 58, 69, 48, 72, 70, 68, 71, 50, 53  
   Третья группа:  
   57, 67, 49, 48, 47, 55, 66, 51, 54  
   Есть ли различия между группами?

5. Заявляется, что партия изготавливается со средним арифметическим 2,5 см.  
    Проверить данную гипотезу, если известно, что размеры изделий подчинены нормальному закону распределения. Объем выборки 10, уровень статистической значимости 5%  
   2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34

DZ7/DZ7.ipynb

#### Урок 8. Корреляционный анализ

1. Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks):
   zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
   ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
   Найдите ковариацию этих двух величин с помощью элементарных действий, а затем с помощью функции cov из numpy
   Полученные значения должны быть равны.
   Найдите коэффициент корреляции Пирсона с помощью ковариации и среднеквадратичных отклонений двух признаков,
   а затем с использованием функций из библиотек numpy и pandas.

2. Измерены значения IQ выборки студентов,
   обучающихся в местных технических вузах:
   131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
   Известно, что в генеральной совокупности IQ распределен нормально.
   Найдите доверительный интервал для математического ожидания с надежностью 0.95.

3. Известно, что рост футболистов в сборной распределен нормально
   с дисперсией генеральной совокупности, равной 25 кв.см. Объем выборки равен 27,
   среднее выборочное составляет 174.2. Найдите доверительный интервал для математического
   ожидания с надежностью 0.95.

DZ8/DZ8.ipynb

#### Урок 9. Линейная регрессия Логистическая регрессия

1. Даны значения величины заработной платы заемщиков банка (zp) и значения их поведенческого кредитного скоринга (ks):  
   zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],  
   ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].  
   Используя математические операции, посчитать коэффициенты  
   линейной регрессии,  
   приняв за X заработную плату (то есть, zp - признак),  
   а за y - значения скорингового балла (то есть, ks - целевая переменная).  
   Произвести расчет как с использованием intercept, так и без.

2. Посчитать коэффициент линейной регрессии при заработной плате (zp), используя градиентный спуск (без intercept).

3. Произвести вычисления как в пункте 2, но с вычислением intercept.  
   Учесть, что изменение коэффициентов должно производиться
   на каждом шаге одновременно  
   (то есть изменение одного коэффициента не должно влиять на изменение другого во время одной итерации).

DZ9/DZ9.ipynb
