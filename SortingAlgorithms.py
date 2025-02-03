'''Конечно уклончиво будет говорит, что каждый алгоритм подходит для каждой конкретной задачи,
но это так увы, другого ответа дать не могу. Могу лишь пояснить для каких ситуаций какой подходит.
Понятное дело, что ассимтотическое приближение у всх алгоритмов одинаковое в среднем, но по определению
О() приближение не учитывает константу на которую может быть домножено выражение, поэтому собственно
сортировка кучей и проигрывала по времени всем остальным. Каков итог?
Среднее время Быстрой сортировки 1.015921 секунд.
Среднее время Сортировки слиянием 1.841035 секунд.
Среднее время Сортировки кучей 2.926444 секунд.
Время Быстрой сортировки для отсортированного массива 0.993305 секунд.
Время Сортировки слиянием для отсортированного массива 1.449636 секунд.
Время Сортировки кучей для отсортированного массива 2.863451 секунд.
Время Быстрой сортировки для частично отсортированного массива 1.572037 секунд.
Время Сортировки слиянием для частично отсортированного массива 1.453650 секунд.
Время Сортировки кучей для частично отсортированного массива 2.819916 секунд.
Если характер данных в списке нам извествен, мы уверены что они случаные или около этого - однозначно
следует выбрать Быструю сортировку(банально времени меньше тратит). Если же характер значений не известен -
выбираем Сортировку слиянием - время чуть похуже, но стабильная работа с частично упорядоченными списками.
Если нужна стабильност и минимум дополнительной памяти - сортировка кучей, но тогда придется хранить список в виде
этой самой кучи.
P.s. привязывая ответ к вопросу - " который быстрее всего (по процессорным тикам)" - время отсчитывается как раз
по ним, так что говоря о времени в контексте программы, можно говорить и об тиках процессора.
P.p.s. Конечно некрасиво начинать наше общение с фейка, поэтому скажу честно, мне удобна пятидневка, но не с пн по пт, а все дни кроме чт и вт.
'''
